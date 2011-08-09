
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PhysicalNicCdpDeviceCapability(DynamicData):
    '''The capability of the CDP-awared device that connects to a PNIC.
        PhysicalNicCdpInfo
    '''
    
    def __init__(self, host, igmpEnabled, networkSwitch, repeater, router, sourceRouteBridge, transparentBridge):
        # MUST define these
        super(PhysicalNicCdpDeviceCapability, self).__init__()
    
        self.data['host'] = host
        self.data['igmpEnabled'] = igmpEnabled
        self.data['networkSwitch'] = networkSwitch
        self.data['repeater'] = repeater
        self.data['router'] = router
        self.data['sourceRouteBridge'] = sourceRouteBridge
        self.data['transparentBridge'] = transparentBridge
    
    
    @property
    def host(self):
        '''The CDP-awared device has the capability of a host, which Sends and receives
        packets for at least one network layer protocol.
        '''
        return self.data['host']

    @property
    def igmpEnabled(self):
        '''The CDP-awared device is IGMP-enabled, which does not forward IGMP Report packets
        on nonrouter ports.
        '''
        return self.data['igmpEnabled']

    @property
    def networkSwitch(self):
        '''The CDP-awared device has the capability of switching. The difference between this
        capability and transparentBridge is that a switch does not run the
        Spanning-Tree Protocol. This device is assumed to be deployed in a
        physical loop-free topology.
        '''
        return self.data['networkSwitch']

    @property
    def repeater(self):
        '''The CDP-awared device has the capability of a repeater
        '''
        return self.data['repeater']

    @property
    def router(self):
        '''The CDP-awared device has the capability of a routing for at least one network
        layer protocol
        '''
        return self.data['router']

    @property
    def sourceRouteBridge(self):
        '''The CDP-awared device has the capability of source-route bridging
        '''
        return self.data['sourceRouteBridge']

    @property
    def transparentBridge(self):
        '''The CDP-awared device has the capability of transparent bridging
        '''
        return self.data['transparentBridge']

