
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationLicenseFilePrintData(DynamicData):
    '''The LicenseFilePrintData type maps directly to the LicenseFilePrintData key in the
        answer file. These values are transferred into the file that VirtualCenter
        stores on the target virtual disk. For more detailed information, see the
        document . LicenseFilePrintData provides licensing information for Windows
        server operating systems.
    '''
    
    def __init__(self, autoMode, autoUsers):
        # MUST define these
        super(CustomizationLicenseFilePrintData, self).__init__()
    
        self.data['autoMode'] = autoMode
        self.data['autoUsers'] = autoUsers
    
    
    @property
    def autoMode(self):
        '''Server licensing mode
        '''
        return self.data['autoMode']

    @property
    def autoUsers(self):
        '''This key is valid only if AutoMode = PerServer. The integer value indicates the
        number of client licenses purchased for the VirtualCenter server being
        installed.
        '''
        return self.data['autoUsers']

