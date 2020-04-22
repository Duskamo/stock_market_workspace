import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options

class TransactionGatherAutomator:
	def __init__(self):
		self.tansactionList = []

	def extractTransactionData(self):
		chrome_options = Options()
		chrome_options.add_argument("--headless")

		driver = webdriver.Chrome(executable_path=os.path.abspath("/var/www/html/p35/stock_market_workspace/stock_market_management/libs/chromedriver2"),chrome_options=chrome_options)

		driver.get("http://www.python.org")
		assert "Python" in driver.title
		elem = driver.find_element_by_name("q")
		elem.clear()
		elem.send_keys("pycon")
		elem.send_keys(Keys.RETURN)
		assert "No results found." not in driver.page_source

		driver.close()

	def getData(self):
		return self.tansactionList
