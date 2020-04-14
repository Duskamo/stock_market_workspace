from flask import Flask, request, render_template
import requests
import threading
import os
app = Flask(__name__)

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

	
# Run app on 0.0.0.0:5001
if __name__ == "__main__":
	port = int(os.environ.get('PORT', 5001))
	app.run(host='0.0.0.0', port=port)
