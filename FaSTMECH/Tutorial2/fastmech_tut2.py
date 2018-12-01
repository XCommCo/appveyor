# fastmech_tut2.py

import pyautogui, sys, time
import subprocess
import os
import tkinter as tk
import winreg

def capture_and_push_artifact(path):
    pyautogui.screenshot(path)
    if os.environ.get('APPVEYOR') is not None:
        subprocess.call("appveyor PushArtifact " + path + " -DeploymentName fastmech_tut2")
    return

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
capture_and_push_artifact("Desktop-{}x{}.png".format(screenWidth, screenHeight))

# start iRIC (Don't include the shortcut overlay for additional compatibility)
# see iricIcon-2012.diff.png
# User left double click on "iRIC (list item)" in "Program Manager"
iricIcon = pyautogui.locateCenterOnScreen('../../iricIcon-no-shortcut-2012.png')
if iricIcon is None:
    print("Didn't locate iricIcon-no-shortcut-2012.png")
    sys.exit(0)
pyautogui.doubleClick(iricIcon)
time.sleep(5.0)
capture_and_push_artifact("StartIRIC-{}x{}.png".format(screenWidth, screenHeight))

# cancel maintenance if visible
# User left click on "Cancel (button)" in "Check for Update"
maintainanceButtons = pyautogui.locateOnScreen('../../maintainanceButtons-2012.png')
if maintainanceButtons is None:
    print("Didn't locate maintainanceButtons-2012.png")
else:
    pyautogui.moveTo(maintainanceButtons[LEFT] + 189, maintainanceButtons[TOP] + maintainanceButtons[HEIGHT]/2)  # this might not be necessary (needs further testing - at least for iric installers)
    pyautogui.click(maintainanceButtons[LEFT] + 189, maintainanceButtons[TOP] + maintainanceButtons[HEIGHT]/2)
time.sleep(1.0)
capture_and_push_artifact("AfterMaintainance-{}x{}.png".format(screenWidth, screenHeight))

# close Start Page
# User left click on "Close Enter (button)" in "iRIC Start Page"
closeButton = pyautogui.locateCenterOnScreen('../../closeButton-2012.png')
if closeButton is None:
    print("Didn't locate closeButton-2012.png")
    sys.exit(0)
