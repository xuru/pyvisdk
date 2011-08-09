
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostScsiTopologyTarget(DynamicData):
    '''This data object type describes the SCSI target that is associated with a list of
        logical units.
    '''
    
    def __init__(self, key, lun, target, transport):
        # MUST define these
        super(HostScsiTopologyTarget, self).__init__()
    
        self.data['key'] = key
        self.data['lun'] = lun
        self.data['target'] = target
        self.data['transport'] = transport
    
    
    @property
    def key(self):
        '''The identifier for the SCSI target
        '''
        return self.data['key']

    @property
    def lun(self):
        '''The list of SCSI logical units with which a target is associated.
        '''
        return self.data['lun']

    @property
    def target(self):
        '''The target identifier.
        '''
        return self.data['target']

    @property
    def transport(self):
        '''SCSI Transport information about the target.
        '''
        return self.data['transport']

