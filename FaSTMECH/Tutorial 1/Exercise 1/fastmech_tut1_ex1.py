# fastmech_tut1_ex1.py

import pyautogui, sys, time
import subprocess
import os
import tkinter as tk
import winreg

# initialize iric by clearing registry
try:
    winreg.DeleteKey(winreg.HKEY_CURRENT_USER, 'Software\\iRIC Organization\\iRIC GUI\\networkproxy')
    winreg.DeleteKey(winreg.HKEY_CURRENT_USER, 'Software\\iRIC Organization\\iRIC GUI')
    winreg.DeleteKey(winreg.HKEY_CURRENT_USER, 'Software\\iRIC Organization\\iRIC GUI 3\\backgroundgrid')
    winreg.DeleteKey(winreg.HKEY_CURRENT_USER, 'Software\\iRIC Organization\\iRIC GUI 3\\general')
    winreg.DeleteKey(winreg.HKEY_CURRENT_USER, 'Software\\iRIC Organization\\iRIC GUI 3\\geodatapointmapwebimporter')
    winreg.DeleteKey(winreg.HKEY_CURRENT_USER, 'Software\\iRIC Organization\\iRIC GUI 3\\graphics')
    winreg.DeleteKey(winreg.HKEY_CURRENT_USER, 'Software\\iRIC Organization\\iRIC GUI 3\\gridcheck')
    winreg.DeleteKey(winreg.HKEY_CURRENT_USER, 'Software\\iRIC Organization\\iRIC GUI 3\\tmsimage')
    winreg.DeleteKey(winreg.HKEY_CURRENT_USER, 'Software\\iRIC Organization\\iRIC GUI 3')
    winreg.DeleteKey(winreg.HKEY_CURRENT_USER, 'Software\\iRIC Organization')
except WindowsError:
    pass

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
# User left double click on "iRIC (list item)" in "Program Manager"
iricIcon = pyautogui.locateCenterOnScreen('../../../iricIcon-no-shortcut-2012.png')
if iricIcon is None:
    print("Didn't locate iricIcon-no-shortcut-2012.png")
    sys.exit(0)
pyautogui.doubleClick(iricIcon)
time.sleep(5.0)
pyautogui.screenshot("StartIRIC-{}x{}.png".format(screenWidth, screenHeight))

# cancel maintenance if visible
# User left click on "Cancel (button)" in "Check for Update"
maintainanceButtons = pyautogui.locateOnScreen('../../../maintainanceButtons-2012.png')
if maintainanceButtons is None:
    print("Didn't locate maintainanceButtons-2012.png")
else:
    pyautogui.moveTo(maintainanceButtons[LEFT] + 189, maintainanceButtons[TOP] + maintainanceButtons[HEIGHT]/2)  # this might not be necessary (needs further testing - at least for iric installers)
    pyautogui.click(maintainanceButtons[LEFT] + 189, maintainanceButtons[TOP] + maintainanceButtons[HEIGHT]/2)
time.sleep(1.0)
pyautogui.screenshot("AfterMaintainance-{}x{}.png".format(screenWidth, screenHeight))

# close Start Page
# User left click on "Close Enter (button)" in "iRIC Start Page"
closeButton = pyautogui.locateCenterOnScreen('../../../closeButton-2012.png')
if closeButton is None:
    print("Didn't locate closeButton-2012.png")
    sys.exit(0)
