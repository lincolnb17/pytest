import pytest
def testsendsms():
    # importing modules and packages
    from appium import webdriver
    from selenium.webdriver.common.by import By
    # list of desired capabilities
    desired_capabilities = {
        "deviceName": "emulator-5554", #emulator id
        "platformName": "Android",
        "automationName": "uiautomator2",
        "appPackage": "com.android.mms",
        "appActivity": "com.android.mms.ui.ComposeMessageActivity"
    }
    # conneting with appium server
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

    # findind elements and automating
    driver.find_element(By.ID, 'com.android.mms:id/recipients_editor').send_keys('98404409049')
    driver.find_element(By.ID, 'com.android.mms:id/embedded_text_editor').send_keys('Good Morning')
    driver.find_element(By.ID, 'com.android.mms:id/send_button_sms').click()
    driver.quit()

    # exit