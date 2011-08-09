
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmConfigFileQueryFlags(DynamicData):
    '''
    '''
    
    def __init__(self, configVersion):
        # MUST define these
        super(VmConfigFileQueryFlags, self).__init__()
    
        self.data['configVersion'] = configVersion
    
    
    @property
    def configVersion(self):
        '''The flag to indicate whether or not the configuration file version number is
        returned.
        '''
        return self.data['configVersion']

