from selenium import webdriver
import unittest
import time

class SwagLabs(unittest.TestCase):
    
    def setUp(self):
        # select the web driver
        self.chrome = webdriver.Chrome("./chromedriver.exe")

        # authentification data
        self.username = "standard_user"
        self.password = "secret_sauce"

        # extra
        self.chrome.maximize_window()
    
    def login(self):
        # load setup
        chrome = self.chrome

        # load the URL
        url = "https://www.saucedemo.com/"
        chrome.get(url)


        # verify the page avalibility
        self.assertIn("Swag Labs", chrome.title)
        
        # the actual login
        chrome.find_element_by_id("user-name").send_keys(self.username)
        chrome.find_element_by_id("password").send_keys(self.password)
        submit = chrome.find_element_by_id("login-button")
        submit.click()
    

    def test_checkout(self):
        self.login()
        chrome = self.chrome

        # find backpack and add it to chart
        backpak = chrome.find_element_by_xpath('//*[@id="add-to-cart-sauce-labs-backpack"]')
        backpak.click()
        
        # go to chart and follow up to checkout
        chart_index = chrome.find_element_by_xpath('//*[@id="shopping_cart_container"]/a/span')
        if chart_index.text == '1':
            print('One intem added to chart')
        else:
            print('chart failed')
        chart_index.click()
        checkout = chrome.find_element_by_xpath('//*[@id="checkout"]')
        checkout.click()

        # checkout completion form
        chrome.find_element_by_xpath('//*[@id="first-name"]').send_keys('alex')
        chrome.find_element_by_xpath('//*[@id="last-name"]').send_keys('ax')
        chrome.find_element_by_xpath('//*[@id="postal-code"]').send_keys('200435')
        confirm_checkout = chrome.find_element_by_xpath('//*[@id="continue"]')
        confirm_checkout.click()

        # confirm checkout
        chrome.find_element_by_xpath('//*[@id="finish"]').click()
        if 'THANK YOU FOR YOUR ORDER' in chrome.page_source:
            print('Checkout success!!')
        else:
            print('failure')


    def tearDown(self):
        # wait and close chrome after test finished
        # time.sleep(3)
        self.chrome.close()
        print('THANK YOU FOR YOUR ORDER')


if __name__ == "__main__":
    unittest.main()

        