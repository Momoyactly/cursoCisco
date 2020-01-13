import requests, json

url = "http://172.16.1.12/ins"

payload = {"ins_api": { "version": "1.2","type": "cli_show","chunk": "0","sid": "1","input": "sh ip int brief","output_format": "json"}}
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic YWRtaW46YWRtaW4='
}

response = requests.request("POST", url, headers=headers, json = payload,auth=("admin","admin")).json()

print(json.dumps(response,indent=2,sort_keys=True))
