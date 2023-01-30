import streamlit as st
import cv2
import numpy as np
from PIL import Image

def preprocessing(image, thres):
    image = cv2.cvtColor(image, cv2.COLOR_RGB2HSV)
    lower = np.array(thres[0], dtype="uint8")
    upper = np.array(thres[1], dtype="uint8")
    mask = cv2.inRange(image, lower, upper)
        
    blur = cv2.GaussianBlur(mask, (5, 5), 1)
    canny = cv2.Canny(blur, 50, 150)  
    kernel = np.ones((3, 3), np.uint8)
    dilated = cv2.dilate(canny, kernel, iterations=6)
    cnt, hierarchy = cv2.findContours(dilated.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    return cnt

# Allow user to upload an image
image_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if image_file is not None:
    # Open the image
    image = Image.open(image_file)
    image = np.array(image)
    original = image.copy()
    # Show the image
    st.image(original, caption='Original Image', use_column_width=True)

    # Yellow Vibrio
    yellow_thres = [[22, 93, 0],[45, 255, 255]]
    yellow_cnt = preprocessing(image, yellow_thres)

    yellow_count = 0
    yellow_areas = []

    for c in yellow_cnt:
        area = cv2.contourArea(c)
        yellow_areas.append(area)

    for i in range(len(yellow_cnt)):
        if (1000 < yellow_areas[i] < 40000):
            yellow_count += 1
            cv2.drawContours(original, yellow_cnt[i], -1, (255, 255, 0), 3)

    # Green Vibrio
    green_thres = [[40, 100, 100],[90, 255, 255]]
    green_cnt = preprocessing(image, green_thres)

    green_count = 0
    green_areas = []

    for c in green_cnt:
        area = cv2.contourArea(c)
        green_areas.append(area)

    for i in range(len(green_cnt)):
        if (10000 < green_areas[i] < 40000):
            green_count += 1
            cv2.drawContours(original, green_cnt[i], -1, (0, 255, 0), 3)

    # # Show image
    st.image(original, use_column_width=True)
    st.text('yellow: '+ str(yellow_count*10))
    st.text('green: '+ str(green_count*10))

