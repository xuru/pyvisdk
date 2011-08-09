
from pyvisdk.do.entity_event_argument import EntityEventArgument
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DvsEventArgument(EntityEventArgument):
    '''The event argument is a Host object.
    '''
    
    def __init__(self, dvs):
        # MUST define these
        super(DvsEventArgument, self).__init__()
    
        self.data['dvs'] = dvs
    
    
    @property
    def dvs(self):
        '''The distributed virtual switch object.
        '''
        return self.data['dvs']

