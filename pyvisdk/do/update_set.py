
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class UpdateSet(DynamicData):
    '''A set of updates that represent the changes since a prior call to CheckForUpdates,
        WaitForUpdates, or WaitForUpdatesEx.
    '''
    
    def __init__(self, filterSet, truncated, version):
        # MUST define these
        super(UpdateSet, self).__init__()
    
        self.data['filterSet'] = filterSet
        self.data['truncated'] = truncated
        self.data['version'] = version
    
    
    @property
    def filterSet(self):
        '''Set of managed object updates detected by specific filters. Updates are reported
        in sets. Each set is associated with a reference to a filter that detected
        the updates in the set.
        '''
        return self.data['filterSet']

    @property
    def truncated(self):
        '''If true, this UpdateSet contains results from a suspended change calculation,
        which places restrictions on the use of version.
        '''
        return self.data['truncated']

    @property
    def version(self):
        '''New data version to pass in the next call to CheckForUpdates, WaitForUpdates, or
        WaitForUpdatesEx. These versions, although they are opaque, are strongly
        ordered in the sense that passing a version to WaitForUpdates,
        CheckForUpdates or WaitForUpdatesEx requests updates that reflect changes
        in the objects selected by the Filter that happened after the specified
        version.
        '''
        return self.data['version']

