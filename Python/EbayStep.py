import unittest
import time
import unicodedata
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.driver import ChromeDriver
from selenium.webdriver.chrome.webdriver import WebDriver
from Python.EbayPageObject import EbayPageObject
from lib2to3.tests.support import driver
from _overlapped import NULL
from selenium.webdriver.common.action_chains import ActionChains
    



 
class EbayStepp():
    
    eleSearch="Shoes"    
    
    def __init__(self,driver):
        self.driver=driver
        self.ebayPO=EbayPageObject(self.driver)         
    
    
    def test_Search_Ebay_Step(self):
        self.ebayPO.test_Search_Ebay_PO().send_keys(self.eleSearch)
        self.ebayPO.test_Click_Search_Ebay_PO().click()
        time.sleep(2)
        
    def test_Click_Charac_Size_Ebay_Step(self):
        target=self.ebayPO.test_Click_CHB_Size_Ebay_PO()
        self.driver.execute_script('arguments[0].scrollIntoView(true);', target)
        self.ebayPO.test_Click_CHB_Size_Ebay_PO().click()
        self.ebayPO.test_Search_Brand_Ebay_PO().send_keys("puma")
        time.sleep(2)
        self.ebayPO.test_Click_CHB_Brand_Ebay_PO().click()
        time.sleep(2)
        
    def elimina_tildes(self,cadena):
        s = ''.join((c for c in unicodedata.normalize('NFD',cadena) if unicodedata.category(c) != 'Mn'))
        return s   
        
        
    def test_Order_Elements_Ebay_Step(self):    
        print("--------------------------------------------------------------------------")
        print("Total resultados Puma talla 10")
        print("--------------------------------------------------------------------------")
        print(self.ebayPO.test_Get_LBL_Results_Ebay_PO().text)
        self.ebayPO.test_Click_DDL_Opc_Ebay_PO()
        numero1=float(self.ebayPO.test_Get_Lbl_Price1_Ebay_PO().text[5:].replace(' ',''))+float(self.ebayPO.test_Get_Lbl_Price1_Ship_Ebay_PO().text[6:15].replace(' ',''))
        print("--------------------------------------------------------------------------")
        print("Orden Ascendente")
        print("--------------------------------------------------------------------------")
        print(self.ebayPO.test_Get_Lbl_Name1_Ebay_PO().text+' ')
        print(numero1)
        numero2=float(self.ebayPO.test_Get_Lbl_Price2_Ebay_PO().text[5:].replace(' ',''))+float(self.ebayPO.test_Get_Lbl_Price2_Ship_Ebay_PO().text[6:15].replace(' ',''))
        print(self.ebayPO.test_Get_Lbl_Name2_Ebay_PO().text+' ')
        print(numero2)
        numero3=float(self.ebayPO.test_Get_Lbl_Price3_Ebay_PO().text[5:].replace(' ',''))+float(self.ebayPO.test_Get_Lbl_Price3_Ship_Ebay_PO().text[6:15].replace(' ',''))
        print(self.ebayPO.test_Get_Lbl_Name3_Ebay_PO().text+' ')
        print(numero3)
        numero4=float(self.ebayPO.test_Get_Lbl_Price4_Ebay_PO().text[5:].replace(' ',''))+float(self.ebayPO.test_Get_Lbl_Price4_Ship_Ebay_PO().text[6:15].replace(' ',''))
        print(self.ebayPO.test_Get_Lbl_Name4_Ebay_PO().text+' ')
        print(numero4)
        numero5=float(self.ebayPO.test_Get_Lbl_Price5_Ebay_PO().text[5:].replace(' ',''))
        print(self.ebayPO.test_Get_Lbl_Name5_Ebay_PO().text+' ')
        print(numero5)
        assert numero1<=numero2 and numero2<=numero3 and numero3<=numero4 and numero4<=numero5
        time.sleep(2)
        
        
    def test_Order_Elements_Desc_Ebay_Step(self):
        self.ebayPO.test_Click_DDL_Opc_Desc_Ebay_PO()
        numeroDesc1=float(self.ebayPO.test_Get_Lbl_Price1_Desc_Ebay_PO().text[5:].replace(' ',''))
        print("--------------------------------------------------------------------------")
        print("Orden Descendente")
        print("--------------------------------------------------------------------------")
        print(self.ebayPO.test_Get_Lbl_Name1_Desc_Ebay_PO().text)
        print(numeroDesc1)
        numeroDesc2=float(self.ebayPO.test_Get_Lbl_Price2_Desc_Ebay_PO().text[5:].replace(' ',''))
        print(self.ebayPO.test_Get_Lbl_Name2_Desc_Ebay_PO().text)
        print(numeroDesc2)
        numeroDesc3=float(self.ebayPO.test_Get_Lbl_Price3_Desc_Ebay_PO().text[5:].replace(' ',''))
        print(self.ebayPO.test_Get_Lbl_Name3_Desc_Ebay_PO().text)
        print(numeroDesc3)
        numeroDesc4=float(self.ebayPO.test_Get_Lbl_Price4_Desc_Ebay_PO().text[5:].replace(' ',''))
        print(self.ebayPO.test_Get_Lbl_Name4_Desc_Ebay_PO().text)
        print(numeroDesc4)
        numeroDesc5=float(self.ebayPO.test_Get_Lbl_Price5_Desc_Ebay_PO().text[5:].replace(' ',''))
        print(self.ebayPO.test_Get_Lbl_Name5_Desc_Ebay_PO().text)
        print(numeroDesc5)