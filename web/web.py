import cv2
import streamlit as st

def main():
    st.title("Multiple Video Display Example")

    # 첫 번째 영상 파일 불러오기
    video_path1 = "C:/User/admin/PycharmProjects/web/demo.avi"
    video1 = cv2.VideoCapture(video_path1)

    # 두 번째 영상 파일 불러오기
    video_path2 = "C:/User/admin/PycharmProjects/web/cars.avi"
    video2 = cv2.VideoCapture(video_path2)

    # 영상 프레임별 처리 및 출력
    while True:
        ret1, frame1 = video1.read()
        ret2, frame2 = video2.read()

        if not ret1 or not ret2:
            break

        # 첫 번째 영상 출력
        st.image(frame1, channels="BGR", caption="Video 1")

        # 두 번째 영상 출력
        st.image(frame2, channels="BGR", caption="Video 2")

if __name__ == "__main__":
    main()
