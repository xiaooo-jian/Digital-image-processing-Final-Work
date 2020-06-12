import pytesseract as tess
import cv2


def recognize_text(img):
    gray = cv2.cvtColor(img[0:int(img.shape[0] / 3.4), :], cv2.COLOR_BGR2GRAY)
    ret, binnary = cv2.threshold(gray, 200, 255, cv2.THRESH_OTSU)

    kerhel2 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
    bin2 = cv2.morphologyEx(binnary, cv2.MORPH_CLOSE, kerhel2, iterations=1)

    text = tess.image_to_string(bin2)

    print(text.replace(' ', ''))
    cv2.imshow("binary_img", bin2)
    cv2.waitKey()
    return text.replace(' ', '')




img = cv2.imread("handcard2.png")
recognize_text(img)
