
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ExtensionFaultTypeInfo(DynamicData):
    '''This data object type describes fault types defined by the extension.
    '''
    
    def __init__(self, faultID):
        # MUST define these
        super(ExtensionFaultTypeInfo, self).__init__()
    
        self.data['faultID'] = faultID
    
    
    @property
    def faultID(self):
        '''The ID of the fault type. Should follow java package naming conventions for
        uniqueness.
        '''
        return self.data['faultID']

