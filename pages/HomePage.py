from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.BasePage import BasePage
from selenium import webdriver

class HomePage(BasePage):  
    
    def __init__(self, driver):
        self.driver = driver
    
    def open_page(self,url):        
        self.driver.get(url)
        
        
    
    text_pageTitle = (By.XPATH, '//a[@id="sdgBod"]')
    text_watchlist = (By.XPATH, '//*[@id="smart-watchlist-title"]')  
    list_StockSymbols = (By.XPATH, '//ul[@class="sbnBtf"]//div[@class="COaKTb"]')
            
            
    def get_page_title(self):
        return self.driver.title
        
      # Verify if page title is correct
      
    def verify_page_title(self):
      
        return self.getAttributeValue(self.text_pageTitle,name="title")
        
        #return self.wait.until(EC.title_contains("Finance"))
       
    def getWatchlistSectionText(self):
        return self.getText(self.text_watchlist,listOfElements=False)
    
    def getListOfStockSymbolsTexts(self):
        stocks = self.getText(self.list_StockSymbols,listOfElements=True)
        for stock in stocks:
            if stock =="INDEX":
                stocks.remove(stock)
        return stocks
    
    def compareTheStockSymbolsNotInGivenTestData(self, expected_stocks):
        """Returns as a list of stock symbols that are in retrieved_stocks but not in given test data """
        # Step 3: Retrieve stock symbols from the UI
        retrieved_stocks = self.getListOfStockSymbolsTexts()
        print("retrieved_stocks = ",retrieved_stocks)
        list1 = []
        for stock in retrieved_stocks:
            if stock not in expected_stocks:
                list1.append(stock) 
        return list1               
        
    def compareTheStockSymbolsNotInRetrievedStocks(self,expected_stocks):
        """Retuns as a list of all stock symbols that are in retrieved_stocks but not in given test data"""
        # Step 3: Retrieve stock symbols from the UI
        retrieved_stocks = self.getListOfStockSymbolsTexts()
        list2 = []
        for stock in expected_stocks :
            if stock not in retrieved_stocks:
                list2.append(stock) 
        return list2   
    
    
        
        
        
          
            
            
                
  
        
        
                
    







    

   