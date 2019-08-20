import time
import json
import requests
from my_apic_em_functions import *
from tabulate import *
requests.packages.urllib3.disable_warnings()

ticket = get_ticket()
api_url = "https://devnetsbx-netacad-apicem-1.cisco.com/api/v1/flow-analysis"

headers = {
        "content-type": "application/json",
        "X-Auth-Token": ticket
        }



print("list of hosts on the network: ")
print_hosts()

print("list of network devices on the network: ")
print_devices()

while True:
    s_ip = input('Please enter the src host IPadd for the path trace: ')
    d_ip = input('pls ender dst host IPadd: ')
    if s_ip != "" and d_ip != "":
        path_data = {
                      "sourceIP": s_ip,
                      "destIP": d_ip
  
            }
        print("src IP is: ", path_data["sourceIP"])
        print("dst IP is: ", path_data["destIP"])

        break
    else:
        print("enter correct IPAdd")
        continue
        

path = json.dumps(path_data)
resp = requests.post(api_url, path, headers=headers, verify=False)
#print(resp)

resp_json = resp.json()
#print(resp_json)

flowAnalysisId = resp_json["response"]["flowAnalysisId"]
print("Flow analysis ID: ", flowAnalysisId)


check_url = ("https://devnetsbx-netacad-apicem-1.cisco.com/api/v1/flow-analysis/" + flowAnalysisId)
print(check_url)
status = ""
checks = 1
while status != "COMPLETED":
    respGet = requests.get(check_url, headers=headers, verify=False)
    #print(respGet)
    respGet_json = respGet.json()
    status = respGet_json["response"]["request"]["status"]
    print("request status: ", status)

    if checks == 15:
        print("error")
    checks += 1

path_source = respGet_json["response"]["request"]["sourceIP"]
path_dest = respGet_json["response"]["request"]["destIP"]
print(" source ip is: ", path_source)
print(" dest ip is: ", path_dest)


networkElementsInfo = respGet_json["response"]["networkElementsInfo"]

all_device = []
device_no = 1

for networkDev in networkElementsInfo:
    #typeDev = respGet_json["type"]
    typeDev = networkDev["type"]
    if "name" not in networkDev:
        name = "unknown"
        ip = networkDev["ip"]
        ingressInterfaceName = "Unkn"
        egressInterfaceName = "Unkn"
    else:
        name = networkDev["name"]
        ip = networkDev["ip"]
        if "ingressInterface" in networkDev:
            
            ingressInterfaceName = networkDev["ingressInterface"]["physicalInterface"]["name"]
        else:
            ingressInterfaceName = "UNKN"
        if "egressInterface" in networkDev:
            egressInterfaceName = networkDev["egressInterface"]["physicalInterface"]["name"]
        else:
            egressInterfaceName = "UNKN"

    device = [
        device_no,
        typeDev,
        name,
        ip,
        ingressInterfaceName,
        egressInterfaceName
        ]
    all_device.append(device)
    device_no += 1


table_header = [
    "Item",
    "typeDev",
    "name",
    "ip",
    "ingressInterfaceName",
    "egressInterfaceName"
    ]

print( tabulate(all_device, table_header))


            
