import streamlit as st
import cv2


def main():
    st.title("영상 출력 예제")

    # 첫 번째 영상 출력
    st.subheader("첫 번째 영상")
    video1 = cv2.VideoCapture("cars.avi")
    st.video(video1)

    # 두 번째 영상 출력
    st.subheader("두 번째 영상")
    video2 = cv2.VideoCapture("demo.avi")
    st.video(video2)


if __name__ == "__main__":
    main()
