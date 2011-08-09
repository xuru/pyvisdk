
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostBIOSInfo(DynamicData):
    '''
    '''
    
    def __init__(self, biosVersion, releaseDate):
        # MUST define these
        super(HostBIOSInfo, self).__init__()
    
        self.data['biosVersion'] = biosVersion
        self.data['releaseDate'] = releaseDate
    
    
    @property
    def biosVersion(self):
        '''The current BIOS version of the physical chassis
        '''
        return self.data['biosVersion']

    @property
    def releaseDate(self):
        '''The release date for the BIOS.
        '''
        return self.data['releaseDate']

