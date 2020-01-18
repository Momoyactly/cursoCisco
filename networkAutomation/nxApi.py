import requests

url = "https://172.16.1.13/api/aaaLogin.json"

payload = {"aaaUser":{"attributes":{"name": "uriel","pwd": "cisco123"}}}
headers = {
  'Content-Type': 'application/json'
}

response = requests.post( url, headers=headers, json = payload,verify=False).json()

token =response["imdata"][0]["aaaLogin"]["attributes"]["token"]
cookies={}
cookies["APIC-cookie"]=token



url = "https://172.16.1.13/api/node/mo/sys/cdp/inst/if-[eth1/2]/adj-1.json"

headers = {
  'Content-Type': 'application/json'
}

getResponse = requests.get( url, headers=headers, cookies=cookies,verify=False).json()
vecinoNombre=getResponse["imdata"][0]["cdpAdjEp"]["attributes"]["devId"]




url = "https://172.16.1.13/api/mo/sys/intf/phys-[eth1/2].json"

payload = {"l1PhysIf": {"attributes": {"descr":vecinoNombre+" es el vecino"}}}
headers = {
  'Content-Type': 'application/json'
}

putResponse = requests.put( url, headers=headers, json = payload,cookies=cookies,verify=False).json()

print(putResponse)
