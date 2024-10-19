from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import time
from pages.HomePage import HomePage



Service = Service(executable_path="")
driver = webdriver.Chrome(service=Service)

driver.get("https://google.com/finance/")
driver.maximize_window()
page = HomePage(driver)

# Verify the page title
assert page.verify_page_title().__contains__( "Finance"), "Page title is incorrect."
assert page.getWatchlistSectionText().__contains__( "You may be interested in"), "Icon title is incorrect."

# Given test data
expected_stocks = ["NFLX", "MSFT", "TSLA"]
# Print all stock symbols that are in retrieved_stocks but not in given test data
print(page.compareTheStockSymbolsNotInGivenTestData(expected_stocks))
# Print all stock symbols that are in in given test dataocks but not in retrieved_stocks
print(page.compareTheStockSymbolsNotInRetrievedStocks(expected_stocks))

page.driver.quit


