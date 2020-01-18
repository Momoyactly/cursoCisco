from ncclient import manager

with manager.connect(host="172.16.1.11",
                    port="830",
                    username="uriel",
                    password="cisco123", 
                    hostkey_verify=False) as m:
    for capacidad in m.server_capabilities:
        print("*"*5)
        print(capacidad)