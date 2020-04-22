from flask import Flask
import requests
import os

from src.DatabaseManager import *
from src.JournalManager import *
from src.TransactionGatherAutomator import *

app = Flask(__name__)

# Data Requests
@app.route('/get_journal_list', methods=['GET'])
def get_journal_list():
	# Fetch saved orders and info from database
	database = DatabaseManager()
	journalList = database.getJournalList()

	# 1.) Convert saved journal list data to dictionary object
	# 2.) Add new fields and calculations and return newly crafted json object to GUI
	journalManager = JournalManager(journalList)
	journalManager.convertListTODict()
	journalManager.appendCalculatedFields()
	journal = journalManager.getJournal()
	

	return journal

@app.route('/import_data_to_table', methods=['GET'])
def import_data_to_table():
	# Login to MarketWatch and download data
	transactionAutomator = TransactionGatherAutomator()
	transactionAutomator.extractTransactionData()
	transactionList = transactionAutomator.getData()

	# Convert data to journal format

	# Save journal to database

	return "True"
	
# Run app on 0.0.0.0:5001
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5001))
	app.run(host='0.0.0.0', port=port)
