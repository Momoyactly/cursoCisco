from ncclient import manager
import xml.dom.minidom
import xmltodict

netconf_filter="""
    <filter>
        <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>GigabitEthernet2</name>
            </interface>
        </interfaces>
        <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
            <interface>
                <name>GigabitEthernet2</name>
            </interface>
        </interfaces-state>
    </filter>
    """

with manager.connect(host="172.16.1.11",
                    port="830",
                    username="uriel",
                    password="cisco123", 
                    hostkey_verify=False) as m:
    interface_netconf = m.get(netconf_filter)
    interfaceDict = xmltodict.parse(interface_netconf.xml)["rpc-reply"]["data"]
    nombre = interfaceDict["interfaces"]["interface"]["name"]["#text"]
    config = interfaceDict["interfaces"]
    op_status = interfaceDict["interfaces-state"]
    print(f"nombre: {nombre}")
    print("Habilitada:",config["interface"]["enabled"])
    print("Paquetes entrando:",op_status["interface"]["statistics"]["in-unicast-pkts"])