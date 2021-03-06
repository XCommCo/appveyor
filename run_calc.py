# run_calc.py

import pyautogui, sys, time
import subprocess
import os

# left = location[0]; top = location[1]; width = location[2]; height = location[3]
LEFT = 0
TOP = 1
WIDTH = 2
HEIGHT = 3

pyautogui.FAILSAFE = False

# place mouse on screen to start calc (if multiple screens)
pyautogui.moveTo(1, 1)

# verify resolution
screenWidth, screenHeight = pyautogui.size()
print("Screen resolution: {}x{}".format(screenWidth, screenHeight))

pyautogui.screenshot("screenshot-{}x{}-0.png".format(screenWidth, screenHeight))

# place mouse at middle of screen
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)

# start calculator
subprocess.Popen("calc.exe")
time.sleep(5.0)

pyautogui.screenshot("screenshot-{}x{}-1.png".format(screenWidth, screenHeight))

# Set to Scientific (Alt+2)
pyautogui.hotkey('alt', '2')
time.sleep(2.0)

pyautogui.screenshot("screenshot-{}x{}-2.png".format(screenWidth, screenHeight))


# find upper left
#left, top, width, height = pyautogui.locateOnScreen('upperLeft.png')
location = pyautogui.locateOnScreen('upperLeft-2012.png')
if location is None:
    print("Didn't locate upperLeft-2012.png")
    sys.exit(0)

# move the mouse so nothing is highlighted
# left = location[0]; top = location[1]; width = location[2]; height = location[3]
pyautogui.moveTo(location[LEFT] - 1, location[TOP] - 1)
time.sleep(2.0)

# find upper left
location = pyautogui.locateOnScreen('lowerRight-2012.png')
if location is None:
    print("Didn't locate lowerRight-2012.png")
    sys.exit(0)
else:
    left, top, width, height = location

# move the mouse so nothing is highlighted
pyautogui.moveTo(left + width + 1, top + height + 1)
time.sleep(2.0)
pyautogui.screenshot("screenshot-{}x{}-3.png".format(screenWidth, screenHeight))

# reset to Standard (Alt+1)
pyautogui.hotkey('alt', '1')
time.sleep(2.0)
pyautogui.screenshot("screenshot-{}x{}-final.png".format(screenWidth, screenHeight))

# close calc
pyautogui.hotkey('alt', 'f4')
