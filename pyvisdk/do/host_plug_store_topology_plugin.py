
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPlugStoreTopologyPlugin(DynamicData):
    '''This data object type represents a Plugin in the plug store architecture. A Plugin
        claims a set of paths and groups them into Devices.
    '''
    
    def __init__(self, claimedPath, device, key, name):
        # MUST define these
        super(HostPlugStoreTopologyPlugin, self).__init__()
    
        self.data['claimedPath'] = claimedPath
        self.data['device'] = device
        self.data['key'] = key
        self.data['name'] = name
    
    
    @property
    def claimedPath(self):
        '''The set of paths claimed by this plugin. Not every claimed path will necessarily
        appear as part of a Device. Claimed paths will only appear under Devices
        if the device identifier of the path matches up with the device identifier
        exposed by the Device.
        '''
        return self.data['claimedPath']

    @property
    def device(self):
        '''The set of devices formed by this plugin.
        '''
        return self.data['device']

    @property
    def key(self):
        '''The identifier of the plugin.
        '''
        return self.data['key']

    @property
    def name(self):
        '''The name of the plugin.
        '''
        return self.data['name']

