from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class BasePage:    
                   
    def findElement (self, locator, listOfElements = True ):
        if not listOfElements:
            element = self.driver.find_element(locator)
            return element
        elements = self.driver.find_elements(locator)
        return elements
    
    def getText(self, locator, listOfElements = True):
        if not listOfElements:
            element = self.driver.find_element(*locator)
            text = element.text
            return text   
        elements = self.driver.find_elements(*locator)
        texts = []
        for e in elements:
            texts.append(e.text)
        return texts
    
    def getAttributeValue(self, locator, name=""):
        element = self.driver.find_element(*locator)
        return element.get_attribute(name)
        
        
    
          
    
    

   