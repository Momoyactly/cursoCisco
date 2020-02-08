import requests,json,urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

urlBase = "https://fmcrestapisandbox.cisco.com/"
loginUrl = "api/fmc_platform/v1/auth/generatetoken"

payload = {}
headers = {
  'Authorization': 'Basic am9hcnJpYWc6cmRrN1h3OWg='
}

response = requests.post( urlBase + loginUrl, headers=headers,verify=False)
token = response.headers.get("X-auth-access-token")

print(token)

appsUrl = "api/fmc_config/v1/domain/e276abec-e0f2-11e3-8169-6d9ed49b625f/object/applications"

headers = {
  'X-auth-access-token': token
}

response = requests.get( urlBase + appsUrl, headers=headers,verify=False).json()

print(json.dumps(response["links"],indent=2))
