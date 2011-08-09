
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmUpgradingEvent(VmEvent):
    '''This event records the process of upgrading the virtual hardware on a virtual
        machine.
    '''
    
    def __init__(self, version):
        # MUST define these
        super(VmUpgradingEvent, self).__init__()
    
        self.data['version'] = version
    
    
    @property
    def version(self):
        '''The version of the agent.
        '''
        return self.data['version']

