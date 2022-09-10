
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction

import time
desired_capabilities = {
    "deviceName": "emulator-5554",
    "platformName": "Android",
    "automationName": "uiautomator2",
    "appPackage": "com.google.android.apps.messaging",
    "appActivity": "com.google.android.apps.messaging.ui.ConversationListActivity"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
ts = time.strftime("%Y_%m_%d_%H%M%S")
activityName = driver.current_activity
filename =activityName+ts
driver.save_screenshot("D:/freelance/pytest/Mobile Automation/Screenshots/"+filename+".png")