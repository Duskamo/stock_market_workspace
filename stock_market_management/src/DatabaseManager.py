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
		self.mycursor.close()

		return {"data" : myresult}

	def insertJournalList(self,journalList):
		# Remove all entries from table
		self.mycursor.execute("TRUNCATE TABLE trading_journal")

		# Insert new data into table
		queryBeginning = "INSERT INTO trading_journal (trade_id, trade_date, symbol, type, quantity, bought, sold, initial_risk, commission, profit_and_loss) VALUES "
		queryBody = ""

		for i in range(len(journalList)):
			queryBody += "('{0}','{1}','{2}','{3}','{4}','{5}','{6}','{7}','{8}','{9}'),".format(journalList[i]['trade_id'],journalList[i]['trade_date'],journalList[i]['symbol'],journalList[i]['type'],float(journalList[i]['quantity']),float(journalList[i]['bought']),float(journalList[i]['sold']),float(journalList[i]['initial_risk']),float(journalList[i]['commission']),float(journalList[i]['profit_and_loss']))
		queryBody = queryBody[:-1] + ';'

		insertQuery = queryBeginning + queryBody

		self.mycursor.execute(insertQuery)
		self.mydb.commit()
		self.mycursor.close()

		return "Success"
