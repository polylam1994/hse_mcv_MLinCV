# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 15:31:23 2022

@author: Sea
"""

import numpy as np
import streamlit as st
from PIL import Image
from hse_mcv_dbface import demo

st.title("DBFace, the human face detector")

img_upload = st.file_uploader("Upload image", type=["jpg", "jpeg", "png"])

if img_upload is not None:
    img = Image.open(img_upload)
    st.image(img, "Input")

    img_array = np.array(img.convert("RGB"))

    output = demo.image_demo(img_array,show_image=False)
    st.image(output, "output")