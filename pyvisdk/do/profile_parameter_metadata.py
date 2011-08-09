
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileParameterMetadata(DynamicData):
    '''This data object represents the metadata information of a PolicyParameter
    '''
    
    def __init__(self, defaultValue, id, optional, type):
        # MUST define these
        super(ProfileParameterMetadata, self).__init__()
    
        self.data['defaultValue'] = defaultValue
        self.data['id'] = id
        self.data['optional'] = optional
        self.data['type'] = type
    
    
    @property
    def defaultValue(self):
        '''The default value that can be used for the parameter
        '''
        return self.data['defaultValue']

    @property
    def id(self):
        '''The id of the parameter
        '''
        return self.data['id']

    @property
    def optional(self):
        '''Whether the parameter is optional
        '''
        return self.data['optional']

    @property
    def type(self):
        '''The type of the parameter
        '''
        return self.data['type']

