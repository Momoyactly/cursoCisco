from ncclient import manager
import xml.dom.minidom
import xmltodict
from router_info import router

netconf_filter = open("/Users/joarriag/Dev/cursoCisco/networkAutomation/netconfCdpFilter.xml").read()

with manager.connect(host=router["host"],
                    port=router["port"],
                    username=router["username"],
                    password=router["password"], 
                    hostkey_verify=False) as m:
    interface_netconf = m.get(netconf_filter)
    interfaceDict = xmltodict.parse(interface_netconf.xml)
    print(interfaceDict)
    """
    nombre = interfaceDict["interfaces"]["interface"]["name"]["#text"]
    config = interfaceDict["interfaces"]
    op_status = interfaceDict["interfaces-state"]
    print(f"nombre: {nombre}")
    print("Habilitada:",config["interface"]["enabled"])
    print("Paquetes entrando:",op_status["interface"]["statistics"]["in-unicast-pkts"])
    """