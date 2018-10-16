# run_iric_install.py

import pyautogui, sys, time
import subprocess
import os

pyautogui.KEYBOARD_KEYS

# left = location[0]; top = location[1]; width = location[2]; height = location[3]
LEFT = 0
TOP = 1
WIDTH = 2
HEIGHT = 3

pyautogui.FAILSAFE = False

# place mouse on screen to start iRIC (if multiple screens)
pyautogui.moveTo(1, 1)

# verify resolution
screenWidth, screenHeight = pyautogui.size()
print("Screen resolution: {}x{}".format(screenWidth, screenHeight))

# start iRIC install
subprocess.Popen("iRIC_Offline_Installer_prod.exe")
time.sleep(2.0)
pyautogui.screenshot("iRIC_Offline_Installer_prod-{}x{}-0.png".format(screenWidth, screenHeight))

# click next
nextButton = pyautogui.locateCenterOnScreen('iRIC_Offline_Installer_prod-1024x768-NextButton-2012.png')
if nextButton is None:
    print("Didn't locate iRIC_Offline_Installer_prod-1024x768-NextButton-2012.png")
    sys.exit(0)

pyautogui.moveTo(nextButton)
pyautogui.click(nextButton)
time.sleep(1.0)
pyautogui.screenshot("iRIC_Offline_Installer_prod-{}x{}-1.png".format(screenWidth, screenHeight))
