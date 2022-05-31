# -*- coding: utf-8 -*-
"""
Created on Tue May 31 14:48:55 2022

@author: 6495
"""


import os.path as osp
import numpy as np
import pytest
from hse_mcv_dbface import demo


def prepare_image_names(list_of_short_names):
    path_to_images = osp.abspath(osp.dirname(__file__)) + "/test_images/"
    images_for_testing = [path_to_images + image for image in list_of_short_names]
    return images_for_testing


# A regression test using a single image that checks results are always the same
@pytest.mark.parametrize("image_name", prepare_image_names(["test.jpg"]))
def test_regression(image_name):
    first_result = demo.image_demo(image_name, show_image=False)
    second_result = demo.image_demo(image_name, show_image=False)
    assert np.array_equal(first_result, second_result)


# A “no error” test with big image, small image
@pytest.mark.parametrize("image_name", prepare_image_names(["small.jpg", "big.jpg"]))
def test_for_errors_on_images_of_different_sizes(image_name):
    demo.image_demo(image_name, show_image=False)
