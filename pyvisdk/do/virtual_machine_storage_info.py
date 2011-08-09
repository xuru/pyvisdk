
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineStorageInfo(DynamicData):
    '''Information about the amount of storage used by a virtual machine across
        datastores that it is located on.
    '''
    
    def __init__(self, perDatastoreUsage, timestamp):
        # MUST define these
        super(VirtualMachineStorageInfo, self).__init__()
    
        self.data['perDatastoreUsage'] = perDatastoreUsage
        self.data['timestamp'] = timestamp
    
    
    @property
    def perDatastoreUsage(self):
        '''Storage space used by this virtual machine on all datastores that it is located
        on.
        '''
        return self.data['perDatastoreUsage']

    @property
    def timestamp(self):
        '''Time when values in this structure were last updated.
        '''
        return self.data['timestamp']

