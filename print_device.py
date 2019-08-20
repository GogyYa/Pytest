import requests
import json
from tabulate import *
from my_apic_em_functions import *

api_url = "https://devnetsbx-netacad-apicem-1.cisco.com/api/v1/network-device"
ticket = get_ticket()
headers = {
        "content-type": "application/json",
        "X-Auth-Token": ticket
        }

resp = requests.get(api_url, headers=headers, verify=False)
print("Status of /host request: ", resp.status_code)
if resp.status_code != 200:
    raise Exception("Status code does not equal 200. Response text: " + resp.text)
response_json = resp.json()

dev_list = []
i = 0
for item in response_json["response"]:
     i+=1
     host = [
             i,
             item["type"],
             item["managementIpAddress"],
             item["macAddress"]
            ]
     dev_list.append( host )
table_header = ["Number", "Type", "IP", "MAC"]
print( tabulate(dev_list, table_header) )

#print(host_list)
