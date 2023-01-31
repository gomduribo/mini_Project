import streamlit as st
import pandas as pd
import numpy as np

st.title('Detecting objects using YOLO')

st.subheader('Upload your image')
uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # uploaded_file.getvalues:
    # To read file as byte
    bytes_data = uploaded_file.getvalue()
    st.image(bytes_data)
else:
    st.write("There is no image yet!")