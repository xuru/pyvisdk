
from pyvisdk.do.host_das_event import HostDasEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPrimaryAgentNotShortNameEvent(HostDasEvent):
    '''This event records that the primary agent specified is not a short name. The name
        of the primary agent is usually stored as a short name. You should not
        normally see this error. Please check the network configurations of your
        hosts.
    '''
    
    def __init__(self, primaryAgent):
        # MUST define these
        super(HostPrimaryAgentNotShortNameEvent, self).__init__()
    
        self.data['primaryAgent'] = primaryAgent
    
    
    @property
    def primaryAgent(self):
        '''
        '''
        return self.data['primaryAgent']

