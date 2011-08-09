
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmAcquiredTicketEvent(VmEvent):
    '''This event records a user successfully acquiring a ticket
    '''
    
    def __init__(self, ticketType):
        # MUST define these
        super(VmAcquiredTicketEvent, self).__init__()
    
        self.data['ticketType'] = ticketType
    
    
    @property
    def ticketType(self):
        '''The type of the ticket
        '''
        return self.data['ticketType']

