import streamlit as st
import torch
from torchvision import transforms
from PIL import Image, ImageOps
import numpy as np
import cv2
from ocr_model import *


def app():
    @st.cache(allow_output_mutation=True, ttl=3600)
    def convert_from_cv2_to_img(img: np.ndarray) -> Image:
        return Image.fromarray(img)

    def convert_from_img_to_cv2(img: Image) -> np.ndarray:
        return np.asarray(img)

    st.write("""
            # Detection & Covering of NumPlate
            """
             )

    file = st.file_uploader("Please upload an car image", type=["jpg", "jpeg"])
    st.set_option('deprecation.showfileUploaderEncoding', False)

    if file is None:
        st.text("Please upload an image file")
    else:

        image = Image.open(file)
        st.write("""
                # Original Image
                """
                 )
        st.image(image, use_column_width=True)

        img = convert_from_img_to_cv2(image)
        result = find_numplate(img)
        st.image(result, use_column_width=True)
