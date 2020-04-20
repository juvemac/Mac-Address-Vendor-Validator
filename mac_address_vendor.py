import requests
import getopt
import json
import sys
import re

api_key = ""
url_base = "https://api.macaddress.io/v1?apiKey={api_key}&output={format}&search={mac_address}"

arguments = sys.argv[1:]
options = "ha:"
full_options = ["help","address"]

def validate_mac_address(mac_address):
	pattern = r"([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}"
	invalid_address = not bool(re.match(pattern, mac_address))
	if invalid_address:
		print("Invalid mac address, supported format: 00:00:00:00:00:00")
		print("Input received: " + mac_address)
		sys.exit()

def process_response(response):
	if response.status_code > 400:
		json_error = json.loads(response.text)
		print("Error: " + json_error["error"])
		sys.exit()

	json_response = json.loads(response.text)
	
	print("Vendor: " + json_response["vendorDetails"]["companyName"])
	print("Vendor Address: " + json_response["vendorDetails"]["companyAddress"])
	print("Vendor Country: " + json_response["vendorDetails"]["countryCode"])

try:
	arguments, values = getopt.getopt(arguments, options, full_options)

	if len(arguments) == 0:
		print("Usage: mac_address_vendor.py -a 00:00:00:00:00:00")
		sys.exit()

	for argument, value in arguments:

		if argument in ("-h", "--help"):
			print("Usage: mac_address_vendor.py -a 00:00:00:00:00:00")
			sys.exit()

		elif argument in ("-a", "--address"):
			validate_mac_address(value)
			url = url_base.format(api_key=api_key, format="json", mac_address=value)
			response = requests.get(url)
			process_response(response)
            
except getopt.error as err:
    print(str(err)) 
    sys.exit(2)   