import requests,json,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

urlBase = "https://fmcrestapisandbox.cisco.com/"
loginUrl = "api/fmc_platform/v1/auth/generatetoken"

payload = {}
headers = {
  'Authorization': 'Basic am9hcnJpYWc6cmRrN1h3OWg='
}
print("*"*50+"\n"+"Obteniendo token....")
response = requests.post( urlBase + loginUrl, headers=headers,verify=False)
token = response.headers.get("X-auth-access-token")
print("¡¡exitoso!!")

accessPolicysUrl = "api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/policy/accesspolicies"

headers = {
  'X-auth-access-token': token
}
body = {
  "type": "AccessPolicy",
  "name": "AccessPolicyUriel",
  "defaultAction": {
    "intrusionPolicy": {
      "name": "Security Over Connectivity",
      "id": "abba9b63-bb10-4729-b901-2e2aa0f4491c",
      "type": "IntrusionPolicy"
    },
    "variableSet": {
      "name": "Default Set",
      "id": "76fa83ea-c972-11e2-8be8-8e45bb1343c0",
      "type": "VariableSet"
    },
    "type": "AccessPolicyDefaultAction",
    "logBegin": False,
    "logEnd": True,
    "sendEventsToFMC": True
  }
}
print("*"*50+"\n"+"Creando Politica....")
response = requests.post( urlBase + accessPolicysUrl, headers=headers,json=body ,verify=False).json()
accesspolicyId = response["id"]
print("¡¡Politica Creada!! Id: ",accesspolicyId)

reglas= {
        "sendEventsToFMC": True,
        "action": "ALLOW",
        "enabled": True,
        "type": "AccessRule",
        "name": "Deep File Inspect Dst Geos",
        "logFiles": True,
        "logBegin": False,
        "logEnd": False,
        "variableSet": {
            "name": "Default Set",
            "id": "76fa83ea-c972-11e2-8be8-8e45bb1343c0",
            "type": "VariableSet"
        },
        "sourceNetworks": {
            "objects": [{
                "type": "NetworkGroup",
                "name": "IPv4-Private-All-RFC1918",
                "id": "15b12b14-dace-4117-b9d9-a9a7dcfa356f"
            }]
        },
        "filePolicy": {
            "name": "New Malware",
            "id": "59433a1e-f492-11e6-98fd-84ec1dfeed47",
            "type": "FilePolicy"
        }
    }
print("*"*50+"\n"+"Actualizando reglas....")
url ="/".join([urlBase,accessPolicysUrl,accesspolicyId,"accessrules"])
print(url)

response = requests.post( url, headers=headers,json=reglas ,verify=False).json()
print("Exito!!")

print(json.dumps(response,indent=2))

print("*"*50+"\n"+"Borrando....")
url ="/".join([urlBase,accessPolicysUrl,accesspolicyId])
response = requests.delete( url, headers=headers,verify=False).json()
print("Exito!!")