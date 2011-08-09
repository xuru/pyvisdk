
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationSpecInfo(DynamicData):
    '''Information about a specification.
    '''
    
    def __init__(self, changeVersion, description, lastUpdateTime, name, type):
        # MUST define these
        super(CustomizationSpecInfo, self).__init__()
    
        self.data['changeVersion'] = changeVersion
        self.data['description'] = description
        self.data['lastUpdateTime'] = lastUpdateTime
        self.data['name'] = name
        self.data['type'] = type
    
    
    @property
    def changeVersion(self):
        '''The changeVersion is a unique identifier for a given version of the configuration.
        Each change to the configuration will update this value. This is typically
        implemented as an ever increasing count or a time-stamp. However, a client
        should always treat this as an opaque string.
        '''
        return self.data['changeVersion']

    @property
    def description(self):
        '''Description of the specification.
        '''
        return self.data['description']

    @property
    def lastUpdateTime(self):
        '''Time when the specification was last modified. This time is ignored when the
        CustomizationSpecItem containing this is used as an input to
        CustomizationSpecManager.create.
        '''
        return self.data['lastUpdateTime']

    @property
    def name(self):
        '''Unique name of the specification.
        '''
        return self.data['name']

    @property
    def type(self):
        '''Guest operating system for this specification (Linux or Windows).
        '''
        return self.data['type']

