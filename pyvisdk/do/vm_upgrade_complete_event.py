
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmUpgradeCompleteEvent(VmEvent):
    '''This event records the successful completion of an upgrade operation.
    '''
    
    def __init__(self, version):
        # MUST define these
        super(VmUpgradeCompleteEvent, self).__init__()
    
        self.data['version'] = version
    
    
    @property
    def version(self):
        '''The version of the agent.
        '''
        return self.data['version']

