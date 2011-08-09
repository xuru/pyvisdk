
from pyvisdk.do.file_info import FileInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmConfigFileInfo(FileInfo):
    '''This data object type describes a virtual machine configuration file.
    '''
    
    def __init__(self, configVersion):
        # MUST define these
        super(VmConfigFileInfo, self).__init__()
    
        self.data['configVersion'] = configVersion
    
    
    @property
    def configVersion(self):
        '''
        '''
        return self.data['configVersion']

