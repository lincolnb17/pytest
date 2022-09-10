
from appium import webdriver
from selenium.webdriver.common.by import By

import time
desired_capabilities = {
    "deviceName": "emulator-5554",
    "platformName": "Android",
    "automationName": "uiautomator2",
    "appPackage": "com.google.android.apps.messaging",
    "appActivity": "com.google.android.apps.messaging.ui.ConversationListActivity"
    # "appActivity": "com.google.android.apps.messaging.home.HomeActivity"
}
self.driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)


# driver.find_element_by_xpath("//android.widget.ImageView[@content-desc="Start new conversation"]").click()
# driver.find_element_by_id("com.google.android.apps.messaging:id/start_new_conversation_button").click()
# driver.find_element_by_xpath("//android.widget.ImageView[@index='2']").click()
open=self.driver.find_element(By.ID,'com.google.android.apps.messaging:id/start_new_conversation_button')
open.click()
time.sleep(60)


