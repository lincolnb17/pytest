import time
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
import sys
import os
# # #this will start  appium server automatically
# os.system("start /B start cmd.exe @cmd /k appium")
#sending information
phone_no ='9821322643'
text='Hello'
file_name = 'screenshot.png'


def testsendsms():
    # device and app details
    deviceId = "4c59e4b60406"
    path = "D:\\freelance\\pytest\\Mobile Automation\\apk\\verizon.apk"  ##path of the apk file
    appPackage = "com.verizon.messaging.vzmsgs"
    appActivity = "com.verizon.mms.ui.ComposeMessageActivity"

    desired_capabilities = {
        "deviceName": deviceId,  # emulator id
        "platformName": "Android",
        "automationName": "uiautomator2",
        "app": path,
        "appPackage": appPackage,
        "appActivity": appActivity,
        "autoGrantPermissions": "true",
        "skipDeviceInitialization": "true"
    }
     # conneting with appium server
    driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_capabilities)

    driver.find_element(By.ID, 'com.verizon.messaging.vzmsgs:id/start').click()
    time.sleep(3)
    TouchAction(driver).tap(x=1198, y=1473).perform()
    time.sleep(3)
    TouchAction(driver).tap(x=1068, y=1908).perform()
    time.sleep(1)
    driver.find_element(By.ID, 'com.verizon.messaging.vzmsgs:id/profile_mdn_custom_view').send_keys(9867916462) ##own mobile number
    time.sleep(1)
    driver.find_element(By.ID, 'com.verizon.messaging.vzmsgs:id/nextTextView').click()














