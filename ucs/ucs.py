from ucsmsdk.ucshandle import UcsHandle

devnetUcs = UcsHandle("10.10.20.113","ucspe","ucspe")

devnetUcs.login()

org = devnetUcs.query_classid(class_id="orgOrg",hierarchy=True)

print(org)


servers = devnetUcs.query_classid("computeBlade")

for server in servers:
    print(server)

for server in servers :
    print(server.dn,server.num_of_cpus,server.available_memory)


blade = devnetUcs.query_dn("sys/chassis-3/blade-1")

print(blade)
devnetUcs.logout()