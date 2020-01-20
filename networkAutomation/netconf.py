from ncclient import manager
import xml.dom.minidom
import xmltodict
from router_info import router

netconf_filter = open("/Users/joarriag/Dev/cursoCisco/networkAutomation/netconfCdpFilter.xml").read()
configInterfaceTemplate = open("/Users/joarriag/Dev/cursoCisco/networkAutomation/iosXeConfig.xml").read()

with manager.connect(host=router["host"],
                    port=router["port"],
                    username=router["username"],
                    password=router["password"], 
                    hostkey_verify=False) as m:
    interface_netconf = m.get(netconf_filter)
    interfaceDict = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]
    cdpNeighName = interfaceDict["cdp-neighbor-details"]["cdp-neighbor-detail"]["device-name"]
    localIntName = interfaceDict["cdp-neighbor-details"]["cdp-neighbor-detail"]["local-intf-name"]
    print("vecino:",cdpNeighName,"interfaz:",localIntName)

    netconfConfig = configInterfaceTemplate.format(interfaceName=localIntName,interfaceDesc=cdpNeighName+" es el vecino en la interfaz: "+localIntName)
    deviceReply = m.edit_config(netconfConfig, target="running")
    replyDict = xmltodict.parse(deviceReply.xml)["rpc-reply"]
    if 'ok' in replyDict:
        print("OK")
    else:
        print("Fail")