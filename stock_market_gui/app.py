from flask import Flask, request, render_template
import requests
import threading
import os
app = Flask(__name__)

# Page Requests
@app.route('/')
def index():
	return render_template('index.html')

@app.route('/management')
def management():
	return render_template('management.html')

@app.route('/news')
def news():
	return render_template('news.html')

@app.route('/automation')
def automation():
	return render_template('automation.html')


# Data Requests

"""
@app.route('/update_car', methods=['POST'])
def update_car():
	# Gather booking request data
	bookingInfo = request.json

	# Process Data
	bookingServiceUrl = "http://localhost:5002/booking_availability"
	resp = requests.post(bookingServiceUrl,json=bookingInfo)

	# Start Background Thread
	t = threading.Thread(target=fireSaveRequests,args=[bookingInfo])
	t.start()

	# Return user to booking page with dates pre-booked if available, if not then return error message to user 
	if (resp.text == "available"):
		return "Success"
	else:
		return "Failure"
"""
"""
# Background Processes
def fireSaveRequests(bookingInfo):
	bookingSendToVRBOServiceUrl = "http://localhost:5002/send_booked_information_to_vrbo"
	resp = requests.post(bookingSendToVRBOServiceUrl,json=bookingInfo)
"""

	
# Run app on 0.0.0.0:5000
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5000))
	app.run(host='0.0.0.0', port=port)
