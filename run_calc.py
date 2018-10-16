# run_calc.py

import pyautogui, sys, time
import subprocess
import os

pyautogui.FAILSAFE = False

# place mouse on screen to start iRIC (if multiple screens)
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
