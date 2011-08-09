
from pyvisdk.do.type_description import TypeDescription
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ScheduledTaskDetail(TypeDescription):
    '''Descriptive detail for each scheduler type.
    '''
    
    def __init__(self, frequency):
        # MUST define these
        super(ScheduledTaskDetail, self).__init__()
    
        self.data['frequency'] = frequency
    
    
    @property
    def frequency(self):
        '''Scheduler frequency description.
        '''
        return self.data['frequency']

