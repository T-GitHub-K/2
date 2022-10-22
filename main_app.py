import streamlit as st
from PIL import Image
# streamlit run c:/Users/user/mysite/2/main_app.py

# テキスト
st.title('SAMPLE APL')
st.caption('これはSAMPLEテストアプリです。')

image = Image.open('./data/012.jpg')
st.image(image, width=200)

# 動画
video_file = open('./data/file.mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
