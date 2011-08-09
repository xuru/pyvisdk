
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineConfigInfoDatastoreUrlPair(DynamicData):
    '''Contains the name of a datastore, and its local file path on the host currently
        affiliated with this virtual machine.
    '''
    
    def __init__(self, name, url):
        # MUST define these
        super(VirtualMachineConfigInfoDatastoreUrlPair, self).__init__()
    
        self.data['name'] = name
        self.data['url'] = url
    
    
    @property
    def name(self):
        '''
        '''
        return self.data['name']

    @property
    def url(self):
        '''
        '''
        return self.data['url']

