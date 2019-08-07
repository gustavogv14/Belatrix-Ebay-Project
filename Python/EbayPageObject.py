import time
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.driver import ChromeDriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains

 
class EbayPageObject():

#-----------------------VARIABLES-----------------------
 eleTFSearchXpath="//*[@id='gh-ac']"
 eleBTNSearchXpath="//*[@id='gh-btn']"
 eleChBSizeXpath="//*[@id='w3']/li[1]/ul/li[2]/ul/li[1]/ul/li[5]/div/a/span[1]"
 eleTFSearchBrandXpath="//*[@id='w3-w3-0[0]']"
 eleChBBrand="//*[@id='w3-w3']/ul/li[7]/div/a/span[1]"
 eleLblResults="//*[@id='mainContent']/div[1]/div/div[2]/div/div[1]/h1"
 eleDdlSort="//*[@id='w7']/button/div"
 eleDdlOpc4="//*[@id='w7']/div/div/ul/li[4]/a/span"
 eleDdlOpc5="//*[@id='w7']/div/div/ul/li[5]/a/span"
 eleLblPrice1="//*[@id='srp-river-results-listing1']/div/div[2]/div[4]/div[1]/span"
 eleLblPrice1_Ship="//*[@id='srp-river-results-listing1']/div/div[2]/div[4]/div[3]/span"
 eleLblPriceDesc1="//*[@id='srp-river-results-listing1']/div/div[2]/div[3]/div[1]/span[1]"
 eleLblPriceDesc2="//*[@id='srp-river-results-listing2']/div/div[2]/div[3]/div[1]/span"
 eleLblPriceDesc3="//*[@id='srp-river-results-listing3']/div/div[2]/div[3]/div[1]/span"
 eleLblPriceDesc4="//*[@id='srp-river-results-listing4']/div/div[2]/div[3]/div[1]/span[1]"
 eleLblPriceDesc5="//*[@id='srp-river-results-listing5']/div/div[2]/div[3]/div[1]/span"
 eleLblPrice2="//*[@id='srp-river-results-listing2']/div/div[2]/div[3]/div[1]/span[1]"
 eleLblPrice2_Ship="//*[@id='srp-river-results-listing2']/div/div[2]/div[3]/div[2]/span"
 eleLblPrice3="//*[@id='srp-river-results-listing3']/div/div[2]/div[3]/div[1]/span"
 eleLblPrice3_Ship="//*[@id='srp-river-results-listing3']/div/div[2]/div[3]/div[3]/span"
 eleLblPrice4="//*[@id='srp-river-results-listing4']/div/div[2]/div[3]/div[1]/span"
 eleLblPrice4_Ship="//*[@id='srp-river-results-listing4']/div/div[2]/div[3]/div[3]/span"
 eleLblPrice5="//*[@id='srp-river-results-listing5']/div/div[2]/div[3]/div[1]/span"
 eleLblName1="//*[@id='srp-river-results-listing1']/div/div[2]/a/h3"
 eleLblName2="//*[@id='srp-river-results-listing2']/div/div[2]/a/h3"
 eleLblName3="//*[@id='srp-river-results-listing3']/div/div[2]/a/h3"
 eleLblName4="//*[@id='srp-river-results-listing4']/div/div[2]/a/h3"
 eleLblName5="//*[@id='srp-river-results-listing5']/div/div[2]/a/h3"
 eleLblName1Desc="//*[@id='srp-river-results-listing1']/div/div[2]/a/h3"
 eleLblName2Desc="//*[@id='srp-river-results-listing2']/div/div[2]/a/h3"
 eleLblName3Desc="//*[@id='srp-river-results-listing3']/div/div[2]/a/h3"
 eleLblName4Desc="//*[@id='srp-river-results-listing4']/div/div[2]/a/h3"
 eleLblName5Desc="//*[@id='srp-river-results-listing5']/div/div[2]/a/h3"
#-----------------------VARIABLES-----------------------


 def __init__(self,driver):
        self.driver=driver


 def test_Search_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleTFSearchXpath)
        
 def test_Click_Search_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleBTNSearchXpath)
 
 def test_Click_CHB_Size_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleChBSizeXpath)
    
 def test_Search_Brand_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleTFSearchBrandXpath)
    
 def test_Click_CHB_Brand_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleChBBrand)
    
 def test_Get_LBL_Results_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblResults)
    
 def test_Click_DDL_Sort_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleDdlSort)
    
 def test_Click_DDL_Opc_Ebay_PO(self):
        action = ActionChains(self.driver);
        firstEleMenu=self.driver.find_element_by_xpath(self.eleDdlSort)
        action.move_to_element(firstEleMenu).perform();
        secondLevelMenu = self.driver.find_element_by_xpath(self.eleDdlOpc4)
        secondLevelMenu.click();
        time.sleep(2)
        
 def test_Get_Lbl_Price1_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblPrice1)
    
 def test_Get_Lbl_Price1_Ship_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblPrice1_Ship)
    
 def test_Get_Lbl_Price2_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblPrice2)
    
 def test_Get_Lbl_Price2_Ship_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblPrice2_Ship)   
    
 def test_Get_Lbl_Price3_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblPrice3)
    
 def test_Get_Lbl_Price3_Ship_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblPrice3_Ship)
    
 def test_Get_Lbl_Price4_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblPrice4)
    
 def test_Get_Lbl_Price4_Ship_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblPrice4_Ship)      
  
 def test_Get_Lbl_Price5_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblPrice5)
    
 def test_Get_Lbl_Name1_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblName1)   
  
 def test_Get_Lbl_Name2_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblName2)
    
 def test_Get_Lbl_Name3_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblName3) 
    
 def test_Get_Lbl_Name4_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblName4)
    
 def test_Get_Lbl_Name5_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblName5)   
    
 def test_Click_DDL_Opc_Desc_Ebay_PO(self):
        action = ActionChains(self.driver);
        firstEleMenu=self.driver.find_element_by_xpath(self.eleDdlSort)
        action.move_to_element(firstEleMenu).perform();
        secondLevelMenu = self.driver.find_element_by_xpath(self.eleDdlOpc5)
        secondLevelMenu.click();
        time.sleep(2)
            
 def test_Get_Lbl_Price1_Desc_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblPriceDesc1)
               
 def test_Get_Lbl_Price2_Desc_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblPriceDesc2)
    
 def test_Get_Lbl_Price3_Desc_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblPriceDesc3)   
    
 def test_Get_Lbl_Price4_Desc_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblPriceDesc4)
    
 def test_Get_Lbl_Price5_Desc_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblPriceDesc5)
    
 def test_Get_Lbl_Name1_Desc_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblName1Desc)
    
 def test_Get_Lbl_Name2_Desc_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblName2Desc)
    
 def test_Get_Lbl_Name3_Desc_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblName3Desc)
    
 def test_Get_Lbl_Name4_Desc_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblName4Desc)
    
 def test_Get_Lbl_Name5_Desc_Ebay_PO(self):
        return self.driver.find_element_by_xpath(self.eleLblName5Desc)            