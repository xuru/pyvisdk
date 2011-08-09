
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmPrimaryFailoverEvent(VmEvent):
    '''This event records a fault tolerance failover. The reason could be : lost
        connection to primary, partial hardware failure of primary or by user.
    '''
    
    def __init__(self, reason):
        # MUST define these
        super(VmPrimaryFailoverEvent, self).__init__()
    
        self.data['reason'] = reason
    
    
    @property
    def reason(self):
        '''The reason for the failure. see VirtualMachineNeedSecondaryReason
        '''
        return self.data['reason']

