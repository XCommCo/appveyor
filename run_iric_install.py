# run_iric_install.py

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

# place mouse on screen to start iRIC (if multiple screens)
pyautogui.moveTo(1, 1)

# verify resolution
screenWidth, screenHeight = pyautogui.size()
print("Screen resolution: {}x{}".format(screenWidth, screenHeight))

# start iRIC install
subprocess.Popen("iRIC_Offline_Installer_No_Runtime_prod.exe")
time.sleep(10.0)
pyautogui.screenshot("iRIC-Setup-{}x{}.png".format(screenWidth, screenHeight))

# click next
nextButton = pyautogui.locateCenterOnScreen('iRIC_Offline_Installer_prod-1024x768-NextButton-2012.png')
if nextButton is None:
    print("Didn't locate iRIC_Offline_Installer_prod-1024x768-NextButton-2012.png")
    sys.exit(0)

pyautogui.moveTo(nextButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(nextButton)
time.sleep(1.0)
pyautogui.screenshot("iRIC-InstallationFolder-{}x{}.png".format(screenWidth, screenHeight))

# copy installer location
pyautogui.hotkey('ctrl', 'a')
time.sleep(0.5)
pyautogui.hotkey('ctrl', 'c')
r = tk.Tk()
# keep the window from showing
r.withdraw()
# text from clipboard
install_location = r.clipboard_get()
print("Installation Folder:", install_location)

# click next
pyautogui.moveTo(nextButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(nextButton)
time.sleep(1.0)
pyautogui.screenshot("iRIC-SelectComponents-{}x{}.png".format(screenWidth, screenHeight))

# click next
pyautogui.moveTo(nextButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(nextButton)
time.sleep(1.0)
pyautogui.screenshot("iRIC-LicenseAgreement-{}x{}.png".format(screenWidth, screenHeight))

# click agree
acceptRadio = pyautogui.locateCenterOnScreen('iRIC_Offline_Installer_prod-1024x768-AcceptRadio-2012.png')
if acceptRadio is None:
    print("Didn't locate iRIC_Offline_Installer_prod-1024x768-AcceptRadio-2012.png")
    sys.exit(0)
pyautogui.moveTo(acceptRadio)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(acceptRadio)
time.sleep(1.0)
pyautogui.screenshot("iRIC-LicenseAgreementAccept-{}x{}.png".format(screenWidth, screenHeight))

# click next
pyautogui.moveTo(nextButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(nextButton)
time.sleep(1.0)
pyautogui.screenshot("iRIC-StartMenushortcuts-{}x{}.png".format(screenWidth, screenHeight))

# click next
pyautogui.moveTo(nextButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(nextButton)
time.sleep(1.0)
pyautogui.screenshot("iRIC-ReadytoInstall-{}x{}.png".format(screenWidth, screenHeight))

# click Install
pyautogui.moveTo(nextButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(nextButton)
time.sleep(3.0)
pyautogui.screenshot("iRIC-Finished-{}x{}.png".format(screenWidth, screenHeight))

# click Finish
finishButton = pyautogui.locateCenterOnScreen('iRIC_Offline_Installer_prod-1024x768-FinishButton-2012.png')
pyautogui.moveTo(finishButton)  # this might not be necessary (needs further testing - at least for iric installers)
pyautogui.click(finishButton)
time.sleep(3.0)
pyautogui.screenshot("Done-{}x{}.png".format(screenWidth, screenHeight))
