import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
import time
from appium.common.logger import logger

#sending information
phone_no ='1234567890'
text='Good Morning'
file_name = 'screenshot.png'

def testsendsms():

    #device and app details
    deviceId="1B11293210NA103R"
    path = "D:\\freelance\\pytest\\Mobile Automation\\apk\\190_SendMessage.apk"  ##path of the apk file
    appPackage="com.android_coding.sendmessage"
    appActivity="com.android_coding.sendmessage.MainActivity"


    desired_capabilities = {
        "deviceName": deviceId, #emulator id
        "platformName": "Android",
        "automationName": "uiautomator2",
        "app": path,
        "appPackage": appPackage,
        "appActivity": appActivity,
        "autoGrantPermissions": "true"
    }

    # conneting with appium server
    try:
        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
    except:
        print("Please open appium server at PORT=4723")




    #checking if the phone is correct or not
    if len(phone_no) == 10 and type(phone_no == int):
        driver.find_element(By.ID, 'com.android_coding.sendmessage:id/et_phone').send_keys(phone_no)
        driver.find_element(By.ID, 'com.android_coding.sendmessage:id/et_message').send_keys(text)
        driver.find_element(By.ID, 'com.android_coding.sendmessage:id/bt_send').click()
        driver.save_screenshot('D:/freelance/pytest/Mobile Automation/finals-scripts-with-error-handling/Screenshots' + file_name)
    else:
        print("Enter valid phone number")
        assert 1 == 2



    # exit