from appium import webdriver
 
desired_cap ={
  "deviceName": "emulator-5554",
  "platformName": "Android",
  "app": "D:\\freelance\\pytest- runs in emulator 5.1\\Mobile Automation\\apk\\apkinfo.apk",  #location of apk file to be installed
  "automationName": "UiAutomator2",
}
driver= webdriver.Remote("http://localhost:4723/wd/hub",desired_cap)


#exit




 