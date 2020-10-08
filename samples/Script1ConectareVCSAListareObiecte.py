# 1.    Script Python conectare vCenter pentru a elimina conectarea manuala
#       si a reduce timpul de interventie in cazul unui incident

# Mai mult decat atat, am listat toate obiectele din inventarul VCSA:
# datacenter-e, cluster-e, host-uri, datastore-uri, vm-uri

from pyVim import connect
from pyVim.connect import SmartConnect, Disconnect
import ssl
import atexit
from pyVmomi import vim

# Conectarea la vCenter
s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode = ssl.CERT_NONE
si = SmartConnect(host="192.168.224.100", user="administrator@vsphere.local", pwd="Passw0rd!", sslContext=s)
aboutInfo = si.content.about
content = si.content
# Deconectare
atexit.register(connect.Disconnect, si)

# Afisarea informatiilor despre vCenter
print("VCSA Details:")
print("-----------------")
print("\tProduct Name:", aboutInfo.fullName)
print("\tProduct Build:", aboutInfo.build)
print("\tProduct Unique Id:", aboutInfo.instanceUuid)
print("\tProduct Version:", aboutInfo.version)
print("\tProduct Base OS:", aboutInfo.osType)
print("\tProduct vendor:", aboutInfo.vendor)
print("------------------")


# Metoda care populeaza obiecte de tipul vimtype
def get_all_objs(content, vimtype):
    obj = {}
    container = content.viewManager.CreateContainerView(content.rootFolder, vimtype, True)
    for managed_object_ref in container.view:
        obj.update({managed_object_ref: managed_object_ref.name})
    return obj


# Apelez metoda "get_all_objs"
dcs = get_all_objs(content, [vim.Datacenter])
clusters = get_all_objs(content, [vim.ClusterComputeResource])
hosts = get_all_objs(content, [vim.HostSystem])
datastores = get_all_objs(content, [vim.Datastore])
getAllVms = get_all_objs(content, [vim.VirtualMachine])

# DC
print("Show me the Datacenters:")
for dc in dcs:
    print("\t", dc.name)
print("---------------")

# Clusters
print("Show me the Clusters:")
for cluster in clusters:
    print("\t", cluster.name)
print("---------------")

# ESXi hosts
print("Show me the Hosts:")
for host in hosts:
    print("\t", host.name)
print("----------------")

# Datastores
print("Show me the Datastores:")
for datastore in datastores:
    print("\t", datastore.name)
print("----------------")

# VMs
print("Show me all the VMs in this VCSA:")
for vm in getAllVms:
    print("\t", vm.name)





