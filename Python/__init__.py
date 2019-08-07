import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.driver import ChromeDriver
from selenium.webdriver.chrome.webdriver import WebDriver


class TestSearchText(unittest.TestCase):


#-----------------------VARIABLES-----------------------

 eleSearch="Shoes"
 eleTFSearchXpath="//*[@id='gh-ac']"
 eleBTNSearchXpath="//*[@id='gh-btn']"

#-----------------------VARIABLES-----------------------

def setUp(self):
        # create a new Firefox session
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://www.ebay.com/")




def tearDown(self):
        # close the browser window
        self.driver.quit()
        
        