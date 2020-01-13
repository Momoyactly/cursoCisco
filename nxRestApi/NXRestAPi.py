import requests

url = "https://172.16.1.13/api/aaaLogin.json"

payload = {"aaaUser":{"attributes":{"name": "cisco","pwd": "cisco"}}}
headers = {
  'Content-Type': 'application/json'
}

response = requests.post( url, headers=headers, json = payload,verify=False).json()

token =response["imdata"][0]["aaaLogin"]["attributes"]["token"]
cookies={}
cookies["APIC-cookie"]=token



url = "https://172.16.1.13/api/mo/sys/intf/phys-[eth1/97].json"

payload = {"l1PhysIf": {"attributes": {"descr":"Uriel wuz here from python"}}}
headers = {
  'Content-Type': 'application/json'
}

putResponse = requests.put( url, headers=headers, json = payload,cookies=cookies,verify=False).json()

print(putResponse)
