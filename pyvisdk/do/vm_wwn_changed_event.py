
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmWwnChangedEvent(VmEvent):
    '''This event records a change in a virtual machine's WWN (World Wide Name).
    '''
    
    def __init__(self, newNodeWwns, newPortWwns, oldNodeWwns, oldPortWwns):
        # MUST define these
        super(VmWwnChangedEvent, self).__init__()
    
        self.data['newNodeWwns'] = newNodeWwns
        self.data['newPortWwns'] = newPortWwns
        self.data['oldNodeWwns'] = oldNodeWwns
        self.data['oldPortWwns'] = oldPortWwns
    
    
    @property
    def newNodeWwns(self):
        '''The new node WWN.
        '''
        return self.data['newNodeWwns']

    @property
    def newPortWwns(self):
        '''The new port WWN.
        '''
        return self.data['newPortWwns']

    @property
    def oldNodeWwns(self):
        '''The old node WWN.
        '''
        return self.data['oldNodeWwns']

    @property
    def oldPortWwns(self):
        '''The old port WWN.
        '''
        return self.data['oldPortWwns']

