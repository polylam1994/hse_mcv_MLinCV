# -*- coding: utf-8 -*-
"""
Created on Mon May 23 11:30:03 2022

@author: 6495
"""

from . import common
import numpy as np
import torch
import torch.nn.functional as F
import cv2
import os
from argparse import ArgumentParser
from openvino.inference_engine import IECore


def build_argparser():
    parser = ArgumentParser()
    parser.add_argument(
        "-d",
        "--device",
        help="Specify the target device to infer on; CPU, GPU, FPGA or MYRIAD is acceptable. \
                                                Sample will look for a suitable plugin for device specified (CPU by default)",
        default="CPU",
        type=str,
    )
    return parser


def nms(objs, iou=0.5):

    if objs is None or len(objs) <= 1:
        return objs

    objs = sorted(objs, key=lambda obj: obj.score, reverse=True)
    keep = []
    flags = [0] * len(objs)
    for index, obj in enumerate(objs):

        if flags[index] != 0:
            continue

        keep.append(obj)
        for j in range(index + 1, len(objs)):
            if flags[j] == 0 and obj.iou(objs[j]) > iou:
                flags[j] = 1
    return keep


def detect(exec_net, input_blob, image, threshold=0.4, nms_iou=0.5):

    # image = ((image / 255.0 - mean) / std).astype(np.float32)
    image = image.transpose(2, 0, 1)
    outputs = exec_net.infer(inputs={input_blob: image})
    # print('outputs:', outputs)
    # print('outputs[\'Sigmoid_526\'].shape:', outputs['Sigmoid_526'].shape)
    # print('outputs[\'Exp_527\'].shape:', outputs['Exp_527'].shape)
    # print('outputs[\'Conv_525\'].shape:', outputs['Conv_525'].shape)
    # hm, box, landmark = outputs['Sigmoid_526'], outputs['Exp_527'], outputs['Conv_525']
    hm, box, landmark = outputs["1028"], outputs["1029"], outputs["1027"]

    # print('outputs:', outputs)
    # print('outputs[\'1028\'].shape:', outputs['1028'].shape)
    # print('outputs[\'1029\'].shape:', outputs['1029'].shape)
    # print('outputs[\'1027\'].shape:', outputs['1027'].shape)

    hm = torch.from_numpy(hm).clone()
    box = torch.from_numpy(box).clone()
    landmark = torch.from_numpy(landmark).clone()

    hm_pool = F.max_pool2d(hm, 3, 1, 1)
    scores, indices = ((hm == hm_pool).float() * hm).view(1, -1).cpu().topk(1000)

    hm_height, hm_width = hm.shape[2:]

    scores = scores.squeeze()
    indices = indices.squeeze()
    ys = list((indices / hm_width).int().data.numpy())
    xs = list((indices % hm_width).int().data.numpy())
    # ys = list((indices / hm_height).int().data.numpy())
    # xs = list((indices % hm_width).int().data.numpy())
    scores = list(scores.data.numpy())

    box = box.cpu().squeeze().data.numpy()
    landmark = landmark.cpu().squeeze().data.numpy()

    stride = 4
    objs = []
    for cx, cy, score in zip(xs, ys, scores):

        if score < threshold:

            break

        x, y, r, b = box[:, cy, cx]
        xyrb = (np.array([cx, cy, cx, cy]) + [-x, -y, r, b]) * stride
        x5y5 = landmark[:, cy, cx]
        x5y5 = (common.exp(x5y5 * 4) + ([cx] * 5 + [cy] * 5)) * stride
        box_landmark = list(zip(x5y5[:5], x5y5[5:]))
        objs.append(common.BBox(0, xyrb=xyrb, score=score, landmark=box_landmark))

    return nms(objs, iou=nms_iou)


def image_demo(jpg, show_image=True):

    # args = build_argparser().parse_args()
    # model_xml = "openvino/480x640/FP32/dbface_mbnv3_480x640_opt.xml" #<--- CPU
    model_xml = os.path.dirname(__file__) + "/openvino/480x640/FP32/dbface_mbnv3_480x640_opt.xml"  # <--- CPU
    # model_xml = "openvino/480x640/FP16/dbface.xml" #<--- MYRIAD
    model_bin = os.path.splitext(model_xml)[0] + ".bin"
    ie = IECore()
    net = ie.read_network(model=model_xml, weights=model_bin)
    input_blob = next(iter(net.input_info))
    exec_net = ie.load_network(network=net, device_name="CPU")

    # jpg = input("Enter .jpg .jpeg file name absolute path: ")

    frame = cv2.imread(jpg)

    img = cv2.resize(frame, (640, 480))

    objs = detect(exec_net, input_blob, img)

    for obj in objs:
        common.drawbbox(img, obj)

    if show_image:
        cv2.imshow("demo", img)
        cv2.waitKey()
        cv2.destroyAllWindows()

    return (img)

if __name__ == "__main__":
    image_demo()
