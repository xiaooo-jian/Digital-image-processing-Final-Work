import numpy as np
import cv2

# 读取图片并且进行预处理
def processImg(path):
    '''
    path: 图片路径
    '''
    img = cv2.imread(path)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (3, 3), 1)
    ret, th1 = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU )
    # 开闭运算去除噪点
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3,3))
    th1 = cv2.morphologyEx(th1, cv2.MORPH_OPEN, kernel)
    th1 = cv2.morphologyEx(th1, cv2.MORPH_CLOSE, kernel)
    edge = cv2.Canny(th1, 50, 100)

    return th1, img, edge

# 利用轮廓处理获取roi
def getRoi(img, binary):
    '''
    img: 原图
    binary: 预处理后得到的canny边缘
    '''
    # 寻找轮廓
    contours,_ = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    roi_list = []

    # 判断出圆形区域
    for cnt in range(len(contours)):
        area = cv2.contourArea(contours[cnt])
        # 判断提取所需的轮廓，经验值需要调试获取
        if 4000 < area < 10000:
            # 获取外接矩形的值
            x,y,w,h = cv2.boundingRect(contours[cnt])
            roi_list.append((x,y,w,h))
            cv2.rectangle(img, (x,y),(x+w, y+h),(0,255,0),2)
            cv2.drawContours(img, [contours[cnt]], 0, (255, 0, 255), 2)

    return img, roi_list

# Save the roi
def saveRoi(src, roi_list):
    '''
    src: 原图的copy
    roi_list: List,保存的roi位置信息
    '''
    for i in range(len(roi_list)):
        x, y, w, h = roi_list[i]
        roi = src[y:y+h, x:x+w]
        cv2.imwrite("money_roi/roi_%d.jpg"%i, roi)
        print("No.%02d Finished! "%i)

if __name__ == '__main__':

    th1, img, edge = processImg("test2.png")
    img = cv2.resize(img,(1280,720))
    th1 = cv2.resize(th1,(1280,720))
    edge = cv2.resize(edge,(1280,720))
    # copy img
    src = img.copy()
    # 获取roi
    img, roi_list = getRoi(img, edge)

    # 保存roi
    saveRoi(src, roi_list)

    # Display images.
    cv2.imshow("Thresholded Image", th1)
    cv2.imwrite("money_contour_binary.jpg", th1)

    cv2.imshow("edge", edge)
    cv2.imwrite("money_contour_edge.jpg", edge)

    cv2.imshow("roi image", img)
    cv2.imwrite("money_contour_out.jpg", img)

    cv2.waitKey(0)
    cv2.destroyAllWindows()