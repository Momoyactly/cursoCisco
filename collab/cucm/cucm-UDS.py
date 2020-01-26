import requests
import xml.dom.minidom
import xmltodict
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
print("*"*50)
url = "https://10.10.20.1/cucm-uds/users"

payload = {}
headers = {
  'Accept': 'application/xml',
  'Content-Type': 'application/xml',
  'Authorization': 'Basic YWRtaW5pc3RyYXRvcjpjaXNjb3BzZHQ='
}

response = requests.get(url, headers=headers, data = payload,verify=False)


tree = xml.dom.minidom.parseString(response.text)
bonito = tree.toprettyxml()

xmldata = xmltodict.parse(bonito)
users = xmldata["users"]["user"]

for user in users:
    print(user["lastName"],user["firstName"])
    print("ID:",user["id"])
    print(" ")

