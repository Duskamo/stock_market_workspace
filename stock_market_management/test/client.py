import requests

def testJournalList():
	managementServiceUrl = "http://localhost:5001/get_journal_list"
	resp = requests.get(managementServiceUrl)

	print(resp.text)

def import_data_to_table():
	managementServiceUrl = "http://localhost:5001/import_data_to_table"
	resp = requests.get(managementServiceUrl)

	print(resp.text)

#testJournalList()
import_data_to_table()
