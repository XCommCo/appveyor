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
time.sleep(2.0)

pyautogui.screenshot("screenshot-{}x{}-1.png".format(screenWidth, screenHeight))

pyautogui.hotkey('alt', '2')  # Alt+2 to set Scientific
time.sleep(2.0)

pyautogui.screenshot("screenshot-{}x{}-2.png".format(screenWidth, screenHeight))

pyautogui.hotkey('alt', '1')  # Alt+1 to set Standard
time.sleep(2.0)

pyautogui.screenshot("screenshot-{}x{}-3.png".format(screenWidth, screenHeight))
