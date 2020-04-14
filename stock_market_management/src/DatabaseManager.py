import mysql.connector

class DatabaseManager:
	def __init__(self):
		self.mydb = mysql.connector.connect(
			host="localhost",
			user="duskamo",
			passwd="Sassy13",
			database="stock_market_workspace"
		)

		self.mycursor = self.mydb.cursor()

	def getJournalList(self):
		self.mycursor.execute("SELECT * FROM trading_journal")
		
		myresult = self.mycursor.fetchall()

		return {"journalList" : myresult}
