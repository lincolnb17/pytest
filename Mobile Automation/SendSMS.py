
from appium import webdriver
from selenium.webdriver.common.by import By

import time
receiver_number='9840449049'

desired_capabilities = {
    "deviceName": "emulator-5554",
    "platformName": "Android",
    "automationName": "uiautomator2",
    "appPackage": "com.android.mms",
    "appActivity": "com.android.mms.ui.ComposeMessageActivity"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)
driver.find_element(By.ID,'com.android.mms:id/recipients_editor').send_keys('98404409049')
driver.find_element(By.ID,'com.android.mms:id/embedded_text_editor').send_keys('Hello My name is Lincoln Bhattachan')
driver.find_element(By.ID,'com.android.mms:id/send_button_sms').click()
driver.quit()


