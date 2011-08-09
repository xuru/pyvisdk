
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OvfNetworkInfo(DynamicData):
    '''The name and description of a network as specified by the OVF descriptor.
    '''
    
    def __init__(self, description, name):
        # MUST define these
        super(OvfNetworkInfo, self).__init__()
    
        self.data['description'] = description
        self.data['name'] = name
    
    
    @property
    def description(self):
        '''
        '''
        return self.data['description']

    @property
    def name(self):
        '''
        '''
        return self.data['name']

