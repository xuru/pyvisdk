
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ScsiLunCapabilities(DynamicData):
    '''Scsi device specific capabilities.
    '''
    
    def __init__(self, updateDisplayNameSupported):
        # MUST define these
        super(ScsiLunCapabilities, self).__init__()
    
        self.data['updateDisplayNameSupported'] = updateDisplayNameSupported
    
    
    @property
    def updateDisplayNameSupported(self):
        '''Can the display name of the SCSI device be updated?
        '''
        return self.data['updateDisplayNameSupported']

