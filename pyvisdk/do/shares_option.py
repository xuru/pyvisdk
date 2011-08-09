
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class SharesOption(DynamicData):
    '''Specification of shares.Object of this class specifies value ranges for object of
        instance SharesInfo
    '''
    
    def __init__(self, defaultLevel, sharesOption):
        # MUST define these
        super(SharesOption, self).__init__()
    
        self.data['defaultLevel'] = defaultLevel
        self.data['sharesOption'] = sharesOption
    
    
    @property
    def defaultLevel(self):
        '''Default value for level
        '''
        return self.data['defaultLevel']

    @property
    def sharesOption(self):
        '''Value range which can be used for share definition in shares
        '''
        return self.data['sharesOption']

