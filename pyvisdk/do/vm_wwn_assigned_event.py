
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmWwnAssignedEvent(VmEvent):
    '''This event records the assignment of a new WWN (World Wide Name) to a virtual
        machine.
    '''
    
    def __init__(self, nodeWwns, portWwns):
        # MUST define these
        super(VmWwnAssignedEvent, self).__init__()
    
        self.data['nodeWwns'] = nodeWwns
        self.data['portWwns'] = portWwns
    
    
    @property
    def nodeWwns(self):
        '''The new node WWN.
        '''
        return self.data['nodeWwns']

    @property
    def portWwns(self):
        '''The new port WWN.
        '''
        return self.data['portWwns']

