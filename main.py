import time
import numpy as np
import pydirectinput as pd
import pyscreenshot as ImageGrab
import cv2
import pytesseract
pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

time.sleep(3)

flag = True
while flag:
    time.sleep(3)
    pd.press('q')
    time.sleep(1)
    pd.press('DOWN')
    pd.press('ENTER')
    pd.press('q')
    pd.press('e')
    pd.press('DOWN')
    pd.press('DOWN')

    pd.press('DOWN')
    pd.press('DOWN')
    pd.press('ENTER')
    time.sleep(1)

    filename = 'Image.png'
    x = 1

    while (True):
        screen = np.array(ImageGrab.grab(bbox=(0, 0, 542, 198)))
        cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
        cv2.imwrite(filename, screen)
        x = x + 1
        if x == 2:
            cv2.destroyAllWindows()
            break

    img = cv2.imread('Image.png')
    text = pytesseract.image_to_string(img, lang='rus')

    if "штраф" in text:
        time.sleep(2)
        pd.moveTo(104, 137)
        time.sleep(1)
        pd.click(button="right")
        time.sleep(1)
        pd.moveTo(203, 375)
        time.sleep(1)
        pd.click()
        time.sleep(1)
        pd.moveTo(1034, 570)
        time.sleep(1)
        pd.click()
        time.sleep(1)
        pd.moveTo(1057, 738)
        time.sleep(1)
        pd.click()
        time.sleep(1)
        pd.moveTo(959, 1065)
        time.sleep(1)
        pd.click()
        time.sleep(1)
        pd.press("F9")
        time.sleep(4)
    else:
        flag = False
