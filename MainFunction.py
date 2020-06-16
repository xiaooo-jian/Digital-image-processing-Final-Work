import ImageCapture as ic
import ImagePartition as ip
import Tencent as te
import cv2


def HandCardRegnziion():
    img = ic.screenShot()
    card = ip.getHandCard(img)
    texts = te.text_recognition(card)
    print(texts)
    card_text = ""
    for text in texts:
        card_text += text
    card_text = card_text.replace(" ", "")
    card_text = card_text.replace("I", "1")
    card_text = card_text.replace("10", "T")  # 转换其他符号代表10
    card_text = card_text.replace("0", "Q")

    print(card_text)
    card_list = list(card_text)
    if card_list[0] == 'J':
        card_list[0] = '王'
    if card_list[1] == 'J':
        card_list[1] = '王'
    print(card_list)

    card_num = {"王": 2, "2": 4, "A": 4, "K": 4, "Q": 4, "J": 4, "10": 4, "9": 4, "8": 4, "7": 4, "6": 4, "5": 4,
                "4": 4, "3": 4}
    for card in card_list:
        if card == "T":
            card_num["10"] -= 1
        else:
            card_num[card] -= 1
    return card_num


def OutCardRegnziion(card_num):
    img = ic.screenShot()
    cards = ip.getOutCard(img)
    for card in cards:
        texts = te.text_recognition(card)
        print(texts)
        card_text = ""
        for text in texts:
            card_text += text
        card_text = card_text.replace(" ", "")
        card_text = card_text.replace("I", "1")

        card_text = card_text.replace("J0", "JT")  # 识别错误修正
        card_text = card_text.replace("10", "T")  # 转换其他符号代表10
        card_text = card_text.replace("0", "Q")
        print(card_text)
        card_list = list(card_text)
        print(card_list)
        for c in card_list:
            if c not in ['A', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'K', 'Q', 'T']:
                continue
            if c == "T":
                card_num["10"] -= 1
            else:
                card_num[c] -= 1
    return card_num
