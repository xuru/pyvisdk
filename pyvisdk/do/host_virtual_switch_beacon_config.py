
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVirtualSwitchBeaconConfig(DynamicData):
    '''This data object type describes the configuration of the beacon to probe
        connectivity of physical network adapters. A beacon is sent out of one
        network adapter and should arrive on another network adapter in the team.
        The successful roundtrip indicates that the network adapters are
        working.Define this data object to enable beacon probing as a method to
        validate the link status of a physical network adapter. Beacon probing
        must be configured in order to use the beacon status as a criteria to
        determine if a physical network adapter failed. See checkBeacon
    '''
    
    def __init__(self, interval):
        # MUST define these
        super(HostVirtualSwitchBeaconConfig, self).__init__()
    
        self.data['interval'] = interval
    
    
    @property
    def interval(self):
        '''Determines how often, in seconds, a beacon should be sent.
        '''
        return self.data['interval']

