
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineStorageSummary(DynamicData):
    '''A subset of the storage information of this virtual machine.See
        VirtualMachineStorageInfo for a detailed storage break-up.
    '''
    
    def __init__(self, committed, timestamp, uncommitted, unshared):
        # MUST define these
        super(VirtualMachineStorageSummary, self).__init__()
    
        self.data['committed'] = committed
        self.data['timestamp'] = timestamp
        self.data['uncommitted'] = uncommitted
        self.data['unshared'] = unshared
    
    
    @property
    def committed(self):
        '''Total storage space, in bytes, committed to this virtual machine across all
        datastores.
        '''
        return self.data['committed']

    @property
    def timestamp(self):
        '''Time when values in this structure were last updated.
        '''
        return self.data['timestamp']

    @property
    def uncommitted(self):
        '''Additional storage space, in bytes, potentially used by this virtual machine on
        all datastores.
        '''
        return self.data['uncommitted']

    @property
    def unshared(self):
        '''Total storage space, in bytes, occupied by the virtual machine across all
        datastores, that is not shared with any other virtual machine.
        '''
        return self.data['unshared']

