from flask import Flask
import requests
import os

from src.DatabaseManager import *

app = Flask(__name__)

# Data Requests
@app.route('/get_journal_list', methods=['GET'])
def get_journal_list():
	database = DatabaseManager()
	journalList = database.getJournalList()

	return journalList

	
# Run app on 0.0.0.0:5001
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5001))
	app.run(host='0.0.0.0', port=port)
