
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDigestInfo(DynamicData):
    '''This data object type describes the digest information
    '''
    
    def __init__(self, digestMethod, digestValue, objectName):
        # MUST define these
        super(HostDigestInfo, self).__init__()
    
        self.data['digestMethod'] = digestMethod
        self.data['digestValue'] = digestValue
        self.data['objectName'] = objectName
    
    
    @property
    def digestMethod(self):
        '''Method in which the digest value is calculated. The set of possible values is
        described in HostDigestInfoDigestMethodType.
        '''
        return self.data['digestMethod']

    @property
    def digestValue(self):
        '''The variable length byte array containing the digest value calculated by the
        specified digestMethod.
        '''
        return self.data['digestValue']

    @property
    def objectName(self):
        '''The name of the object from which this digest value is calcaulated.
        '''
        return self.data['objectName']

