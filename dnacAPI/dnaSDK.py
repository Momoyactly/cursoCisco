from dnacentersdk import api

dna = api.DNACenterAPI(username="devnetuser",password="Cisco123!")
"""
clientes = dna.clients.get_overall_client_health()["response"][0]["scoreDetail"]
for cleinte in clientes:
    print("categoria del score:",cleinte["scoreCategory"]["scoreCategory"],"con el valor:",cleinte["scoreCategory"]["value"])
"""

devices = dna.devices.get_device_list()["response"]
for device in devices:
    print("El dispositivo tiene el nombre de:",device.hostname, "con numero de Serie:",device.serialNumber)