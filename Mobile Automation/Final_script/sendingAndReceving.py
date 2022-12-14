#
# Setup
# 1. install appium package via terminal or command prompt  t.ie npm install -g appium
# 2.Set environment path variable of appium package run to commands  i.e path=C:\Users\bhatt\AppData\Roaming\npm\node_modules\appium\build\lib\main.js
#

import time
from appium import webdriver
from selenium.webdriver.common.by import By
import os
from appium.webdriver.common.touch_action import TouchAction
#sending information
phone_no ='9821322643'
text='Good Morning'

#staring appium server at PORT=4723
os.system("start /B start cmd.exe @cmd /k appium")

#desired_capabilities of the app
path = "D:\\freelance\\pytest\\Mobile Automation\\apk\\verizon.apk"  ##path of the apk file
appPackage = "com.verizon.messaging.vzmsgs"
appActivity = "com.verizon.mms.ui.ComposeMessageActivity"
def testsendsms():
    # device and app details
    deviceId = "4c59e4b60406"

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
    try:
        driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_capabilities)
    except:
        print("Appium Server is not running at PORT= 4723")

    driver.find_element(By.ID, 'com.verizon.messaging.vzmsgs:id/start').click()
    time.sleep(3)
    TouchAction(driver).tap(x=1198, y=1473).perform()
    time.sleep(3)
    TouchAction(driver).tap(x=1068, y=1908).perform()
    time.sleep(3)
    driver.find_element(By.ID, 'com.verizon.messaging.vzmsgs:id/skip_provisioning_tv').click()
    time.sleep(1)
    driver.find_element(By.ID, 'com.verizon.messaging.vzmsgs:id/composeFab').click()
    time.sleep(1)
    driver.find_element(By.ID, 'com.verizon.messaging.vzmsgs:id/curRecip').send_keys(phone_no)
    time.sleep(1)
    driver.find_element(By.ID, 'com.verizon.messaging.vzmsgs:id/compose_embedded_text_editor').send_keys(text)
    time.sleep(1)
    driver.find_element(By.ID, 'com.verizon.messaging.vzmsgs:id/composebtnSend').click()
    time.sleep(2)
    driver.find_element(By.ID, 'com.verizon.messaging.vzmsgs:id/okayTv').click()



#staring appium server at PORT=4724
os.system("start /B start cmd.exe @cmd /k appium -a 0.0.0.0 -p 4724")
#validating sms at receiver side
def testreceivesms():
    #device and app details
    deviceId2="1B11293210NA103R"

    desired_capabilities = {
        "deviceName": deviceId2, #emulator id
        "platformName": "Android",
        "automationName": "uiautomator2",
        "app": path,
        "appPackage": appPackage,
        "appActivity": appActivity,
        "autoGrantPermissions": "true",
        "skipDeviceInitialization":"true"
    }

    # conneting with appium server
    try:
        driver = webdriver.Remote("http://localhost:4724/wd/hub",desired_capabilities)
    except:
        print("Appium Server is not running at PORT=4724")

    driver.find_element(By.ID, 'com.verizon.messaging.vzmsgs:id/start').click()
    time.sleep(1)
    driver.find_element(By.ID, 'com.verizon.messaging.vzmsgs:id/skip_provisioning_tv').click()
    time.sleep(1)
    sender=driver.find_element(By.ID,'com.verizon.messaging.vzmsgs:id/from')
    time.sleep(1)
    sms=driver.find_element(By.ID,'com.verizon.messaging.vzmsgs:id/subject')
    time.sleep(1)
    if sender.text== '(982) 132-2643' and sms.text == text:
        print("SMS sucessfully received")
    else:

        print("SMS not received")
        assert 1==-1


