import requests

def testJournalList():
	managementServiceUrl = "http://localhost:5001/get_journal_list"
	resp = requests.get(managementServiceUrl)

	print(resp.text)

testJournalList()
