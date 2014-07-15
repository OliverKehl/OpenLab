from azure import *
from azure.servicemanagement import *

subscription_id = '0db41f26-7fe8-4402-a13b-9efc38d25f14'
cert_file = '/home/kehl/mycert.pem'
class AzureService():
    def __init__(self,subscription_id=None, cert_file=None, host='management.core.chinacloudapi.cn'):
        '''
            constructor
        '''
        self.sms=ServiceManagementService(subscription_id,cert_file)
        self.connected=True
    
    def create_virtual_machine(self,service_name,deployment_name):
        #judge whether the cloud service exist or not
        self.sms.ge
         
        #self.sms.create_virtual_machine_deployment(service_name, deployment_name, deployment_slot, label, role_name, system_config, os_virtual_hard_disk, network_config, availability_set_name, data_virtual_hard_disks, role_size, role_type, virtual_network_name)
    
    
