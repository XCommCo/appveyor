# Nays2DH_tut1.py

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
type_interval = 0.02

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
# User left double click on "iRIC (list item)" in "Program Manager"
iricIcon = pyautogui.locateCenterOnScreen('../../iricIcon-no-shortcut-2012.png')
#{
print(type(iricIcon))
print(type(['alt', 'g', 's']))
print(['alt', 'g', 's'] + 4*['tab'])
print(['tab', 'down'] + 4*['tab'] + list('60') + ['tab'] + list('0.01') + ['tab', '0'] + 4*['tab'])
orig=['tab', 'space', 'space', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'right', '0', '.', '0', '0', '4', 'enter', 'tab', 'tab', '1', '8', '0', '0', 'enter', 'right', '0', '.', '0', '0', '4', 'enter', 'enter']
new=['tab'] + 2*['space'] + 6*['tab'] + ['right'] + list('0.004') + ['enter'] + 2*['tab'] + list('1800') + ['enter', 'right'] + list('0.004') + 2*['enter']
print(type(new))
print((orig>new)-(orig<new))
##sys.exit(0)
#}
if iricIcon is None:
    print("Didn't locate iricIcon-no-shortcut-2012.png")
    pyautogui.hotkey('win', 'm')
    sys.exit(0)
pyautogui.doubleClick(iricIcon)
time.sleep(5.0)
pyautogui.screenshot("StartIRIC-{}x{}.png".format(screenWidth, screenHeight))

# cancel maintenance if visible
# User left click on "Cancel (button)" in "Check for Update"
maintainanceButtons = pyautogui.locateOnScreen('../../maintainanceButtons-2012.png')
if maintainanceButtons is None:
    print("Didn't locate maintainanceButtons-2012.png")
else:
    pyautogui.moveTo(maintainanceButtons[LEFT] + 189, maintainanceButtons[TOP] + maintainanceButtons[HEIGHT]/2)  # this might not be necessary (needs further testing - at least for iric installers)
    pyautogui.click(maintainanceButtons[LEFT] + 189, maintainanceButtons[TOP] + maintainanceButtons[HEIGHT]/2)
time.sleep(1.0)
pyautogui.screenshot("AfterMaintainance-{}x{}.png".format(screenWidth, screenHeight))

# close Start Page
# User left click on "Close Enter (button)" in "iRIC Start Page"
closeButton = pyautogui.locateCenterOnScreen('../../closeButton-2012.png')
if closeButton is None:
    print("Didn't locate closeButton-2012.png")
    pyautogui.hotkey('win', 'm')
    sys.exit(0)
