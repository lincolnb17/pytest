from appium import webdriver
 
desired_cap ={
  "deviceName": "emulator-5554",
  "platformName": "Android",
  "app": "D:\\freelance\\pytest\\Mobile Automation\\apk\\com.android.messaging_1.0.001-10001140_minAPI30(nodpi)_apkmirror.com.apk",
  "automationName": "UiAutomator2",
}

driver= webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)
# driver.find_element_by_id("com.android.mms:id/recipients_editor").sendKeys("3453535");




 