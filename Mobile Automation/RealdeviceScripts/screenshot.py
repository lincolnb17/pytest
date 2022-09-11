
#importing the required packages and modules
from appium import webdriver
from selenium.webdriver.common.by import By
import os
import time
from appium.common.logger import logger

#defining desired Capabilites
desired_capabilities = {}
desired_capabilities['deviceName'] = '1B11293210NA103R'
desired_capabilities['platformName'] = 'Android'
desired_capabilities['appPackage'] ='com.google.android.apps.messaging'
desired_capabilities['appActivity'] ='com.google.android.apps.messaging.home.HomeActivity'

desired_capabilities['automationName']='uiautomator2'

#establising connection with appium desktop server
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)




#filename of screenshot
file_name = 'screenshot.png'
time.sleep(5)
#taking screenshot
driver.save_screenshot("D:/freelance/pytest/Mobile Automation/Screenshots/" + file_name)