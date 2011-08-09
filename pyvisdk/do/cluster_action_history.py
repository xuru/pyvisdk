
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterActionHistory(DynamicData):
    '''Base class for all action history.
    '''
    
    def __init__(self, action, time):
        # MUST define these
        super(ClusterActionHistory, self).__init__()
    
        self.data['action'] = action
        self.data['time'] = time
    
    
    @property
    def action(self):
        '''The action that was executed recently.
        '''
        return self.data['action']

    @property
    def time(self):
        '''The time when the action was executed.
        '''
        return self.data['time']

