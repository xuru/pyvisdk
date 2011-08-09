
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class FaultToleranceConfigInfo(DynamicData):
    '''FaultToleranceConfigInfo is a data object type containing Fault Tolerance settings
        for this virtual machine. role, instanceUuids and configPaths contain
        information about the whole fault tolerance group.
    '''
    
    def __init__(self, configPaths, instanceUuids, role):
        # MUST define these
        super(FaultToleranceConfigInfo, self).__init__()
    
        self.data['configPaths'] = configPaths
        self.data['instanceUuids'] = instanceUuids
        self.data['role'] = role
    
    
    @property
    def configPaths(self):
        '''The configuration file path for all the VMs in this fault tolerance group.
        '''
        return self.data['configPaths']

    @property
    def instanceUuids(self):
        '''The instanceUuid of all the VMs in this fault tolerance group. The first element
        is the instanceUuid of the primary VM.
        '''
        return self.data['instanceUuids']

    @property
    def role(self):
        '''The index of the current VM in instanceUuids array starting from 1, so 1 means
        that it is the primary VM.
        '''
        return self.data['role']

