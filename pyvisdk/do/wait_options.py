
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class WaitOptions(DynamicData):
    '''Options for WaitForUpdatesEx.
    '''
    
    def __init__(self, maxObjectUpdates, maxWaitSeconds):
        # MUST define these
        super(WaitOptions, self).__init__()
    
        self.data['maxObjectUpdates'] = maxObjectUpdates
        self.data['maxWaitSeconds'] = maxWaitSeconds
    
    
    @property
    def maxObjectUpdates(self):
        '''The maximum number of ObjectUpdate entries that should be returned in a single
        result from WaitForUpdatesEx. See truncated
        '''
        return self.data['maxObjectUpdates']

    @property
    def maxWaitSeconds(self):
        '''The number of seconds the PropertyCollector should wait before returning null.
        Returning updates may take longer if the actual calculation time exceeds
        maxWaitSeconds. Additionally PropertyCollector policy may cause it to
        return null sooner than maxWaitSeconds.
        '''
        return self.data['maxWaitSeconds']

