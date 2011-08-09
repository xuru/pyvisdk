
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostMultipathStateInfoPath(DynamicData):
    '''Data object indicating state of storage path for a named path.
    '''
    
    def __init__(self, name, pathState):
        # MUST define these
        super(HostMultipathStateInfoPath, self).__init__()
    
        self.data['name'] = name
        self.data['pathState'] = pathState
    
    
    @property
    def name(self):
        '''Name of path.
        '''
        return self.data['name']

    @property
    def pathState(self):
        '''The state of the path. Must be one of the values of MultipathState.
        '''
        return self.data['pathState']

