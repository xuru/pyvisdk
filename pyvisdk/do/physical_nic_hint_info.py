
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PhysicalNicHintInfo(DynamicData):
    '''The NetworkHint data object type is some information about the network to which
        the physical network adapter is attached.
    '''
    
    def __init__(self, connectedSwitchPort, device, network, subnet):
        # MUST define these
        super(PhysicalNicHintInfo, self).__init__()
    
        self.data['connectedSwitchPort'] = connectedSwitchPort
        self.data['device'] = device
        self.data['network'] = network
        self.data['subnet'] = subnet
    
    
    @property
    def connectedSwitchPort(self):
        '''If the uplink is directly connects to a CDP-awared network device and the device's
        CDP broadcast is enabled, this property will be set to return the CDP
        information that vmkernel received on this PNIC. CDP data contains the
        device information and port ID that the PNIC connects to. If the uplink is
        not connecting to a CDP-awared device or CDP is not enabled on the device,
        this property will be unset. PhysicalNicCdpInfo
        '''
        return self.data['connectedSwitchPort']

    @property
    def device(self):
        '''The physical network adapter device to which this hint applies.
        '''
        return self.data['device']

    @property
    def network(self):
        '''The list of network names that were detected on this physical network adapter.
        '''
        return self.data['network']

    @property
    def subnet(self):
        '''The list of subnets that were detected on this physical network adapter.
        '''
        return self.data['subnet']

