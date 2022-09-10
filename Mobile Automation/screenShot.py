
#importing the required packages and modules
from appium import webdriver
from selenium.webdriver.common.by import By
import os
from appium.common.logger import logger

#defining desired Capabilites
desired_capabilities = {}
desired_capabilities['deviceName'] = 'emulator-5554'
desired_capabilities['platformName'] = 'Android'
desired_capabilities['appPackage'] ='com.google.android.apps.messaging'
desired_capabilities['appActivity'] ='com.google.android.apps.messaging.ui.ConversationListActivity'

#establising connection with appium desktop server
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
driver.find_element(By.ID,'com.google.android.apps.messaging:id/start_new_conversation_button').click()

#filename of screenshot
file_name = 'screenshot.png'

#taking screenshot
driver.save_screenshot("D:/freelance/pytest/Mobile Automation/Screenshots/" + file_name)