pyautogui.moveTo(closeButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(closeButton)
time.sleep(1.0)
pyautogui.screenshot("AfterStartPage-{}x{}.png".format(screenWidth, screenHeight))

# maximize main window
maximizeButton = pyautogui.locateCenterOnScreen('../../../maximizeButton-2012.png')
if maximizeButton is None:
    print("Didn't locate maximizeButton-2012.png")
    sys.exit(0)
pyautogui.moveTo(maximizeButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(maximizeButton)
time.sleep(1.0)
pyautogui.screenshot("Maximized-{}x{}.png".format(screenWidth, screenHeight))

# start new porject
pyautogui.hotkey('ctrl', 'n')

# doubleClick on "FaSTMECH (list item)" in "Select Solver"
newFaSTMECH = pyautogui.locateCenterOnScreen('newFaSTMECH-2012.png')
if newFaSTMECH is None:
    print("Didn't locate newFaSTMECH-2012.png")
    sys.exit(0)
pyautogui.moveTo(newFaSTMECH)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.doubleClick(newFaSTMECH)
time.sleep(1.0)
pyautogui.screenshot("newFaSTMECH-{}x{}.png".format(screenWidth, screenHeight))

# maximize preprocessor window
# User left click on "Pre-processing Window (window)" in "Untitled - iRIC 3.0.7.6238 [FaSTMECH]"
preProcessingMaximize = pyautogui.locateCenterOnScreen('preProcessingMaximize-2012.png')
if preProcessingMaximize is None:
    print("Didn't locate preProcessingMaximize-2012.png")
    sys.exit(0)
pyautogui.moveTo(preProcessingMaximize)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(preProcessingMaximize)
time.sleep(1.0)
pyautogui.screenshot("preProcessingMaximize-{}x{}.png".format(screenWidth, screenHeight))

# Import r5finpt2m114_shifted.tpo
pyautogui.typewrite(['alt', 'i', 'e', 'enter'], interval=.1)
pyautogui.typewrite(os.getcwd()+'\\r5finpt2m114_shifted.tpo\n', interval=.1)
pyautogui.typewrite(['tab', 'enter'], interval=.2)
time.sleep(1.0)
pyautogui.screenshot("importElevation-{}x{}.png".format(screenWidth, screenHeight))

# copy and paste file name
# this doesn't seem to work
## r = tk.Tk()
## r.withdraw()
## r.clipboard_clear()
## r.clipboard_append(os.getcwd()+'\\r5finpt2m114_shifted.tpo')
## r.update()
## pyautogui.typewrite(['alt', 'i', 'e', 'enter'], interval=.1)
## time.sleep(0.5)
## pyautogui.hotkey('ctrl', 'v')
## time.sleep(0.5)
## pyautogui.typewrite(['enter', 'enter'], interval=.1)
## r.destroy()

# The Pre-processing Window now displays the topography data on the canvas and the data you imported
# appears in the Object Browser under Geographic Data | Elevation | Points1 (Figure 3). In the Object
# Browser the topography can be made visible or not visible by checking or unchecking the box next to
# Elevation.

# uncheck points
selectedChecked = pyautogui.locateCenterOnScreen('selectedChecked-2012.png')
if selectedChecked is None:
    print("Didn't locate selectedChecked-2012.png")
    sys.exit(0)
pyautogui.moveTo(selectedChecked)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(selectedChecked)
time.sleep(1.0)
pyautogui.screenshot("selectedChecked-{}x{}.png".format(screenWidth, screenHeight))

# re-check points
selectedUnchecked = pyautogui.locateCenterOnScreen('selectedUnchecked-2012.png')
if selectedUnchecked is None:
    print("Didn't locate selectedUnchecked-2012.png")
    sys.exit(0)
pyautogui.moveTo(selectedUnchecked)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(selectedUnchecked)
time.sleep(1.0)
pyautogui.screenshot("selectedUnchecked-{}x{}.png".format(screenWidth, screenHeight))

# To adjust how the elevation points are displayed, select in the Object Browser Geographic Data |
# Elevation | Points1 and then right-click to access a dialog that allows you to edit the data name in the
# Object Browser, Export the data, Delete the data, and adjust Properties. Select “Property” and change the
# point size to 1 (Figure 4). 

# right-click Points->Property... and change points to 1
pointsItem = pyautogui.locateCenterOnScreen('pointsItem-2012.png')
if pointsItem is None:
    print("Didn't locate pointsItem-2012.png")
    sys.exit(0)
pyautogui.moveTo(pointsItem)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.rightClick(pointsItem)
time.sleep(0.1)
pyautogui.typewrite(['down', 'down', 'down', 'down', 'down', 'down', 'enter'], interval=.1)
pyautogui.typewrite(['tab', '1', 'tab', 'tab', 'enter'], interval=.1)
pyautogui.screenshot("pointsItemOne-{}x{}.png".format(screenWidth, screenHeight))

# Add a data legend for the elevation data by selecting in the Object Browser Geographic Data | Elevation
# and then right-clicking and in the resulting pop-up menu selecting “Set up Scalarbar”. Make sure Elevation
# is displayed in the drop-down menu and check the “Visible” box. Select the “Edit” button for additional
# features that control the legend display, or simply select OK and left-click on the legend and drag to a new
# location. 

# right-click Elevation->Set up Scalarbar
elevationItem = pyautogui.locateCenterOnScreen('elevationItem-2012.png')
if elevationItem is None:
    print("Didn't locate elevationItem-2012.png")
    sys.exit(0)
pyautogui.moveTo(elevationItem)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.rightClick(elevationItem)
pyautogui.typewrite(['up', 'enter'], interval=.1)
pyautogui.typewrite(['enter'], interval=.1)
time.sleep(0.1)
pyautogui.screenshot("elevationItem-{}x{}.png".format(screenWidth, screenHeight))

# drag scalarbar
pyautogui.moveTo(863, 547)
pyautogui.dragRel(-460, -35)
time.sleep(0.5)
pyautogui.screenshot("dragScalarbar-{}x{}.png".format(screenWidth, screenHeight))

# To change the range and intervals displayed in the data legend select Menu Bar Geographic Data -> Color
# Setting -> Elevation. This opens a dialog that allows you to change the minimum and maximum elevation
# colors (Figure 5). Uncheck “Automatic” and change the maximum to 840 to see more detail in the channel.
# Select OK.

# Geographic Data->Color Setting->Elevation and set max to 840
pyautogui.typewrite(['alt', 'e', 'down', 'down', 'down', 'down', 'down', 'enter', 'enter'], interval=.1)
pyautogui.typewrite(['tab', 'tab', 'space', 'tab', '8', '4', '0', 'tab', 'tab', 'tab', 'enter'], interval=.1)
time.sleep(1.5)
pyautogui.screenshot("setMaxScalarbar-{}x{}.png".format(screenWidth, screenHeight))

# minimize window to know when finished
minimizeButton = pyautogui.locateCenterOnScreen('../../../minimizeButton-2012.png')
if minimizeButton is None:
    print("Didn't locate minimizeButton-2012.png")
    sys.exit(0)
pyautogui.moveTo(minimizeButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(minimizeButton)
time.sleep(1.0)

# place mouse at middle of screen
pyautogui.moveTo(screenWidth / 2, screenHeight / 2)
print("Finished")
