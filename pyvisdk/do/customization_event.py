
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationEvent(VmEvent):
    '''Base for customization events.
    '''
    
    def __init__(self, logLocation):
        # MUST define these
        super(CustomizationEvent, self).__init__()
    
        self.data['logLocation'] = logLocation
    
    
    @property
    def logLocation(self):
        '''The location of the in-guest customization log which will contain details of the
        customization operation.
        '''
        return self.data['logLocation']

