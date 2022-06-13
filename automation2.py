import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):

        self.driver = webdriver.Chrome("./chromedriver.exe")

    def test_download_progress_bar(self):
        driver = self.driver
        driver.get("https://www.seleniumeasy.com/test/jquery-download-progress-bar-demo.html")
        driver.maximize_window()
        self.assertIn("JQuery Download Progress bar", driver.title)
        download_button = driver.find_element_by_id("downloadButton")
        print("button is enabele: ", download_button.is_enabled())
        download_button.click()
        wait = WebDriverWait(driver, 10)
        element = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "progress-label")))
        print(element.text)
        n = 0
        while element.text is not "Complete!":
            time.sleep(1)
            print(element.text)
            if element.text == "Complete!":
                break
            n += 1
            print(n)
            if n == 10:
                print("Something went wrong! Download failed!")
                break
        close_dialog = driver.find_element_by_class_name("ui-dialog-buttonset")
        close_dialog.click()
        # progress_display = driver.find_element_by_id("progress-label")
        # print("profress display: ",progress_display.text)
        # print("element: ", element.text)
        # assert "Complete!" in driver.name

        # elem.send_keys("pycon")
        # elem.send_keys(Keys.RETURN)
        # assert "No results found." in driver.page_source
    def test_slider_automation(self): 
        driver = self.driver
        driver.maximize_window()
        driver.get('https://www.seleniumeasy.com/test/drag-drop-range-sliders-demo.html')

        slider = driver.find_element_by_xpath('//div[@id="slider1"]//input')
        ActionChains(driver).drag_and_drop_by_offset(slider, 200, 50).perform()
        time.sleep(3)


    def tearDown(self):
        # time.sleep(3)
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
