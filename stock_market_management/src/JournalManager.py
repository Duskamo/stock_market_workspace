
class JournalManager:
	def __init__(self):
		self.journalList = []
		self.transactionList = []
		self.journalDict = []

	# Manager - From Initial Database List To Prepped Journal List For GUI  
	def addJournalList(self,journalList):
		self.journalList = journalList

	def convertJournalListTODict(self):
		listOfIndexes = ['trade_id','trade_date','symbol','type','quantity','bought','sold','initial_risk','commission','profit_and_loss']
		listOfLists = self.journalList['data']

		for i in range(len(listOfLists)):
			journalZipObj = zip(listOfIndexes,listOfLists[i])
			self.journalDict.append(dict(journalZipObj))

		self.journalDict = {'data': self.journalDict}
		
		return self.journalDict

	def appendCalculatedFields(self):
		for i in range(len(self.journalDict['data'])):
			money_at_work = self.journalDict['data'][i]['quantity'] * self.journalDict['data'][i]['bought']
			winLoss = 1 if (self.journalDict['data'][i]['profit_and_loss'] > 0) else 0
			sumWinLoss = winLoss + (0 if (i == 0) else self.journalDict['data'][i-1]['sum_wl'])

			self.journalDict['data'][i]['r_multiple'] = round(self.journalDict['data'][i]['profit_and_loss'] / self.journalDict['data'][i]['initial_risk'],2)
			self.journalDict['data'][i]['percent_wins'] = round(sumWinLoss / self.journalDict['data'][i]['trade_id'],2)
			self.journalDict['data'][i]['money_at_work'] = round(money_at_work,2)
			self.journalDict['data'][i]['percent_pl'] = round((self.journalDict['data'][i]['profit_and_loss'] / money_at_work) * 100,2)
			self.journalDict['data'][i]['initial_percent_risk'] = round((self.journalDict['data'][i]['initial_risk'] / money_at_work) * 100,2)
			self.journalDict['data'][i]['wl'] = winLoss
			self.journalDict['data'][i]['sum_wl'] = sumWinLoss

	def getJournal(self):
		return self.journalDict

	# Manager - From Initial Transaction List to Stored Database List
	def addTransactionList(self,transactionList):
		self.transactionList = transactionList

	def convertTransactionListToJournalList(self):
		for i in range(len(self.transactionList)):
			if (self.transactionList[i]['Type'] == "Sell"):
				for j in range(len(self.transactionList)):
					if (self.transactionList[i]['Amount'] == self.transactionList[j]['Amount'] and self.transactionList[i]['Symbol'] == self.transactionList[j]['Symbol'] and self.transactionList[i] != self.transactionList[j] and self.transactionList[j]['Type'] == "Buy"):
						self.journalList.append({
							'trade_date':self.transactionList[i]['Transaction Date'].split()[0],
							'symbol':self.transactionList[i]['Symbol'],
							'type':'L',
							'quantity':self.transactionList[i]['Amount'].replace(',',''),
							'bought':self.transactionList[i]['Price'][1:],
							'sold':self.transactionList[j]['Price'][1:],
							'initial_risk':round((float(self.transactionList[i]['Price'][1:])*float(self.transactionList[i]['Amount'].replace(',',''))*.01),2),
							'commission':"0",

							'profit_and_loss':round((float(self.transactionList[j]['Price'][1:])*float(self.transactionList[j]['Amount'].replace(',',''))) - (float(self.transactionList[i]['Price'][1:])*float(self.transactionList[i]['Amount'].replace(',',''))),2)
						})

		for i in range(len(self.journalList)):
			self.journalList[i]['trade_id'] = i + 1

		
	def getJournalList(self):
		return self.journalList
