# from selenium import webdriver
# from home import Driver
import time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from unittest import TestLoader, TestSuite, TextTestRunner, TestCase
from home_page import homePage
import testtools as testtools
# import HtmlTestRunner

class petStore_homePage(unittest.TestCase):
    
    @classmethod
    def setUpClass(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
    def test_001_search(self) -> None:
        driver = self.driver
        home_class = homePage(driver)
        home_class.search_homePage_imput()
        # time.sleep(2)
        
    @classmethod   
    def tearDownClass(self) -> None:
        # time.sleep(2)
        self.driver.close()
        
class petStore_category(unittest.TestCase):
    
    @classmethod
    def setUpClass(self) -> None:
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        
    def test_002_dog_category(self) -> None:
        driver = self.driver
        home_class = homePage(driver)
        home_class.dog_category()
        
    def test_003_reptile_category(self) -> None:
        driver = self.driver
        home_class = homePage(driver)
        home_class.reptile_category()
        # time.sleep(2)
        
    @classmethod   
    def tearDownClass(self) -> None:
        # time.sleep(2)
        self.driver.close()


if __name__ == "__main__":
    
    test_loader = TestLoader()
    # Test Suite is used since there are multiple test cases
    test_suite = TestSuite((
        test_loader.loadTestsFromTestCase(petStore_homePage),
        test_loader.loadTestsFromTestCase(petStore_category),
        ))
 
    test_runner = TextTestRunner(verbosity=2)
    test_runner.run(test_suite)
    
     # Refer https://testtools.readthedocs.io/en/latest/api.html for more information
    # parallel_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in test_suite))
    # parallel_suite.run(testtools.StreamResult())
    
    # unittest.main()