from flask import Flask, request, jsonify
import requests
import os

from src.StockNewsAPI import *

app = Flask(__name__)

# Data Requests
@app.route('/get_current_stock_news', methods=['POST'])
def get_current_stock_news():
	# Get input data from microservice
	stocksDict = request.get_json()	

	# Get current news from API
	stockNewsApi = StockNewsAPI(stocksDict['stocks'])
	articles = stockNewsApi.getAllArticles()
	
	return articles

	
# Run app on 0.0.0.0:5002
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5002))
	app.run(host='0.0.0.0', port=port)
