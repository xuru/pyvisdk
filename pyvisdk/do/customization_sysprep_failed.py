
from pyvisdk.do.customization_failed import CustomizationFailed
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationSysprepFailed(CustomizationFailed):
    '''Sysprep failed to run in the guest during customization. This will most like have
        been caused by the fact that the wrong sysprep was used for the guest, so
        we include the version information in the event.
    '''
    
    def __init__(self, sysprepVersion, systemVersion):
        # MUST define these
        super(CustomizationSysprepFailed, self).__init__()
    
        self.data['sysprepVersion'] = sysprepVersion
        self.data['systemVersion'] = systemVersion
    
    
    @property
    def sysprepVersion(self):
        '''The version string for the sysprep files that were included in the customization
        package.
        '''
        return self.data['sysprepVersion']

    @property
    def systemVersion(self):
        '''The version string for the system
        '''
        return self.data['systemVersion']