pyautogui.moveTo(closeButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(closeButton)
time.sleep(1.0)
capture_and_push_artifact("AfterStartPage-{}x{}.png".format(screenWidth, screenHeight))

# maximize main window
maximizeButton = pyautogui.locateCenterOnScreen('../../maximizeButton-2012.png')
if maximizeButton is None:
    print("Didn't locate maximizeButton-2012.png")
    sys.exit(0)
pyautogui.moveTo(maximizeButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(maximizeButton)
time.sleep(1.0)
capture_and_push_artifact("Maximized-{}x{}.png".format(screenWidth, screenHeight))

# start new project
pyautogui.hotkey('ctrl', 'n')

# doubleClick on "FaSTMECH (list item)" in "Select Solver"
newFaSTMECH = pyautogui.locateCenterOnScreen('newFaSTMECH-2012.png')
if newFaSTMECH is None:
    print("Didn't locate newFaSTMECH-2012.png")
    sys.exit(0)
pyautogui.moveTo(newFaSTMECH)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.doubleClick(newFaSTMECH)
time.sleep(1.0)
capture_and_push_artifact("newFaSTMECH-{}x{}.png".format(screenWidth, screenHeight))

# maximize preprocessor window
# User left click on "Pre-processing Window (window)" in "Untitled - iRIC 3.0.7.6238 [FaSTMECH]"
preProcessingMaximize = pyautogui.locateCenterOnScreen('preProcessingMaximize-2012.png')
if preProcessingMaximize is None:
    print("Didn't locate preProcessingMaximize-2012.png")
    sys.exit(0)
pyautogui.moveTo(preProcessingMaximize)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(preProcessingMaximize)
time.sleep(1.0)
capture_and_push_artifact("preProcessingMaximize-{}x{}.png".format(screenWidth, screenHeight))

# Import r5finpt2m114_shifted.tpo
pyautogui.typewrite(['alt', 'i', 'e', 'enter'], interval=type_interval)
time.sleep(1.0)
pyautogui.typewrite(os.getcwd()+'\\GR_Topo_Shifted.tpo\n', interval=type_interval)
time.sleep(2.5)
pyautogui.typewrite(['tab', 'enter'], interval=type_interval)
# wait until import is finished
##time.sleep(24.0)
importFinished = pyautogui.locateOnScreen('importFinished-2012.png')
while importFinished is None:
    # note locateCenterOnScreen takes alot of time so sleep isn't needed
    importFinished = pyautogui.locateOnScreen('importFinished-2012.png')
    capture_and_push_artifact("importFinished-{}x{}.png".format(screenWidth, screenHeight))
capture_and_push_artifact("importElevation-{}x{}.png".format(screenWidth, screenHeight))

# The Pre-processing Window now displays the topography data in the canvas and new data appears in the Object Browser
# under Geographic Data | Elevations | Points1 (Figure 2). In the Object Browser the topography can be made visible or
# not visible by checking or unchecking the box next to Elevation. Add a scalarbar from the Menu Bar by selecting
# Geographic Data -> Set Up Scalarbar. Make sure Elevation is displayed in the drop-down menu and check the “Visible”
# box. Select OK (Figure 2).

# uncheck points
selectedChecked = pyautogui.locateCenterOnScreen('selectedChecked-2012.png')
if selectedChecked is None:
    print("Didn't locate selectedChecked-2012.png")
    sys.exit(0)
pyautogui.moveTo(selectedChecked)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(selectedChecked)
time.sleep(1.0)
capture_and_push_artifact("selectedUnChecked-{}x{}.png".format(screenWidth, screenHeight))

# re-check points
selectedUnchecked = pyautogui.locateCenterOnScreen('selectedUnchecked-2012.png')
if selectedUnchecked is None:
    print("Didn't locate selectedUnchecked-2012.png")
    sys.exit(0)
pyautogui.moveTo(selectedUnchecked)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(selectedUnchecked)
time.sleep(1.0)
capture_and_push_artifact("selectedChecked-{}x{}.png".format(screenWidth, screenHeight))

# Setup Scalarbar
pyautogui.typewrite(['alt', 'e'] + 6*['down'] + 2*['enter'], interval=type_interval)

# To adjust how the elevation points are displayed, highlight Elevation | Points1 in the Object Browser and
# right-click. This will bring up a dialog that allows you to rename the data in the Object Browser, Export the
# data, Delete the data, and adjust properties. Select “Property” and change the point size to 2 (Figure 3).
# Select OK when done. 

# right-click Points->Property... and change points to 2
pointsItem = pyautogui.locateCenterOnScreen('pointsItem-2012.png')
if pointsItem is None:
    print("Didn't locate pointsItem-2012.png")
    sys.exit(0)
pyautogui.moveTo(pointsItem)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.rightClick(pointsItem)
time.sleep(0.1)
pyautogui.typewrite(6*['down'] + ['enter'], interval=type_interval)
time.sleep(1.0)
pyautogui.typewrite(['tab', '2', 'tab', 'tab', 'enter'], interval=type_interval)
capture_and_push_artifact("pointsItemTwo-{}x{}.png".format(screenWidth, screenHeight))
##sys.exit(1)

# Save (for example, named Tutorial 2) by selecting File -> Save as File (*.ipro) from the Menu Bar.

# remove existing file
if os.path.isfile(os.getcwd() + '\\Tutorial2.ipro'):
    os.remove(os.getcwd() + '\\Tutorial2.ipro')
pyautogui.typewrite(['alt', 'f', 'a'], interval=type_interval)
time.sleep(0.3)
pyautogui.typewrite(os.getcwd()+'\\Tutorial2.ipro\n', interval=type_interval)
time.sleep(10.0)
capture_and_push_artifact("fileSaveAsFile-{}x{}.png".format(screenWidth, screenHeight))


# Import an image to place in the background of the data. Background images can be imported through the
# Menu Bar by selecting Import -> Background Image. In the Open Image dialog select the Green River.jpg
# file. The image will be displayed in the canvas (Figure 4). To turn the image off, uncheck Background
# Images in the Object Browser. 
pyautogui.typewrite(['alt', 'i', 'b'], interval=type_interval)
time.sleep(0.3)
pyautogui.typewrite(os.getcwd()+'\\GreenRiver.jpg\n', interval=type_interval)
time.sleep(3.0)
capture_and_push_artifact("importBackgroundImage-{}x{}.png".format(screenWidth, screenHeight))


# To verify the modeled water-surface elevation, you need to first import measured water-surface elevation
# data. Select Import -> Measured Values from the Menu Bar.  Select the file “GR_wse.csv" in the File
# Open dialog. The data is added to the Pre-processing window Object Browser under Measured Values.
pyautogui.typewrite(['alt', 'i', 'm'], interval=type_interval)
time.sleep(0.3)
pyautogui.typewrite(os.getcwd()+'\\GR_wse.csv\n', interval=type_interval)
time.sleep(3.0)
capture_and_push_artifact("importWaterSurfaceElevation-{}x{}.png".format(screenWidth, screenHeight))


# You will see that importing the measured data adds a legend by default.  To turn the legend off in the
# Object Browser select and right-click on Measured Values | C:\(path)\wse.csv | Scalar and in the resulting
# pop-up dialog select “Property”.  In the Scalar Setting dialog select the “Color Bar Setting” button, and
# then deselect the “Visible” attribute. Select OK to exit the Color Legend Setting dialog box and select OK
# again to exit the Scalar Setting dialog box. 

# right-click Scalar->Property... and turn-off legend
scalarItem = pyautogui.locateCenterOnScreen('scalarItem-2012.png')
if scalarItem is None:
    print("Didn't locate scalarItem-2012.png")
    sys.exit(0)
pyautogui.moveTo(scalarItem)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.rightClick(scalarItem)
time.sleep(0.1)
pyautogui.typewrite(['down', 'enter'], interval=type_interval)
time.sleep(1.0)
pyautogui.typewrite(6*['tab'] + ['space'], interval=type_interval)
time.sleep(0.1)
pyautogui.typewrite(13*['tab'] + ['space', 'enter'], interval=type_interval)
time.sleep(0.1)
pyautogui.typewrite(3*['tab'] + ['enter'], interval=type_interval)
time.sleep(1.0)
capture_and_push_artifact("turnOffLegend-{}x{}.png".format(screenWidth, screenHeight))


# In the Menu Bar select Grid -> Select Algorithm to Create Grid. This opens a dialog (Figure 5). Select “Create
# grid from polygonal line and width.” Click OK. Another dialog will open providing instructions on using this
# feature. Click OK. 
pyautogui.typewrite(['alt', 'g', 's'], interval=type_interval)
time.sleep(0.3)
pyautogui.typewrite(4*['tab'] + ['space', 'enter'], interval=type_interval)
time.sleep(1.0)
pyautogui.typewrite(['tab', 'space', 'enter'], interval=type_interval)
capture_and_push_artifact("selectGridAlgorithm-{}x{}.png".format(screenWidth, screenHeight))


# To draw the centerline, left-click in the desired locations starting at the upstream most point of interest and
# ending at the downstream (Figure 6). The upstream end of the channel in Figure 6 is at the bottom right and the
# channel centerline should be drawn in the direction from lower-right to upper-left. When finished, press “Enter”
# on the keyboard. Use Figure 6 and the blue water-surface points on the background image as a guide in 
# selecting the boundary locations.

# zoom in 4 times
zoomInButton = pyautogui.locateCenterOnScreen('zoomInButton-2012.png')
if zoomInButton is None:
    print("Didn't locate zoomInButton-2012.png")
    sys.exit(0)
pyautogui.moveTo(zoomInButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(zoomInButton)
pyautogui.click(zoomInButton)
pyautogui.click(zoomInButton)
pyautogui.click(zoomInButton)
capture_and_push_artifact("zoomIn-{}x{}.png".format(screenWidth, screenHeight))

# draw centerline
pyautogui.click(810, 565)
pyautogui.click(808, 599)
pyautogui.click(802, 631)
pyautogui.click(784, 659)
#
pyautogui.click(748, 683)
pyautogui.click(716, 687)
pyautogui.click(670, 668)
pyautogui.click(610, 625)
#
pyautogui.click(483, 516)
pyautogui.click(432, 438)
pyautogui.click(395, 370)
pyautogui.click(368, 285)
#
##pyautogui.click(343, 211) # at the edge
pyautogui.click(349, 229) # perpendicular to the last measured WaterSurfaceElevation 
time.sleep(5.0)
capture_and_push_artifact("drawCenterLineXXX-{}x{}.png".format(screenWidth, screenHeight))
pyautogui.typewrite(['enter'], interval=type_interval)
time.sleep(2.0)
capture_and_push_artifact("drawCenterLine-{}x{}.png".format(screenWidth, screenHeight))
pyautogui.typewrite(2*['tab'] + list('360') + 4*['tab'] + list('310') + ['tab'] + list('36') + 2*['tab'] + ['enter'], interval=type_interval)
time.sleep(0.1)
pyautogui.typewrite(['alt', 'n'], interval=type_interval)
time.sleep(3.0)
capture_and_push_artifact("createGrid-{}x{}.png".format(screenWidth, screenHeight))
time.sleep(3.0)


# A Confirmation message “Do you want to map geographic data to grid attributes now?” follows.  In this case
# we will decline by selecting “No”. We want to modify the location and curvature of the grid which is likely in
# this case to take many iterations. To disable the automatic mapping of geographic information from the Menu
# Bar select Grid -> Attributes Mapping -> Setting and in the resulting Grid Attribute Mapping Setting dialog,
# select “Manual” for the Execute mapping property. Select OK. Your grid should look similar to Figure 8.
pyautogui.typewrite(['alt', 'g', 'a', 's'], interval=type_interval)
time.sleep(0.1)
manualRadio = pyautogui.locateCenterOnScreen('manualRadio-2012.png')
if manualRadio is None:
    print("Didn't locate manualRadio-2012.png")
    sys.exit(0)
pyautogui.moveTo(manualRadio)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(manualRadio)
time.sleep(0.1)
pyautogui.typewrite(2*['tab'] + ['enter'], interval=type_interval)

# match figure 8
pyautogui.click(selectedChecked)
time.sleep(1.0)
capture_and_push_artifact("elevationPointsOff-{}x{}.png".format(screenWidth, screenHeight))

# We need to set the width and length of the template. From the Menu Bar select Grid -> Attributes
# Mapping -> Setting. This opens the Grid Attribute Mapping Setting dialog.  We previously set the Execute
# attribute to “Manual” and the Mapping attribute to “Template mapping”. Select the “Detail” button near the
# bottom of the dialog (Figure 10). 
pyautogui.typewrite(['alt', 'g', 'a', 's'], interval=type_interval)
time.sleep(0.3)
templateRadio = pyautogui.locateCenterOnScreen('templateRadio-2012.png')
if templateRadio is None:
    print("Didn't locate templateRadio-2012.png")
    sys.exit(0)
pyautogui.moveTo(templateRadio)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(templateRadio)
time.sleep(0.1)
pyautogui.typewrite(['tab', 'space'], interval=type_interval)
time.sleep(0.1)
pyautogui.typewrite(2*['tab'] + ['2'] + 3*['tab'] + ['down', 'tab'] + list('50') + ['tab'] + list('5') + 3*['tab'] + ['enter'], interval=type_interval)
time.sleep(0.1)
pyautogui.typewrite(['tab', 'enter'], interval=type_interval)


# To execute the mapping method, select Grid -> Attributes Mapping -> Execute from the Menu Bar. Check
# “Elevation” and select OK. Select OK when notified that mapping is complete. Node attributes will be
# added to the Object Browser under Grid () | Node Attributes. Expand the Node attributes and make sure
# that Elevation is selected.
pyautogui.typewrite(['alt', 'g', 'a', 'e', 'tab', 'space', 'tab', 'enter'], interval=type_interval)
time.sleep(7.0)
pyautogui.typewrite(['tab', 'enter'], interval=type_interval)
time.sleep(0.1)
pyautogui.typewrite(2*['tab'] + ['2'] + 3*['tab'] + ['down', 'tab'] + list('50') + ['tab'] + list('5') + 3*['tab'] + ['enter'], interval=type_interval)
time.sleep(0.1)
# Information dialog
pyautogui.typewrite(['tab', 'enter'], interval=type_interval)
# select Node attributes
time.sleep(0.3)
nodeAttributes = pyautogui.locateCenterOnScreen('nodeAttributes-2012.png')
if nodeAttributes is None:
    print("Didn't locate nodeAttributes-2012.png")
    sys.exit(0)
pyautogui.click(nodeAttributes)
time.sleep(0.1)
pyautogui.typewrite(['space', 'right', 'down', 'space'], interval=type_interval)
capture_and_push_artifact("executeElevation-{}x{}.png".format(screenWidth, screenHeight))


# You will likely need to adjust the Color bar so you can view the results of mapping elevation to the grid.
# From the Object Browser select and right-click on Grid () | Node Attributes | Elevation and in the
# resulting pop-up menu select “Property”. In the Grid Node Attributes Display Setting dialog uncheck the
# box next to automatic. Set the max value to 449 and the min value to 444. Set the Contour setting attribute
# to “Contour Figure”. Select OK. Additionally, in the Object Browser, deselect Geographic Data, Grid
# Creating Condition, and Grid () | Grid Shape. Your results look similar to Figure 12. 

# right-click Node attributes -> Elevation
elevationSelectedChecked = pyautogui.locateCenterOnScreen('elevationSelectedChecked-2012.png')
if elevationSelectedChecked is None:
    print("Didn't locate elevationSelectedChecked-2012.png")
    sys.exit(0)
pyautogui.moveTo(elevationSelectedChecked)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.rightClick(elevationSelectedChecked)
time.sleep(0.1)
pyautogui.typewrite(3*['down'] + ['enter'], interval=type_interval)
time.sleep(0.1)
pyautogui.typewrite(6*['tab'] + ['space'], interval=type_interval)
time.sleep(0.1)
pyautogui.typewrite(['tab'] + list('449') + ['tab'] + list('444') + 2*['tab'] + ['right'] + 4*['tab'] + ['enter'], interval=type_interval)

# deselect Geographic Data -> Grid Creating Condition
gridCreatingConditionItem = pyautogui.locateCenterOnScreen('gridCreatingConditionItem-2012.png')
if gridCreatingConditionItem is None:
    print("Didn't locate gridCreatingConditionItem-2012.png")
    sys.exit(0)
pyautogui.moveTo(gridCreatingConditionItem)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(gridCreatingConditionItem)
time.sleep(0.1)
pyautogui.typewrite(['space'], interval=type_interval)

# deselect Grid() | Grid Shape
gridShapeItem = pyautogui.locateCenterOnScreen('gridShapeItem-2012.png')
if gridShapeItem is None:
    print("Didn't locate gridShapeItem-2012.png")
    sys.exit(0)
pyautogui.moveTo(gridShapeItem)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(gridShapeItem)
time.sleep(0.1)
pyautogui.typewrite(['space'], interval=type_interval)

capture_and_push_artifact("figure12-{}x{}.png".format(screenWidth, screenHeight))


# Save the Project. 
pyautogui.typewrite(['alt', 'f', 's'], interval=type_interval)
##time.sleep(4.0)
saveFinished = pyautogui.locateOnScreen('saveFinished-2012.png')
while saveFinished is None:
    # note locateOnScreen takes alot of time so sleep isn't needed
    saveFinished = pyautogui.locateOnScreen('saveFinished-2012.png')
    capture_and_push_artifact("saveFinished-{}x{}.png".format(screenWidth, screenHeight))
capture_and_push_artifact("saveFinished-{}x{}.png".format(screenWidth, screenHeight))


# Calculation Condition -> Setting
pyautogui.typewrite(['alt', 'c', 's'], interval=type_interval)
time.sleep(0.5)

# Discharge
pyautogui.typewrite(5*['tab'] + list('247') + 4*['tab'], interval=type_interval)
time.sleep(0.5)
capture_and_push_artifact("discharge-{}x{}.png".format(screenWidth, screenHeight))

# Stage
pyautogui.typewrite(['down'] + 5*['tab'] + list('447.1') + ['tab'], interval=type_interval)
time.sleep(0.5)
capture_and_push_artifact("stage-{}x{}.png".format(screenWidth, screenHeight))

# Roughness
pyautogui.typewrite(['down'] + 6*['tab'] + list('0.008') + ['tab'], interval=type_interval)
time.sleep(0.5)
capture_and_push_artifact("roughness-{}x{}.png".format(screenWidth, screenHeight))

# Lateral Eddy Viscosity
pyautogui.typewrite(['down'] + 5*['tab'] + list('0.03') + ['tab'], interval=type_interval)
time.sleep(0.5)
capture_and_push_artifact("lateralEddyViscosity-{}x{}.png".format(screenWidth, screenHeight))

### # Grid Extension (No changes)
### pyautogui.typewrite(['down'], interval=type_interval)
# Grid Extension (Reqd when last point of centerline is (349, 229))
pyautogui.typewrite(['down'] + 5*['tab'] + ['down', 'tab'], interval=type_interval)
time.sleep(0.5)
capture_and_push_artifact("gridExtension-{}x{}.png".format(screenWidth, screenHeight))

# Initial Conditions
pyautogui.typewrite(['down'] + 5*['tab'] + list('449') + ['tab'], interval=type_interval)
time.sleep(0.5)
capture_and_push_artifact("initialConditions-{}x{}.png".format(screenWidth, screenHeight))

# Wetting and Drying (No changes)
pyautogui.typewrite(['down'], interval=type_interval)
time.sleep(0.5)
capture_and_push_artifact("wettingAndDrying-{}x{}.png".format(screenWidth, screenHeight))

# Solution Parameters
pyautogui.typewrite(['down'] + 5*['tab'] + list('1000') + 3*['tab'], interval=type_interval)
time.sleep(0.5)
capture_and_push_artifact("solutionParameters-{}x{}.png".format(screenWidth, screenHeight))

# Solution Relaxation Coefficients (No changes)
pyautogui.typewrite(['down'], interval=type_interval)
time.sleep(0.5)
capture_and_push_artifact("solutionRelaxationCoefficients-{}x{}.png".format(screenWidth, screenHeight))

# 2D Solution Output
pyautogui.typewrite(['down'] + 5*['tab'] + ['down'] + 7*['tab'], interval=type_interval)
time.sleep(0.5)
capture_and_push_artifact("2dSolutionOutput-{}x{}.png".format(screenWidth, screenHeight))

# Save and Close
pyautogui.typewrite(2*['tab'] + ['enter'], interval=type_interval)
time.sleep(0.5)

# Run
pyautogui.typewrite(['alt', 's', 'r'], interval=type_interval)
time.sleep(2.0)
pyautogui.typewrite(['alt', 'y'], interval=type_interval)


# wait until finished
solverFinished = pyautogui.locateOnScreen('../../solverFinished-2012.png')
while solverFinished is None:
    # note locateCenterOnScreen takes alot of time so sleep isn't needed
    solverFinished = pyautogui.locateOnScreen('../../solverFinished-2012.png')
    capture_and_push_artifact("solverFinished-{}x{}.png".format(screenWidth, screenHeight))
capture_and_push_artifact("solverFinished-{}x{}.png".format(screenWidth, screenHeight))
okButton = (solverFinished[0]+196, solverFinished[1]+100)
pyautogui.moveTo(okButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(okButton)


# Place focus on preprocessing window
pyautogui.typewrite(['alt', 'v', '1'], interval=type_interval)

# open 2D Post-processing Window
pyautogui.typewrite(['alt', 'r', 'enter'], interval=type_interval)

# force a redraw (restore and maximize main window)
# restore
pyautogui.keyDown('alt')
pyautogui.press('space')
pyautogui.keyUp('alt')
pyautogui.press('r')
# maximize
pyautogui.keyDown('alt')
pyautogui.press('space')
pyautogui.keyUp('alt')
pyautogui.press('x')

# Save the Project. 
pyautogui.typewrite(['alt', 'f', 's'], interval=type_interval)
time.sleep(4.0)



# select Scalar -> WaterSurfaceElevation
waterSurfaceElevationItem = pyautogui.locateCenterOnScreen('waterSurfaceElevationItem-2012.png')
if waterSurfaceElevationItem is None:
    print("Didn't locate waterSurfaceElevationItem-2012.png")
    sys.exit(0)
pyautogui.moveTo(waterSurfaceElevationItem)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(waterSurfaceElevationItem)
time.sleep(0.1)
pyautogui.typewrite(['space'], interval=type_interval)
capture_and_push_artifact("figure15-{}x{}.png".format(screenWidth, screenHeight))

# set scalar settings
pyautogui.rightClick(waterSurfaceElevationItem)
pyautogui.typewrite(['down', 'down', 'enter'], interval=type_interval)
time.sleep(0.1)
pyautogui.typewrite(6*['tab'] + ['space', 'tab'] + list('449') + 2*['tab'] + list('447') + 5*['tab'] + ['right', 'tab', 'space'] + 10*['tab'], interval=type_interval)
time.sleep(0.1)
capture_and_push_artifact("figure16-{}x{}.png".format(screenWidth, screenHeight))
pyautogui.typewrite(4*['tab'] + ['space'], interval=type_interval)
time.sleep(0.1)
pyautogui.typewrite(['down'], interval=type_interval)
capture_and_push_artifact("figure17a-{}x{}.png".format(screenWidth, screenHeight))
pyautogui.typewrite(['tab'] + ['space'], interval=type_interval)
pyautogui.typewrite(['tab'] + ['space'], interval=type_interval)
capture_and_push_artifact("figure17b-{}x{}.png".format(screenWidth, screenHeight))
pyautogui.typewrite(11*['tab'] + ['enter'], interval=type_interval)
time.sleep(0.1)
pyautogui.typewrite(8*['tab'] + ['enter'], interval=type_interval)


capture_and_push_artifact("final-{}x{}.png".format(screenWidth, screenHeight))
pyautogui.hotkey('win', 'm')
sys.exit(0)
