import streamlit as st
import torch
import cv2
import numpy as np
from PIL import Image

st.set_page_config(page_title="YOLOv5 Object Detection", layout="wide")

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')

st.title("🔍 Real-Time Object Detection using YOLOv5")
st.write("Upload an image or video and detect objects using YOLOv5.")

option = st.radio("Select Input Type", ['Image', 'Video'])

if option == 'Image':
    uploaded_file = st.file_uploader("Upload Image", type=['jpg', 'png', 'jpeg'])
    if uploaded_file is not None:
        file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
        img = cv2.imdecode(file_bytes, 1)
        st.image(img, caption='Original Image', use_column_width=True)
        results = model(img)
        res_img = results.render()[0]
        st.image(res_img, caption='Detected Image', use_column_width=True)

elif option == 'Video':
    uploaded_vid = st.file_uploader("Upload Video", type=['mp4', 'avi', 'mov'])
    if uploaded_vid is not None:
        with open("temp_vid.mp4", "wb") as f:
            f.write(uploaded_vid.read())
        cap = cv2.VideoCapture("temp_vid.mp4")
        stframe = st.empty()
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            results = model(frame)
            annotated_frame = results.render()[0]
            stframe.image(annotated_frame, channels="BGR", use_column_width=True)
        cap.release()
