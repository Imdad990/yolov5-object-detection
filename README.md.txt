# 🧠 YOLOv5 Object Detection Web App

This is a simple yet powerful object detection web application built using **YOLOv5** and **Streamlit**. It allows users to upload images and get real-time object detection results in the browser.

## 🚀 Features

- Object detection using pre-trained YOLOv5s model
- Built-in Streamlit web interface
- Works fully inside Google Colab
- Deployable via ngrok link
- Real-time image detection

## 🛠️ Tech Stack

- Python
- YOLOv5
- OpenCV
- Streamlit
- Ngrok

## 📷 Sample Output

![sample](sample_detection.png)

## ▶️ How to Run in Google Colab

1. Upload the following files to Google Colab:
   - `app.py`
   - `requirements.txt`
   - `yolov5s.pt`

2. Run this in a Colab cell:

```bash
!pip install -r requirements.txt
!streamlit run app.py &>/content/log.txt &



3 Connect with Ngrok
from pyngrok import ngrok
ngrok.set_auth_token("YOUR_AUTH_TOKEN")
public_url = ngrok.connect(port=8501)
print("App running on:", public_url)



##Requirement
streamlit
pyngrok
torch
opencv-python
Pilow

Contact
For freelancing or collaborations: iukhan990@gmail.com

