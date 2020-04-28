import requests

def test_get_current_stock_news():
	managementServiceUrl = "http://localhost:5002/get_current_stock_news"
	resp = requests.get(managementServiceUrl)

	print(resp.text)

test_get_current_stock_news()
