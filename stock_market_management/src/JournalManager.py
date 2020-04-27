
class JournalManager:
	def __init__(self,journalList):
		self.journalList = journalList
		self.journalDict = []

	def convertListTODict(self):
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

