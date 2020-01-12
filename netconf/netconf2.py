from ncclient import manager
import xml.dom.minidom

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
    xmlDom = xml.dom.minidom.parseString(str(interface_netconf))
    print(xmlDom.toprettyxml(indent="   "))