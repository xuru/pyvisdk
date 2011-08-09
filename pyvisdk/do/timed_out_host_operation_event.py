
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class TimedOutHostOperationEvent(HostEvent):
    '''This event indicates that an operation performed on the host timed out. Typically,
        a previous event in the sequence of events contains more information about
        the cause of the operation timing out.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(TimedOutHostOperationEvent, self).__init__()
    

    
    
