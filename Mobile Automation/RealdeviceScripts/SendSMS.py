#importing modules and packages
from appium import webdriver
from selenium.webdriver.common.by import By
#list of desired capabilities
desired_capabilities = {
    "deviceName": "1B11293210NA103R",
    "platformName": "Android",
    "automationName": "uiautomator2",
    "appPackage": "com.simplemobiletools.smsmessenger",
    "appActivity": "com.simplemobiletools.smsmessenger.activities.NewConversationActivity"
}
#conneting with appium server
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_capabilities)

#findind elements and automating
driver.find_element(By.ID,'com.simplemobiletools.smsmessenger:id/new_conversation_address').send_keys('98404409049')
driver.find_element(By.ID,'com.simplemobiletools.smsmessenger:id/new_conversation_confirm').click()
driver.find_element(By.ID,'com.simplemobiletools.smsmessenger:id/thread_type_message').send_keys('Good Morning')
driver.find_element(By.ID,'com.simplemobiletools.smsmessenger:id/thread_send_message').click()



#exit

