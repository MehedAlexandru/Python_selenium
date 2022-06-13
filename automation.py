from selenium import webdriver
import time

chrome_browser = webdriver.Chrome("./chromedriver.exe")

chrome_browser.maximize_window()
chrome_browser.get("https://www.seleniumeasy.com/test/basic-first-form-demo.html")

assert "Selenium Easy Demo" in chrome_browser.title
# print(self.assertIn("Selenium Easy Demo", chrome_browser.title))

# time.sleep(2)
chrome_browser.implicitly_wait(2)
close_ad = chrome_browser.find_element_by_id("at-cv-lightbox-close")
close_ad.click()

assert "Show Message" in chrome_browser.page_source
show_message_button = chrome_browser.find_element_by_class_name("btn-default")
print("Button enabled = ", show_message_button.is_enabled())
user_message = chrome_browser.find_element_by_id("user-message")
user_message.clear()
user_message.send_keys("Some user message!!")

show_message_button.click()

display_message = chrome_browser.find_element_by_id("display")

if "Some" in display_message.text:
    print("Test completed Scucessfully")
else:
    print("Task failed")
    chrome_browser.close()

time.sleep(2)

chrome_browser.close()