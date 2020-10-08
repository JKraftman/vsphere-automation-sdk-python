# Pentru Script 4
host = "192.168.224.100"
user = "Administrator@vsphere.local"
password = "Passw0rd!"
vcsa = "vcsa.vsphere.local"

# Pentru Script 5
inputs = {'vcenter_ip': '192.168.224.100',
          'vcenter_password': 'password',
          'vcenter_user': 'root',
          'vm_name': 'dummy_vm',
          # operation in 'create/remove/revert/
          # list_all/list_current/remove_all'
          'operation': 'list_all',
          'snapshot_name': 'snap1',
          'ignore_ssl': True
          }


