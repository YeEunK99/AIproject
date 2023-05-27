import streamlit as st
import cv2

st.title('CCTV시스템')

vid_file = open("web/cars.avi", "rb").read()
st.video(vid_file, start_time=2)

