
from pyvisdk.do.entity_event_argument import EntityEventArgument
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class NetworkEventArgument(EntityEventArgument):
    '''The event argument is a Network object.
    '''
    
    def __init__(self, network):
        # MUST define these
        super(NetworkEventArgument, self).__init__()
    
        self.data['network'] = network
    
    
    @property
    def network(self):
        '''The Network object.
        '''
        return self.data['network']

