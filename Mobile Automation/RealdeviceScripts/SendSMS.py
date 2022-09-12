#importing modules and packages
from appium import webdriver
from selenium.webdriver.common.by import By
#list of desired capabilities
desired_capabilities = {
    "deviceName": "1B11293210NA103R",
    "platformName": "Android",
    "automationName": "uiautomator2",
    "appPackage": "com.android_coding.sendmessage",
    "appActivity": "com.android_coding.sendmessage.MainActivity",
    "autoGrantPermissions":  "true"
}
#conneting with appium server
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

#findind elements and automating
driver.find_element(By.ID,'com.android_coding.sendmessage:id/et_phone').send_keys('9840449049')
driver.find_element(By.ID,'com.android_coding.sendmessage:id/et_message').send_keys('Good Morning')
driver.find_element(By.ID,'com.android_coding.sendmessage:id/bt_send').click()




#exit

