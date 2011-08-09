
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VimAccountPasswordChangedEvent(HostEvent):
    '''Password for the Vim account user on the host has been changed. This is an account
        created by VirtualCenter and used to manage the host.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(VimAccountPasswordChangedEvent, self).__init__()
    

    
    
