
from newsapi import NewsApiClient

class StockNewsAPI:
	def __init__(self,stocks):
		self.stocks = stocks
		self.newsAPI = NewsApiClient(api_key="88a224096f174b5e8c4468ec7fa47fb6")

	def getAllArticles(self):
		allArticles = []
		stocksList = self.stocks.split(',')

		for i in range(len(stocksList)):
			articles = self.newsAPI.get_everything(q=stocksList[i],
								   sort_by="publishedAt",
								   language="en")
			articles['stock'] = stocksList[i]

			allArticles.append(articles)

		return {'allArticles' : allArticles}

	
