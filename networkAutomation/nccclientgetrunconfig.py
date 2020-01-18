from ncclient import manager

with manager.connect(host="172.16.1.11", port=830, username="uriel",password="cisco123", hostkey_verify=False) as m:
    c = m.get().data_xml
    with open("%s.xml" % "CSRv2", 'w') as f:
        f.write(c)