
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostScsiTopologyInterface(DynamicData):
    '''This data object type describes the SCSI interface that is associated with a list
        of targets.
    '''
    
    def __init__(self, adapter, key, target):
        # MUST define these
        super(HostScsiTopologyInterface, self).__init__()
    
        self.data['adapter'] = adapter
        self.data['key'] = key
        self.data['target'] = target
    
    
    @property
    def adapter(self):
        '''The link to data for this SCSI interface.
        '''
        return self.data['adapter']

    @property
    def key(self):
        '''The identifier for the SCSI interface
        '''
        return self.data['key']

    @property
    def target(self):
        '''The list of targets to which the SCSI interface is associated.
        '''
        return self.data['target']

