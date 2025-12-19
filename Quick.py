import cv2
import numpy as np
import time
import mss
import pydirectinput

pydirectinput.FAILSAFE = False
pydirectinput.PAUSE = 0

repair = cv2.imread("repair_button.png", 0)
exit_btn = cv2.imread("exit_garage_button.png", 0)
success = cv2.imread("purchase_success_text.png", 0)

rh, rw = repair.shape
eh, ew = exit_btn.shape
sh, sw = success.shape

CONF = 0.7

REPAIR_REGION = {"top": 0, "left": 0, "width": 500, "height": 300}
SUCCESS_REGION = {"top": 0, "left": 1200, "width": 720, "height": 250}
EXIT_REGION = {"top": 650, "left": 1100, "width": 800, "height": 400}
FULL_REGION = {"top": 0, "left": 0, "width": 1920, "height": 1080}

sct = mss.mss()

repaired = False
confirmed = False

def locatenclick(template, w, h, region):
    img = np.array(sct.grab(region))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, max_loc = cv2.minMaxLoc(res)
    if max_val >= CONF:
        x = region["left"] + max_loc[0] + w // 2
        y = region["top"] + max_loc[1] + h // 2
        pydirectinput.moveRel(1, 0)
        pydirectinput.moveRel(-1, 0)
        pydirectinput.moveTo(x, y)
        pydirectinput.click()
        return True
    return False

def locateonly(template, region):
    img = np.array(sct.grab(region))
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    res = cv2.matchTemplate(gray, template, cv2.TM_CCOEFF_NORMED)
    _, max_val, _, _ = cv2.minMaxLoc(res)
    return max_val >= CONF

while True:
    if not repaired:
        if locatenclick(repair, rw, rh, REPAIR_REGION):
            repaired = True
            confirmed = False
            time.sleep(0.15)
        else:
            time.sleep(0.02)
        continue

    if repaired and not confirmed:
        if locateonly(success, SUCCESS_REGION):
            confirmed = True
            time.sleep(0.2)
        else:
            time.sleep(0.02)
        continue

    if confirmed:
        if locatenclick(exit_btn, ew, eh, EXIT_REGION):
            repaired = False
            confirmed = False
            time.sleep(0.05)
            continue

        if locatenclick(exit_btn, ew, eh, FULL_REGION):
            repaired = False
            confirmed = False
            time.sleep(0.05)
            continue

    time.sleep(0.02)
