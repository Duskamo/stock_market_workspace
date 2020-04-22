import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time

class TransactionGatherAutomator:
	def __init__(self):
		self.tansactionList = []

	def setup(self):
		chrome_options = Options()
		chrome_options.add_argument("--headless")
		chrome_options.add_argument("--window-size=1920x1080")
		chrome_options.add_argument("--disable-notifications")
		chrome_options.add_argument('--no-sandbox')
		chrome_options.add_argument('--verbose')
		chrome_options.add_experimental_option("prefs", {
			"download.default_directory": "<path_to_download_default_directory>",
			"download.prompt_for_download": False,
			"download.directory_upgrade": True,
			"safebrowsing_for_trusted_sources_enabled": False,
			"safebrowsing.enabled": False
		})
		chrome_options.add_argument('--disable-gpu')
		chrome_options.add_argument('--disable-software-rasterizer')

		self.driver = webdriver.Chrome(executable_path=os.path.abspath("/var/www/html/p35/stock_market_workspace/stock_market_management/libs/chromedriver"),chrome_options=chrome_options)

		download_dir = "/var/www/html/p35/stock_market_workspace/stock_market_management/data"
		self.enable_download_headless(self.driver, download_dir)

	def login(self):
		self.driver.get("https://accounts.marketwatch.com/login?target=https%3A%2F%2Fwww.marketwatch.com%2F")
		usernameField = self.driver.find_element_by_xpath(".//input[@id='username']")
		passwordField = self.driver.find_element_by_xpath(".//input[@id='password']")
		signinButton = self.driver.find_element_by_xpath(".//button[@class='solid-button basic-login-submit']")

		usernameField.send_keys("dustinlandry1150@gmail.com")
		passwordField.send_keys("Sassy13")
		signinButton.click()

		time.sleep(2)

	def extractTransactionData(self):
		self.driver.get("https://www.marketwatch.com/game/duskamo/download?view=transactions&count=81&p=2989888")

	def teardown(self):
		self.driver.close()

	def readFromFile(self):
		""

	def getData(self):
		return self.tansactionList

	##################### private methods #####################33
	def enable_download_headless(self,browser,download_dir):
		browser.command_executor._commands["send_command"] = ("POST", '/session/$sessionId/chromium/send_command')
		params = {'cmd':'Page.setDownloadBehavior', 'params': {'behavior': 'allow', 'downloadPath': download_dir}}
		browser.execute("send_command", params)
