import streamlit as st 


st.title("upload")

ulfile = st.file_uploader("photo")


img_file_buffer = st.camera_input("Take a picture")
if img_file_buffer is not None:
    st.image(img_file_buffer)