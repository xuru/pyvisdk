
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmConfigFileQueryFilter(DynamicData):
    '''The filter for the virtual machine configuration file.
    '''
    
    def __init__(self, matchConfigVersion):
        # MUST define these
        super(VmConfigFileQueryFilter, self).__init__()
    
        self.data['matchConfigVersion'] = matchConfigVersion
    
    
    @property
    def matchConfigVersion(self):
        '''If this property is set, only the virtual machine configuration files that match
        one of the specified configuration versions are selected. If no versions
        are specified, this search criteria is ignored.
        '''
        return self.data['matchConfigVersion']

