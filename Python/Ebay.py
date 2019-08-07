import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.driver import ChromeDriver
from selenium.webdriver.chrome.webdriver import WebDriver
from Python.EbayStep import EbayStepp
from _overlapped import NULL


 
class TestEbay(unittest.TestCase):


 webAddres="https://www.ebay.com"


 def setUp(self):
        # create a new Firefox session
        self.eleDriver = webdriver.Chrome(ChromeDriverManager().install())
        self.eleDriver.implicitly_wait(30)
        self.eleDriver.maximize_window()
        self.eleDriver.get(self.webAddres);
        self.ebayS=EbayStepp(self.eleDriver)


 def test_SearchEbay(self):
         self.ebayS.test_Search_Ebay_Step()
         self.ebayS.test_Click_Charac_Size_Ebay_Step()
         self.ebayS.test_Order_Elements_Ebay_Step()
         self.ebayS.test_Order_Elements_Desc_Ebay_Step()



 def tearDown(self):
        # close the browser window
        self.eleDriver.quit()
           
        
if __name__ == '__main__':
 unittest.main()