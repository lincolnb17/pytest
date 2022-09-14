
#importing the required packages and modules
from appium import webdriver
from selenium.webdriver.common.by import By
import os
from appium.common.logger import logger

#defining desired Capabilites
desired_capabilities = {}
desired_capabilities['deviceName'] = 'emulator-5554' ## emulator device name
desired_capabilities['platformName'] = 'Android'
desired_capabilities['appPackage'] ='com.android.mms'
desired_capabilities['appActivity'] ='com.android.mms.ui.ComposeMessageActivity'

#establising connection with appium desktop server
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)


#filename of screenshot
file_name = 'screenshot.png'

#taking screenshot
driver.save_screenshot("D:/freelance/finals-scripts-with-error-handling/Mobile Automation/Screenshots/" + file_name)  #path of your local machine