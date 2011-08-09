
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CanceledHostOperationEvent(HostEvent):
    '''An operation performed on the host was canceled. Typically, a previous event in
        the sequence of events contains more information about the cause of this
        cancellation.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(CanceledHostOperationEvent, self).__init__()
    

    
    
