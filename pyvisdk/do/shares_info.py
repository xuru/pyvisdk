
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class SharesInfo(DynamicData):
    '''Specification of shares.Shares are used to determine relative allocation between
        resource consumers. In general, a consumer with more shares gets
        proportionally more of the resource, subject to certain other constraints.
    '''
    
    def __init__(self, level, shares):
        # MUST define these
        super(SharesInfo, self).__init__()
    
        self.data['level'] = level
        self.data['shares'] = shares
    
    
    @property
    def level(self):
        '''The allocation level. The level is a simplified view of shares. Levels map to a
        pre-determined set of numeric values for shares. If the shares value does
        not map to a predefined size, then the level is set as custom.
        '''
        return self.data['level']

    @property
    def shares(self):
        '''The number of shares allocated. Used to determine resource allocation in case of
        resource contention. This value is only set if level is set to custom. If
        level is not set to custom, this value is ignored. Therefore, only shares
        with custom values can be compared.
        '''
        return self.data['shares']

