
from pyvisdk.do.event import Event
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostInventoryUnreadableEvent(Event):
    '''Event indicating that the virtual machine inventory file on the host is damaged or
        unreadable.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(HostInventoryUnreadableEvent, self).__init__()
    

    
    
