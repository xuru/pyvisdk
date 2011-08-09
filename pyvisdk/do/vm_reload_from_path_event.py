
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmReloadFromPathEvent(VmEvent):
    '''This event records that a virtual machine was sucessfully reloaded from a new
        configuration path.
    '''
    
    def __init__(self, configPath):
        # MUST define these
        super(VmReloadFromPathEvent, self).__init__()
    
        self.data['configPath'] = configPath
    
    
    @property
    def configPath(self):
        '''
        '''
        return self.data['configPath']

