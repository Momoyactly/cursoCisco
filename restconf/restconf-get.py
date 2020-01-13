import requests, json
from router_info import router

url = "https://"+router["host"]+"/restconf/data/Cisco-IOS-XE-interfaces-oper:interfaces/interface=GigabitEthernet2"

headers = {
  'Accept': 'application/yang-data+json',
  'Content-Type': 'application/yang-data+json'
}

response = requests.request("GET", url, headers=headers,auth=(router["username"],router["password"]),verify=False)

jsonResponse =response.json()
print("Description:",jsonResponse["Cisco-IOS-XE-interfaces-oper:interface"]["description"])
if jsonResponse["Cisco-IOS-XE-interfaces-oper:interface"]["admin-status"] == "if-state-up":
    print("Interface is UP")