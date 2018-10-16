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


# find upper left
left, top, width, height = pyautogui.locateOnScreen('upperLeft.png')

# move the mouse so nothing is highlighted
pyautogui.moveTo(left - 1, top - 1)
time.sleep(2.0)


# find upper left
left, top, width, height = pyautogui.locateOnScreen('lowerRight.png')

# move the mouse so nothing is highlighted
pyautogui.moveTo(left + width + 1, top + height + 1)
time.sleep(2.0)
pyautogui.screenshot("screenshot-{}x{}-3.png".format(screenWidth, screenHeight))


pyautogui.hotkey('alt', '1')  # Alt+1 to set Standard
time.sleep(2.0)
pyautogui.screenshot("screenshot-{}x{}-final.png".format(screenWidth, screenHeight))

# start iRIC install
subprocess.Popen("iRIC_Offline_Installer_prod.exe")
time.sleep(2.0)
pyautogui.screenshot("iRIC_Offline_Installer_prod-{}x{}-0.png".format(screenWidth, screenHeight))

# click next
nextButton = pyautogui.locateCenterOnScreen('iRIC_Offline_Installer_prod-1024x768-NextButton.png')
pyautogui.click(nextButton)
time.sleep(0.5)
pyautogui.screenshot("iRIC_Offline_Installer_prod-{}x{}-1.png".format(screenWidth, screenHeight))
