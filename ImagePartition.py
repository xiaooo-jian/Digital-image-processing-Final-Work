import pytesseract as tess
import numpy as np
import cv2

lower_white = np.array([0, 0, 221])
upper_white = np.array([180, 30, 255])


def CardPartition(img):
    HSV_img = cv2.cvtColor(img, cv2.COLOR_RGB2HSV)
    mask = cv2.inRange(HSV_img, lower_white, upper_white)
    HSV_img = cv2.bitwise_and(HSV_img, HSV_img, mask=mask)
    img2 = cv2.cvtColor(HSV_img, cv2.COLOR_HSV2RGB)
    gray = cv2.cvtColor(img2, cv2.COLOR_RGB2GRAY)

    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (20, 20))  # 定义结构元素
    closing = cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel)  # 闭运算
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (45, 45))  # 定义结构元素
    opening = cv2.morphologyEx(closing, cv2.MORPH_OPEN, kernel)  # 闭运算

    cnts, hierarchy = cv2.findContours(opening, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

    res = []
    for i in range(0, len(cnts)):
        x, y, w, h = cv2.boundingRect(cnts[i])
        cv2.rectangle(img, (x, y), (x + w, y + h), (153, 153, 0), 5)
        newimage = gray[y + 2:y + h - 2, x + 2:x + w - 2]  # 先用y确定高，再用x确定宽
        '''cv2.imshow("1", newimage)
        cv2.waitKey()'''
        res.append(newimage)
    return res


def getHandCard(img):
    handCard = img[500:700, :]
    card = CardPartition(handCard)[0]
    res_card = card[0:int(card.shape[0] / 3.4), :]
    kerhel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (4, 1))
    res_card = cv2.morphologyEx(res_card, cv2.MORPH_CLOSE, kerhel2, iterations=1)
    '''cv2.imshow("1",res_card)
    cv2.waitKey()'''
    return res_card


def getMasterCard(img):
    masterCard = img[0:150, 500:800]
    card = CardPartition(masterCard)
    '''print(len(card))'''
    if len(card) == 0:
        return False
    return True


def getOutCard(img):
    outCard = img[250:430, 300:980]  # 划分手牌、地主牌、出牌区域，方便进行识别
    cards = CardPartition(outCard)
    res_cards = []
    for card in cards:
        res_card = card[0:int(card.shape[0] / 3.5), :]
        kerhel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 1))
        res_card = cv2.morphologyEx(res_card, cv2.MORPH_CLOSE, kerhel2, iterations=1)
        '''cv2.imshow("1", res_card)
        cv2.waitKey()'''
        res_cards.append(res_card)
    return res_cards


