
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmMessageEvent(VmEvent):
    '''This event records when an informational message (consisting of a collection of
        "observations") is thrown by the virtual machine. This is a generic event
        for such messages.
    '''
    
    def __init__(self, message, messageInfo):
        # MUST define these
        super(VmMessageEvent, self).__init__()
    
        self.data['message'] = message
        self.data['messageInfo'] = messageInfo
    
    
    @property
    def message(self):
        '''A raw message returned by the virtualization platform.
        '''
        return self.data['message']

    @property
    def messageInfo(self):
        '''VI API 2.5
        '''
        return self.data['messageInfo']

