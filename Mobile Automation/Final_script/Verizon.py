import time
from appium import webdriver
from selenium.webdriver.common.by import By
import os

#this will start  appium server automatically
os.system("start /B start cmd.exe @cmd /k appium")
#sending information
phone_no ='9821322643'
text='Good Morning'
file_name = 'screenshot.png'

def testsendsms():
    #device and app details
    deviceId="1B11293210NA103R"
    path = "D:\\freelance\\pytest\\Mobile Automation\\apk\\verizon.apk"  ##path of the apk file
    appPackage="com.verizon.messaging.vzmsgs"
    appActivity="com.verizon.mms.ui.ComposeMessageActivity"


    desired_capabilities = {
        "deviceName": deviceId, #emulator id
        "platformName": "Android",
        "automationName": "uiautomator2",
        "app": path,
        "appPackage": appPackage,
        "appActivity": appActivity,
        "autoGrantPermissions": "true",
        "skipDeviceInitialization":"true"
    }

    # conneting with appium server

    driver = webdriver.Remote("http://localhost:4723/wd/hub",desired_capabilities)
    driver.find_element(By.ID, 'com.verizon.messaging.vzmsgs:id/start').click()
    time.sleep(1)
    driver.find_element(By.ID, 'com.verizon.messaging.vzmsgs:id/skip_provisioning_tv').click()
    time.sleep(1)
    driver.find_element(By.ID, 'com.verizon.messaging.vzmsgs:id/composeFab').click()
    time.sleep(1)
    driver.find_element(By.ID, 'com.verizon.messaging.vzmsgs:id/curRecip').send_keys(phone_no)
    time.sleep(1)
    driver.find_element(By.ID, 'com.verizon.messaging.vzmsgs:id/compose_embedded_text_editor').send_keys(text)
    time.sleep(1)
    driver.find_element(By.ID, 'com.verizon.messaging.vzmsgs:id/composebtnSend').click()











