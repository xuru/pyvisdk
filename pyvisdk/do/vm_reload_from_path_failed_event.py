
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmReloadFromPathFailedEvent(VmEvent):
    '''This event records that a virtual machine reload from a new configuration path
        failed.
    '''
    
    def __init__(self, configPath):
        # MUST define these
        super(VmReloadFromPathFailedEvent, self).__init__()
    
        self.data['configPath'] = configPath
    
    
    @property
    def configPath(self):
        '''
        '''
        return self.data['configPath']

