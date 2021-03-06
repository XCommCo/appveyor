# run_iric.py

import pyautogui, sys, time
import subprocess
import os
import tkinter as tk

# left = location[0]; top = location[1]; width = location[2]; height = location[3]
LEFT = 0
TOP = 1
WIDTH = 2
HEIGHT = 3

pyautogui.FAILSAFE = False

# # place mouse on screen to start iRIC (if multiple screens)
# pyautogui.moveTo(1, 1)

# verify resolution
screenWidth, screenHeight = pyautogui.size()
print("Screen resolution: {}x{}".format(screenWidth, screenHeight))

# place mouse at middle of screen
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)

# minimize everything
pyautogui.hotkey('win', 'm')
time.sleep(1.0)
pyautogui.screenshot("Desktop-{}x{}.png".format(screenWidth, screenHeight))

# start iRIC (Don't include the shortcut overlay for additional compatibility)
# see iricIcon-2012.diff.png
iricIcon = pyautogui.locateCenterOnScreen('iricIcon-no-shortcut-2012.png')
if iricIcon is None:
    print("Didn't locate iricIcon-no-shortcut-2012.png")
    sys.exit(0)
pyautogui.doubleClick(iricIcon)
time.sleep(5.0)
pyautogui.screenshot("StartIRIC-{}x{}.png".format(screenWidth, screenHeight))

# cancel maintenance if visible
maintainanceButtons = pyautogui.locateOnScreen('maintainanceButtons-2012.png')
if maintainanceButtons is None:
    print("Didn't locate maintainanceButtons-2012.png")
else:
    pyautogui.moveTo(maintainanceButtons[LEFT] + 189, maintainanceButtons[TOP] + maintainanceButtons[HEIGHT]/2)  # this might not be necessary (needs further testing - at least for iric installers)
    pyautogui.click(maintainanceButtons[LEFT] + 189, maintainanceButtons[TOP] + maintainanceButtons[HEIGHT]/2)
time.sleep(1.0)
pyautogui.screenshot("AfterMaintainance-{}x{}.png".format(screenWidth, screenHeight))

# close Start Page
closeButton = pyautogui.locateCenterOnScreen('closeButton-2012.png')
if closeButton is None:
    print("Didn't locate closeButton-2012.png")
    sys.exit(0)
pyautogui.moveTo(closeButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(closeButton)
time.sleep(1.0)
pyautogui.screenshot("AfterStartPage-{}x{}.png".format(screenWidth, screenHeight))

# maximize main window
maximizeButton = pyautogui.locateCenterOnScreen('maximizeButton-2012.png')
if maximizeButton is None:
    print("Didn't locate maximizeButton-2012.png")
    sys.exit(0)
pyautogui.moveTo(maximizeButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(maximizeButton)
time.sleep(1.0)
pyautogui.screenshot("Maximized-{}x{}.png".format(screenWidth, screenHeight))

# restore main window
restoreButton = pyautogui.locateCenterOnScreen('restoreButton-2012.png')
if restoreButton is None:
    print("Didn't locate restoreButton-2012.png")
    sys.exit(0)
pyautogui.moveTo(restoreButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(restoreButton)
time.sleep(1.0)
pyautogui.screenshot("Restored-{}x{}.png".format(screenWidth, screenHeight))

# close main window
xButton = pyautogui.locateCenterOnScreen('xButton-2012.png')
if xButton is None:
    print("Didn't locate xButton-2012.png")
    sys.exit(0)
pyautogui.moveTo(xButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(xButton)
time.sleep(1.0)
pyautogui.screenshot("Closed-{}x{}.png".format(screenWidth, screenHeight))

# place mouse at middle of screen
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
