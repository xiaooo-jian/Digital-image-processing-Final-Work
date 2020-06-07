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
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (45, 45))  # 定义结构元素
closing = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)  # 闭运算

labeled = cv2.imread("test3.png")
image = cv2.resize(labeled, (1280, 720), interpolation=cv2.INTER_CUBIC)
cnts, hierarchy = cv2.findContours(closing, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

for i in range(0, len(cnts)):
    x, y, w, h = cv2.boundingRect(cnts[i])
    cv2.rectangle(image, (x, y), (x + w, y + h), (153, 153, 0), 5)
    newimage = image[y + 2:y + h - 2, x + 2:x + w - 2]  # 先用y确定高，再用x确定宽
    if newimage.shape[0] < 50 or newimage.shape[1] < 50:
        continue
    cv2.imshow("1", newimage)
    cv2.waitKey()

image = cv2.drawContours(image, cnts, -1, (0, 0, 255), 3)
cv2.imshow("1", image)
cv2.waitKey()
