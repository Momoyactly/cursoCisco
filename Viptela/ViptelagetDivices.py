import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
print("*"*50)

url = "https://sandboxsdwan.cisco.com:8443/j_security_check"
payload = 'j_username=devnetuser&j_password=Cisco123%21'
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}
sesion = requests.session()
response = sesion.post( url, headers=headers, data = payload,verify=False)

if not response.ok or response.text:
    print("login failure")
    import sys
    sys.exit(1)
else:
    print("Login Worked")


url = "https://sandboxsdwan.cisco.com:8443/dataservice/device"


response = sesion.get(url,verify=False).json()
data = response["data"]
for device in data:
    print("hostname:",device["host-name"])
    print("IP      :",device["local-system-ip"])
    print("Model   :",device["device-model"])
    print("")

