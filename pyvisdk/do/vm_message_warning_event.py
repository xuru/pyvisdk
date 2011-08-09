
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmMessageWarningEvent(VmEvent):
    '''This event records when a warning message (consisting of a collection of
        "observations") is thrown by the virtual machine. This is a generic event
        for such messages.
    '''
    
    def __init__(self, message, messageInfo):
        # MUST define these
        super(VmMessageWarningEvent, self).__init__()
    
        self.data['message'] = message
        self.data['messageInfo'] = messageInfo
    
    
    @property
    def message(self):
        '''A raw message returned by the virtualization platform.
        '''
        return self.data['message']

    @property
    def messageInfo(self):
        '''
        '''
        return self.data['messageInfo']

