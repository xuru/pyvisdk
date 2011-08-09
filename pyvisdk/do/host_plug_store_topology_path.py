
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPlugStoreTopologyPath(DynamicData):
    '''This data object type is an association class that describes a Path and its
        associated Device. A Path may be claimed by at most one Device.
    '''
    
    def __init__(self, adapter, channelNumber, device, key, lunNumber, name, target, targetNumber):
        # MUST define these
        super(HostPlugStoreTopologyPath, self).__init__()
    
        self.data['adapter'] = adapter
        self.data['channelNumber'] = channelNumber
        self.data['device'] = device
        self.data['key'] = key
        self.data['lunNumber'] = lunNumber
        self.data['name'] = name
        self.data['target'] = target
        self.data['targetNumber'] = targetNumber
    
    
    @property
    def adapter(self):
        '''The adapter that provided the Path.
        '''
        return self.data['adapter']

    @property
    def channelNumber(self):
        '''The channel number for a path if applicable.
        '''
        return self.data['channelNumber']

    @property
    def device(self):
        '''The device that claimed the Path if any.
        '''
        return self.data['device']

    @property
    def key(self):
        '''The identifier for the Path.
        '''
        return self.data['key']

    @property
    def lunNumber(self):
        '''The LUN number for a path if applicable.
        '''
        return self.data['lunNumber']

    @property
    def name(self):
        '''Name of path. Use this property to correlate this path object to other path
        objects.
        '''
        return self.data['name']

    @property
    def target(self):
        '''The target of the Path if any.
        '''
        return self.data['target']

    @property
    def targetNumber(self):
        '''The target number for a path if applicable. The target number is not guaranteed to
        be consistent across reboots or rescans of the adapter.
        '''
        return self.data['targetNumber']

