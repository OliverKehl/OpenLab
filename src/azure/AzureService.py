from azure import *
from azure.servicemanagement import *

subscription_id = '0db41f26-7fe8-4402-a13b-9efc38d25f14'
cert_file = '/home/kehl/mycert.pem'
class AzureService():
    def __init__(self,subscription_id=None, cert_file=None, host='management.core.chinacloudapi.cn'):
        '''
            constructor
        '''
        sms=ServiceManagementService(subscription_id,cert_file)
    
    
    
