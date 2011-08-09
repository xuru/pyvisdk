
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostCpuPackage(DynamicData):
    '''Information about a physical CPU package.
    '''
    
    def __init__(self, busHz, cpuFeature, description, hz, index, threadId, vendor):
        # MUST define these
        super(HostCpuPackage, self).__init__()
    
        self.data['busHz'] = busHz
        self.data['cpuFeature'] = cpuFeature
        self.data['description'] = description
        self.data['hz'] = hz
        self.data['index'] = index
        self.data['threadId'] = threadId
        self.data['vendor'] = vendor
    
    
    @property
    def busHz(self):
        '''Bus speed in HZ.
        '''
        return self.data['busHz']

    @property
    def cpuFeature(self):
        '''The CPU feature bit on this particular CPU. This is independent of the product and
        licensing capabilities.
        '''
        return self.data['cpuFeature']

    @property
    def description(self):
        '''String summary description of CPU (for display purposes).
        '''
        return self.data['description']

    @property
    def hz(self):
        '''CPU speed in HZ.
        '''
        return self.data['hz']

    @property
    def index(self):
        '''Package index, starting from zero.
        '''
        return self.data['index']

    @property
    def threadId(self):
        '''The logical CPU threads on this package.
        '''
        return self.data['threadId']

    @property
    def vendor(self):
        '''CPU vendor name, possible names currently are "Intel", "AMD", or "unknown".
        '''
        return self.data['vendor']

