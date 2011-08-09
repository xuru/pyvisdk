
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ComplianceFailure(DynamicData):
    '''
    '''
    
    def __init__(self, expressionName, failureType, message):
        # MUST define these
        super(ComplianceFailure, self).__init__()
    
        self.data['expressionName'] = expressionName
        self.data['failureType'] = failureType
        self.data['message'] = message
    
    
    @property
    def expressionName(self):
        '''Name of the Expression which generated the ComplianceFailure
        '''
        return self.data['expressionName']

    @property
    def failureType(self):
        '''String uniquely identifying the failure.
        '''
        return self.data['failureType']

    @property
    def message(self):
        '''Message which describes the compliance failures message.key serves as a key to the
        localized message catalog.
        '''
        return self.data['message']

