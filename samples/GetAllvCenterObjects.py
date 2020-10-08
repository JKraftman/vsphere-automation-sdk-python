

import pyVim
from pyVim.connect import SmartConnect
from pyVmomi import vim
import ssl

# List all the objects from vCenter server inventory


s = ssl.SSLContext(ssl.PROTOCOL_TLSv1)
s.verify_mode = ssl.CERT_NONE
si = pyVim.connect.SmartConnect(host="192.168.224.100", user="Administrator@vsphere.local", pwd="Passw0rd!", sslContext=s)
content = si.content


# Method that populates objects of type vimtype
def get_all_objs(content1, vimtype):
    obj = {}
    container = content1.viewManager.CreateContainerView(content1.rootFolder, vimtype, True)
    for managed_object_ref in container.view:
        obj.update({managed_object_ref: managed_object_ref.name})
    return obj


# Calling above method
dcs = get_all_objs(content, [vim.Datacenter])
clusters = get_all_objs(content, [vim.ClusterComputeResource])
hosts = get_all_objs(content, [vim.HostSystem])
datastores = get_all_objs(content, [vim.Datastore])
getAllVms = get_all_objs(content, [vim.VirtualMachine])

# DC
print("Show me the Datacenter: \n")
for dc in dcs:
    print(dc.name)
print()

# Iterating each cluster object and printing its name
print("Show me the clusters: \n")
for cluster in clusters:
    print(cluster.name)
print()

# ESX hosts
print("Show me the hosts: \n")
for host in hosts:
    print(host.name)
print()

# Iterating each vm object and printing its name
print("Show me all the VMs in this vCenter: \n")
for vm in getAllVms:
    print(vm.name)
print()

print("Show me the datastores: \n")
for datastore in datastores:
    print(datastore.name)
print()
