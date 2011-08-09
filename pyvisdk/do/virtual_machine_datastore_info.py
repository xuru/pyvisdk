
from pyvisdk.do.virtual_machine_target_info import VirtualMachineTargetInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineDatastoreInfo(VirtualMachineTargetInfo):
    '''DatastoreInfo describes a datastore that a virtual disk can be stored on.
    '''
    
    def __init__(self, capability, datastore, maxFileSize, mode):
        # MUST define these
        super(VirtualMachineDatastoreInfo, self).__init__()
    
        self.data['capability'] = capability
        self.data['datastore'] = datastore
        self.data['maxFileSize'] = maxFileSize
        self.data['mode'] = mode
    
    
    @property
    def capability(self):
        '''Information about the datastore capabilities
        '''
        return self.data['capability']

    @property
    def datastore(self):
        '''Information about the datastore
        '''
        return self.data['datastore']

    @property
    def maxFileSize(self):
        '''The maximum size of a file that can reside on this datastore.
        '''
        return self.data['maxFileSize']

    @property
    def mode(self):
        '''Access mode for this datastore. This is either readOnly or readWrite. A virtual
        disk needs to be stored on readWrite datastore. ISOs can be read from a
        readOnly datastore.
        '''
        return self.data['mode']

