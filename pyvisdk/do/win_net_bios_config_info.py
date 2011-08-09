
from pyvisdk.do.net_bios_config_info import NetBIOSConfigInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class WinNetBIOSConfigInfo(NetBIOSConfigInfo):
    '''This data object type describes the Windows-specific NetBIOS configuration.
    '''
    
    def __init__(self, primaryWINS, secondaryWINS):
        # MUST define these
        super(WinNetBIOSConfigInfo, self).__init__()
    
        self.data['primaryWINS'] = primaryWINS
        self.data['secondaryWINS'] = secondaryWINS
    
    
    @property
    def primaryWINS(self):
        '''The IP address of the primary WINS server.
        '''
        return self.data['primaryWINS']

    @property
    def secondaryWINS(self):
        '''The IP address of the secondary WINS server.
        '''
        return self.data['secondaryWINS']

