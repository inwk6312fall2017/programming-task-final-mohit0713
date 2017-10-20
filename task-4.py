import requests

import json

controller='devnetapi.cisco.com/sandbox/apic_em'
def getTicket():
	url = "https://" + controller + "/api/v1/ticket"
	payload = {"username":"devnetuser","password":"Cisco123!"}
	header = {"content-type": "application/json"}
	response= requests.post(url,data=json.dumps(payload), headers=header, verify=False)
	print (response)
getTicket()
