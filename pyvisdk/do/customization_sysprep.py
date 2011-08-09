
from pyvisdk.do.customization_identity_settings import CustomizationIdentitySettings
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationSysprep(CustomizationIdentitySettings):
    '''An object representation of a Windows answer file. The sysprep type encloses all
        the individual keys listed in a file. For more detailed information, see
        the document .
    '''
    
    def __init__(self, guiRunOnce, guiUnattended, identification, licenseFilePrintData, userData):
        # MUST define these
        super(CustomizationSysprep, self).__init__()
    
        self.data['guiRunOnce'] = guiRunOnce
        self.data['guiUnattended'] = guiUnattended
        self.data['identification'] = identification
        self.data['licenseFilePrintData'] = licenseFilePrintData
        self.data['userData'] = userData
    
    
    @property
    def guiRunOnce(self):
        '''An object representation of the sysprep GuiRunOnce key.
        '''
        return self.data['guiRunOnce']

    @property
    def guiUnattended(self):
        '''An object representation of the sysprep GuiUnattended key.
        '''
        return self.data['guiUnattended']

    @property
    def identification(self):
        '''An object representation of the sysprep Identification key.
        '''
        return self.data['identification']

    @property
    def licenseFilePrintData(self):
        '''An object representation of the sysprep LicenseFilePrintData key. Required only
        for Windows 2000 Server and Windows Server 2003.
        '''
        return self.data['licenseFilePrintData']

    @property
    def userData(self):
        '''An object representation of the sysprep UserData key.
        '''
        return self.data['userData']

