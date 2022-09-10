import time

from appium.webdriver.webdriver import WebDriver as AppiumDriver
from appium import webdriver
from appium import webdriver
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
import time

desired_cap = {
    "deviceName": "emulator-5554",
    "platformName": "Android",
    "automationName": "uiautomator2",
    "appPackage": "com.google.android.apps.messaging",
    "appActivity": "com.google.android.apps.messaging.ui.ConversationListActivity"
    # "appActivity": "com.google.android.apps.messaging.home.HomeActivity"
}
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
driver.find_element_by_xpath("//android.widget.ImageView[@bounds='[0,210][1080,1794]']").click();



