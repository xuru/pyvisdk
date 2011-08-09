
from pyvisdk.do.entity_event_argument import EntityEventArgument
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DatacenterEventArgument(EntityEventArgument):
    '''The event argument is a Datacenter object.
    '''
    
    def __init__(self, datacenter):
        # MUST define these
        super(DatacenterEventArgument, self).__init__()
    
        self.data['datacenter'] = datacenter
    
    
    @property
    def datacenter(self):
        '''The Datacenter object.
        '''
        return self.data['datacenter']

