import pytest
import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pages.HomePage import HomePage

class GoogleFinanceTest(unittest.TestCase):

    
   
    def setUp(self):
        # Set up the WebDriver for Chrome
        
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.google.com/finance")
        self.driver.maximize_window()
              
    def test_google_finance_stocks(self):
        # Initialize the page object
        page = HomePage(self.driver)
        
        #assert "Google Finance" in self.get_title(), "Page did not load properly"                
        assert page.verify_page_title().__contains__( "Finance"), "Page title is incorrect."
        assert page.getWatchlistSectionText().__contains__( "You may be interested in"), "Icon title is incorrect."    

            # Given test data
        given_stocks = ["NFLX", "MSFT", "TSLA"]
                # Print all stock symbols that are in retrieved_stocks but not in given test data
        print(page.compareTheStockSymbolsNotInGivenTestData(given_stocks))
                # Print all stock symbols that are in in given test dataocks but not in retrieved_stocks
        print(page.compareTheStockSymbolsNotInRetrievedStocks(given_stocks))
        
    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
            
            
                
                
            
    
        

        
        
                    
                    
            
            
