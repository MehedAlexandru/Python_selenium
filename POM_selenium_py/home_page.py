from locators import Locators
from selenium.webdriver.common.by import By
import time
               
class homePage():
    
    def __init__(self, driver) -> None:
        self.driver = driver
        driver.get("https://petstore.octoperf.com/actions/Catalog.action")
        # self.search_box_xpath = Locators.search_box_xpath
        # self.search_button_xpath = Locators.search_button_xpath
        # self.dog_category_link_xpath = Locators.dog_category_link_xpath
        
    
    def search_homePage_imput(self) -> None:
        self.search_box = self.driver.find_element(By.XPATH, Locators.search_box_xpath)
        self.search_button = self.driver.find_element(By.XPATH, Locators.search_button_xpath)
        self.search_box.send_keys('dog')
        self.search_button.click()
        # time.sleep(2)
        
    def dog_category(self) -> None:
        self.dog_link = self.driver.find_element(By.XPATH, Locators.dog_category_link_xpath)
        self.dog_link.click()
        # time.sleep(2)
        
    def reptile_category(self) -> None:
        self.reptile_link = self.driver.find_element(By.XPATH, Locators.reptile_category_xpath)
        self.reptile_link.click()
        # time.sleep(2)
        
        
        
        
        
        
        