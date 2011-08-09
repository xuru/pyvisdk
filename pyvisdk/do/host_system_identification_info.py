
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostSystemIdentificationInfo(DynamicData):
    '''This data object describes system identifying information of the host. This
        information may be vendor specific.
    '''
    
    def __init__(self, identifierType, identifierValue):
        # MUST define these
        super(HostSystemIdentificationInfo, self).__init__()
    
        self.data['identifierType'] = identifierType
        self.data['identifierValue'] = identifierValue
    
    
    @property
    def identifierType(self):
        '''The description of the identifying information.
        '''
        return self.data['identifierType']

    @property
    def identifierValue(self):
        '''The system identification information
        '''
        return self.data['identifierValue']

