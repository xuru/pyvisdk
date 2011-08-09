
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmTimedoutStartingSecondaryEvent(VmEvent):
    '''This event records timeout when starting a secondary VM. A default alarm will be
        triggered upon this event, which by default would trigger a SNMP trap.
    '''
    
    def __init__(self, timeout):
        # MUST define these
        super(VmTimedoutStartingSecondaryEvent, self).__init__()
    
        self.data['timeout'] = timeout
    
    
    @property
    def timeout(self):
        '''The duration of the timeout in milliseconds.
        '''
        return self.data['timeout']

