import requests
import json

url = "https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token"

headers = {
  'Authorization': 'Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='
}

response = requests.post( url, headers=headers).json()

token =response["Token"]

url = "https://sandboxdnac2.cisco.com/dna/intent/api/v1/client-health?timestamp"

headers = {
  'x-auth-token': token}

response = requests.get( url, headers=headers).json()
with open("dnacAPI/clientesHealth.json", 'w') as f:
        f.write(json.dumps(response))

print("Numero de clientes: ",response["response"][0]["scoreDetail"][0]["clientCount"])