pyautogui.moveTo(closeButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(closeButton)
time.sleep(1.0)
pyautogui.screenshot("AfterStartPage-{}x{}.png".format(screenWidth, screenHeight))

# maximize main window
maximizeButton = pyautogui.locateCenterOnScreen('../../maximizeButton-2012.png')
if maximizeButton is None:
    print("Didn't locate maximizeButton-2012.png")
    pyautogui.hotkey('win', 'm')
    sys.exit(0)
pyautogui.moveTo(maximizeButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(maximizeButton)
time.sleep(1.0)
pyautogui.screenshot("Maximized-{}x{}.png".format(screenWidth, screenHeight))

# start new project
pyautogui.hotkey('ctrl', 'n')
time.sleep(1.0)
pyautogui.screenshot("SelectSolver-{}x{}.png".format(screenWidth, screenHeight))

# doubleClick on "Nays2DH (list item)" in "Select Solver"
newNays2DH = pyautogui.locateCenterOnScreen('newNays2DH-2012.png')
if newNays2DH is None:
    print("Didn't locate newNays2DH-2012.png")
    pyautogui.hotkey('win', 'm')
    sys.exit(0)
pyautogui.moveTo(newNays2DH)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.doubleClick(newNays2DH)
time.sleep(1.0)
pyautogui.screenshot("newNays2DH-{}x{}.png".format(screenWidth, screenHeight))

# maximize preprocessor window
# User left click on "Pre-processing Window (window)" in "Untitled - iRIC 3.0.7.6238 [FaSTMECH]"
preProcessingMaximize = pyautogui.locateCenterOnScreen('preProcessingMaximize-2012.png')
if preProcessingMaximize is None:
    print("Didn't locate preProcessingMaximize-2012.png")
    pyautogui.hotkey('win', 'm')
    sys.exit(0)
pyautogui.moveTo(preProcessingMaximize)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(preProcessingMaximize)
time.sleep(1.0)
pyautogui.screenshot("preProcessingMaximize-{}x{}.png".format(screenWidth, screenHeight))

# Selecte Algorithm to Create Grid
pyautogui.typewrite(['alt', 'g', 's'], interval=type_interval)
time.sleep(1.0)

# Double-Right-Click MultifunctionGridGenarator-2012.png
# User left double click on "Multifunction Grid Genarator (list item)" in "Select Grid Creating Algorithm" 
multifunctionGridGenarator = pyautogui.locateCenterOnScreen('MultifunctionGridGenarator-2012.png')
if multifunctionGridGenarator is None:
    print("Didn't locate MultifunctionGridGenarator-2012.png")
    pyautogui.hotkey('win', 'm')
    sys.exit(0)
pyautogui.moveTo(multifunctionGridGenarator)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.doubleClick(multifunctionGridGenarator)
time.sleep(1.0)
pyautogui.screenshot("multifunctionGridGenarator-{}x{}.png".format(screenWidth, screenHeight))

# Channel Shape
pyautogui.typewrite(['tab', 'tab', 'tab', 'tab', 'down', 'tab', 'tab'], interval=type_interval)
time.sleep(0.5)
pyautogui.screenshot("channelShape-{}x{}.png".format(screenWidth, screenHeight))

# Cross Sectional Shape Para...
pyautogui.typewrite(['down', 'tab', 'tab', 'tab', 'tab', '0', '.', '3', 'tab', '1', '6', 'tab'], interval=type_interval)
time.sleep(0.5)
pyautogui.screenshot("crossSectional-{}x{}.png".format(screenWidth, screenHeight))

# Channel Shape Parameters
pyautogui.typewrite(['down', 'tab', 'tab', 'tab', 'tab', '4', '.', '7', 'tab', 'tab', '2', '8', '.', '6', 'tab', '4', '0', 'tab'], interval=type_interval)
time.sleep(0.5)
pyautogui.screenshot("channelShapeParameters-{}x{}.png".format(screenWidth, screenHeight))

# Bed and Channel Slope
pyautogui.typewrite(['down', 'tab', 'tab', 'tab', 'tab', 'tab', '0', '.', '0', '0', '4', 'tab', 'tab', 'tab', 'space'], interval=type_interval)
time.sleep(0.5)
pyautogui.screenshot("bedAndChannel-{}x{}.png".format(screenWidth, screenHeight))

# Yes to 'Do you want to map geographic data...'
pyautogui.typewrite(['alt', 'y'], interval=type_interval)
time.sleep(1.0)
pyautogui.screenshot("bedAndChannel-{}x{}.png".format(screenWidth, screenHeight))

# select Cell attributes in Object Browser and expand
cellAttributes = pyautogui.locateCenterOnScreen('CellAttributes-2012.png')
if cellAttributes is None:
    print("Didn't locate CellAttributes-2012.png")
    pyautogui.hotkey('win', 'm')
    sys.exit(0)
pyautogui.moveTo(cellAttributes)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(cellAttributes)
time.sleep(0.5)
#pyautogui.typewrite(['space', 'left', 'down', 'down', 'down', 'down', 'down', 'space'], interval=type_interval)
pyautogui.typewrite(['space', 'right', 'down', 'down', 'down', 'down', 'down', 'space'], interval=type_interval)
pyautogui.screenshot("cellAttributes-{}x{}.png".format(screenWidth, screenHeight))

upperLeftCanvas = pyautogui.locateCenterOnScreen('upperLeftCanvas-2012.png')
if upperLeftCanvas is None:
    print("Didn't locate upperLeftCanvas-2012.png")
    pyautogui.hotkey('win', 'm')
    sys.exit(0)

lowerRightCanvas = pyautogui.locateCenterOnScreen('lowerRightCanvas-2012.png')
if lowerRightCanvas is None:
    print("Didn't locate lowerRightCanvas-2012.png")
    pyautogui.hotkey('win', 'm')
    sys.exit(0)

# select entire computational grid
pyautogui.moveTo(upperLeftCanvas)
pyautogui.dragTo(lowerRightCanvas, button='left')

centerCanvas = [upperLeftCanvas[0] + (lowerRightCanvas[0] - upperLeftCanvas[0])/2, upperLeftCanvas[1] + (lowerRightCanvas[1] - upperLeftCanvas[1])/2]
pyautogui.moveTo(centerCanvas)
pyautogui.click(centerCanvas, button='right')
pyautogui.typewrite(['down', 'enter', 'tab', 'tab', '0', '.', '0', '1', '3', 'tab', 'enter'], interval=type_interval)

# Calculation Condition -> Setting
pyautogui.typewrite(['alt', 'c', 's'], interval=type_interval)
time.sleep(0.5)

# Solver Type
#pyautogui.typewrite(['tab', 'tab', 'down', 'tab', 'tab'], interval=type_interval)
pyautogui.typewrite(['tab', 'tab', 'tab', 'tab', 'tab', 'down', 'tab', 'tab'], interval=type_interval)
time.sleep(0.5)
pyautogui.screenshot("solverType-{}x{}.png".format(screenWidth, screenHeight))

# Boundary Condition
pyautogui.typewrite(['down', 'tab', 'tab', 'tab', 'tab', 'down', 'tab', 'tab', 'tab', 'tab'], interval=type_interval)
time.sleep(0.5)
pyautogui.screenshot("boundaryCondition-{}x{}.png".format(screenWidth, screenHeight))

# Time series
pyautogui.typewrite(['space'], interval=type_interval)
time.sleep(0.5)
##pyautogui.typewrite(['tab', 'space', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'right', '0', '.', '0', '0', '4', 'enter', 'enter'], interval=type_interval)
#pyautogui.typewrite(['tab', 'space', 'space', 'tab', 'tab', 'tab', 'tab', 'tab', 'tab', 'right', '0', '.', '0', '0', '4', 'enter', 'tab', 'tab', '1', '8', '0', '0', 'enter', 'right', '0', '.', '0', '0', '4', 'enter', 'enter'], interval=type_interval)
pyautogui.typewrite(['tab'] + 2*['space'] + 6*['tab'] + ['right'] + list('0.004') + ['enter'] + 2*['tab'] + list('1800') + ['enter', 'right'] + list('0.004') + 2*['enter'], interval=type_interval)
###pyautogui.typewrite(['tab'] + 2*['space'] + 6*['tab'] + ['right'] + list('0.004') + ['enter'] + 2*['tab'] + list('120') + ['enter', 'right'] + list('0.004') + 2*['enter'], interval=type_interval)
pyautogui.screenshot("timeSeries-{}x{}.png".format(screenWidth, screenHeight))

# Time
pyautogui.typewrite(['tab', 'down'] + 4*['tab'] + list('60') + ['tab'] + list('0.01') + ['tab', '0'] + 4*['tab'], interval=type_interval)
pyautogui.screenshot("time-{}x{}.png".format(screenWidth, screenHeight))

# Bed material
pyautogui.typewrite(2*['down'] + 5*['tab'], interval=type_interval)
pyautogui.screenshot("bedMaterial-{}x{}.png".format(screenWidth, screenHeight))

# Save and Close
pyautogui.typewrite(2*['tab'] + ['space'], interval=type_interval)
pyautogui.screenshot("saveAndClose-{}x{}.png".format(screenWidth, screenHeight))

# [Simulation] -> [Run]
time.sleep(0.5)
pyautogui.typewrite(['alt', 's', 'r'], interval=type_interval)
#pyautogui.screenshot("simulationRun-{}x{}.png".format(screenWidth, screenHeight))

# save
time.sleep(0.5)
pyautogui.typewrite(['y', 'enter'], interval=type_interval)
#pyautogui.screenshot("simulationRun-{}x{}.png".format(screenWidth, screenHeight))

# remove existing file
if os.path.isfile(os.getcwd() + '\\english.ipro'):
    os.remove(os.getcwd() + '\\english.ipro')

# Select How to Save Project
time.sleep(0.5)
pyautogui.typewrite(['enter'], interval=type_interval)
time.sleep(0.5)
pyautogui.screenshot("saveAsFile-{}x{}.png".format(screenWidth, screenHeight))
pyautogui.typewrite(list(os.getcwd() + '\\english.ipro') + ['enter'], interval=type_interval)


# wait until finished
solverFinished = pyautogui.locateOnScreen('../../solverFinished-2012.png')
##time.sleep(60.0)
while solverFinished is None:
    # note locateCenterOnScreen takes alot of time so sleep isn't needed
    solverFinished = pyautogui.locateOnScreen('../../solverFinished-2012.png')
    pyautogui.screenshot("solverFinished-{}x{}.png".format(screenWidth, screenHeight))
pyautogui.screenshot("solverFinished-{}x{}.png".format(screenWidth, screenHeight))
okButton = (solverFinished[0]+196, solverFinished[1]+100)
pyautogui.moveTo(okButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(okButton)


# 5.  Visualize the results
# open 2d post processor
pyautogui.typewrite(['alt', 'r', 'enter'], interval=type_interval)
time.sleep(0.5)
pyautogui.screenshot("2DPost-{}x{}.png".format(screenWidth, screenHeight))


# select ElevationChange (m) in Object Browser and check
elevationChange = pyautogui.locateCenterOnScreen('ElevationChange-2012.png')
if elevationChange is None:
    print("Didn't locate ElevationChange-2012.png")
    pyautogui.hotkey('win', 'm')
    sys.exit(0)
pyautogui.moveTo(elevationChange)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(elevationChange)
time.sleep(0.5)
pyautogui.typewrite(['space'], interval=type_interval)
pyautogui.screenshot("elevationChange-{}x{}.png".format(screenWidth, screenHeight))

# display Scalar Setting dialog
pyautogui.moveTo(elevationChange)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(elevationChange, button='right')
pyautogui.typewrite(2*['down'] + ['enter'], interval=type_interval)
time.sleep(0.5)
pyautogui.screenshot("scalarSetting-{}x{}.png".format(screenWidth, screenHeight))

# make changes to (max, min, Display Setting, Transparent)
pyautogui.typewrite(['right', 'tab', 'space'] + 3*['tab'] + ['space', 'tab'] + list('0.02') + 2*['tab'] + list('-0.04') + 4*['tab'] + ['enter'], interval=type_interval)

# TODO move color bar

# TODO select Arrow -> Velocity

#  [Calculation Result] -> [Open new graphic window]
# X Axis -> J
# Two-dimensional Data -> Elevation and WaterSurfaceElevation
pyautogui.typewrite(['alt', 'r'] + 3*['down'] + ['enter'], interval=type_interval)
time.sleep(0.5)
pyautogui.typewrite(2*['down'] + 3*['tab'], interval=type_interval)
time.sleep(0.5)
##pyautogui.typewrite(2*['down'], interval=type_interval)

# have to use mouse to select data
# DSElevation-2012.png
# DSWaterSurfaceElevation-2012.png
dsElevation = pyautogui.locateCenterOnScreen('DSElevation-2012.png')
if dsElevation is None:
    print("Didn't locate DSElevation-2012.png")
    pyautogui.hotkey('win', 'm')
    sys.exit(0)
pyautogui.moveTo(dsElevation)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(dsElevation)
time.sleep(0.5)
pyautogui.typewrite(['tab', 'space', 'space'], interval=type_interval)
pyautogui.screenshot("DataSourceSetting-{}x{}.png".format(screenWidth, screenHeight))
pyautogui.typewrite(2*['tab'] + ['space'], interval=type_interval)
time.sleep(0.5)
pyautogui.screenshot("graphWindow-{}x{}.png".format(screenWidth, screenHeight))

# open Draw Setting Dialog
# (Note 'Draw &Setting' conflicts with '&Similation')
graphDrawSetting = pyautogui.locateCenterOnScreen('graphDrawSetting-2012.png')
if graphDrawSetting is None:
    print("Didn't locate graphDrawSetting-2012.png")
    pyautogui.hotkey('win', 'm')
    sys.exit(0)
pyautogui.moveTo(graphDrawSetting)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(graphDrawSetting)
time.sleep(0.5)
pyautogui.screenshot("DrawSetting-{}x{}.png".format(screenWidth, screenHeight))
pyautogui.typewrite(4*['tab'] + list('3') + 5*['tab'] + ['down'] + 3*['tab'] + list('3'), interval=type_interval)

# color button
dsColorButton = pyautogui.locateCenterOnScreen('dsColorButton-2012.png')
if dsColorButton is None:
    print("Didn't locate dsColorButton-2012.png")
    pyautogui.hotkey('win', 'm')
    sys.exit(0)
pyautogui.moveTo(dsColorButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(dsColorButton)
time.sleep(0.5)
pyautogui.screenshot("colorDialog-{}x{}.png".format(screenWidth, screenHeight))

# click on blue button
ccBlueButton = pyautogui.locateCenterOnScreen('ccBlueButton-2012.png')
if ccBlueButton is None:
    print("Didn't locate ccBlueButton-2012.png")
    pyautogui.hotkey('win', 'm')
    sys.exit(0)
pyautogui.moveTo(ccBlueButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(ccBlueButton)
time.sleep(0.5)
pyautogui.screenshot("selectBlue-{}x{}.png".format(screenWidth, screenHeight))
pyautogui.typewrite(11*['tab'] + ['space'], interval=type_interval)
time.sleep(0.5)
pyautogui.screenshot("drawSettingBlue-{}x{}.png".format(screenWidth, screenHeight))
pyautogui.typewrite(2*['tab'] + ['space'], interval=type_interval)
time.sleep(0.5)
pyautogui.screenshot("graphWindow-{}x{}.png".format(screenWidth, screenHeight))

# minimize everything
pyautogui.hotkey('win', 'm')

