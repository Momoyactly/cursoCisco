from ncclient import manager
from router_info import router

configInterfaceTemplate = open("/Users/joarriag/Dev/cursoCisco/netconf/ios_config.xml").read()
netconfConfig = configInterfaceTemplate.format(interfaceName="GigabitEthernet2",interfaceDesc="Uriel wuz here")

with manager.connect(host=router["host"],
                    port=router["port"],
                    username=router["username"],
                    password=router["password"], 
                    hostkey_verify=False) as m:
    deviceReply = m.edit_config(netconfConfig, target="running")
    print(deviceReply)
