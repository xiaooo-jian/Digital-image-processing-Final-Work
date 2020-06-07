import numpy as np
import cv2

lower_white = np.array([0, 0, 221])
upper_white = np.array([180, 30, 255])

img = cv2.imread("test3.png")
img = cv2.resize(img, (1280, 720), interpolation=cv2.INTER_CUBIC)

img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
mask = cv2.inRange(img, lower_white, upper_white)
img = cv2.bitwise_and(img, img, mask=mask)
img = cv2.cvtColor(img, cv2.COLOR_HSV2RGB)
gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20))  # 定义结构元素
closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)  # 闭运算
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20))  # 定义结构元素
closing = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)  # 闭运算


res = cv2.GaussianBlur(closing, (5, 5), 5)
labeled = cv2.imread("test3.png")
labeled = cv2.resize(labeled, (1280, 720), interpolation=cv2.INTER_CUBIC)
cnts, hierarchy = cv2.findContours(res, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
image = cv2.drawContours(labeled, cnts, -1, (0, 0, 255), 3)

cv2.imshow("1", image)

"""cv2.imshow("1", th1[535:600, 270:935])"""
cv2.waitKey()
