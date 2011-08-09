
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineUsageOnDatastore(DynamicData):
    '''Storage space used by this virtual machine on a particular datastore.
    '''
    
    def __init__(self, committed, datastore, uncommitted, unshared):
        # MUST define these
        super(VirtualMachineUsageOnDatastore, self).__init__()
    
        self.data['committed'] = committed
        self.data['datastore'] = datastore
        self.data['uncommitted'] = uncommitted
        self.data['unshared'] = unshared
    
    
    @property
    def committed(self):
        '''Storage space, in bytes, on this datastore that is actually being used by the
        virtual machine.
        '''
        return self.data['committed']

    @property
    def datastore(self):
        '''Reference to datastore for which information is being provided.
        '''
        return self.data['datastore']

    @property
    def uncommitted(self):
        '''Additional storage space, in bytes, potentially used by the virtual machine on
        this datastore.
        '''
        return self.data['uncommitted']

    @property
    def unshared(self):
        '''Storage space, in bytes, occupied by the virtual machine on this datastore that is
        not shared with any other virtual machine.
        '''
        return self.data['unshared']

