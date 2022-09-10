from appium import webdriver
import os
from appium.common.logger import logger
desired_capabilities = {}

desired_capabilities['deviceName'] = 'emulator-5554'
desired_capabilities['platformName'] = 'Android'
desired_capabilities['appPackage'] ='com.google.android.apps.messaging'
desired_capabilities['appActivity'] ='com.google.android.apps.messaging.ui.ConversationListActivity'

driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
directory = '%s/' % os.getcwd()
file_name = 'screenshot.png'

driver.save_screenshot("D:/freelance/pytest/Mobile Automation/Screenshots/" + file_name)