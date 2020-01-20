import requests

url = "https://sandboxapicdc.cisco.com/api/aaaLogin.json"

payload = {"aaaUser": { "attributes": {"name": "admin","pwd": "ciscopsdt"}}}
headers = {
  'Content-Type': 'application/json'
}

response = requests.post(url, headers=headers, json = payload,verify=False).json()

token = response["imdata"][0]["aaaLogin"]["attributes"]["token"]

cookie ={"APIC-Cookie":token}

url = "https://sandboxapicdc.cisco.com/api/mo/uni.json"

payload = {"fvTenant" : {"attributes" : {"name" : "Uriel-lab"} }}
headers = {'Content-Type': 'application/json'}

response = requests.post( url, headers=headers,cookies=cookie, json = payload,verify=False).json()


url = "https://sandboxapicdc.cisco.com/api/mo/uni/tn-Uriel-lab/ap-Prueba.json"

payload = {"fvAp": {"attributes": {"descr": "Uriel wuz here from Python","dn": "uni/tn-Uriel-lab/ap-Prueba"}}}            
headers = {'Content-Type': 'application/json'}

response = requests.post( url, headers=headers,cookies=cookie, json = payload,verify=False).json()

print(response)
