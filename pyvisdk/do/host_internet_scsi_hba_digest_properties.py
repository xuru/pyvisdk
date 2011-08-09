
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostInternetScsiHbaDigestProperties(DynamicData):
    '''The digest settings for this host bus adapter.
    '''
    
    def __init__(self, dataDigestInherited, dataDigestType, headerDigestInherited, headerDigestType):
        # MUST define these
        super(HostInternetScsiHbaDigestProperties, self).__init__()
    
        self.data['dataDigestInherited'] = dataDigestInherited
        self.data['dataDigestType'] = dataDigestType
        self.data['headerDigestInherited'] = headerDigestInherited
        self.data['headerDigestType'] = headerDigestType
    
    
    @property
    def dataDigestInherited(self):
        '''Data digest setting is inherited
        '''
        return self.data['dataDigestInherited']

    @property
    def dataDigestType(self):
        '''The data digest preference if data digest is enabled
        '''
        return self.data['dataDigestType']

    @property
    def headerDigestInherited(self):
        '''Header digest setting is inherited
        '''
        return self.data['headerDigestInherited']

    @property
    def headerDigestType(self):
        '''The header digest preference if header digest is enabled
        '''
        return self.data['headerDigestType']

