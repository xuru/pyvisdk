
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostNetOffloadCapabilities(DynamicData):
    '''Offload capabilities are used to optimize virtual machine network performance.
        When a virtual machine is transmitting on a network, some operations can
        be offloaded either to the host or to physical hardware. This data object
        type defines the set of offload capabilities that may be available on a
        host.This data object type is used both to publish the list of offload
        capabilities and to contain offload capability policy settings. The
        network policy logic is built on a two-level inheritance scheme which
        requires that all settings be optional. As a result, all properties on the
        NetOffloadCapabilities object must be optional. See HostNetworkPolicy
    '''
    
    def __init__(self, csumOffload, tcpSegmentation, zeroCopyXmit):
        # MUST define these
        super(HostNetOffloadCapabilities, self).__init__()
    
        self.data['csumOffload'] = csumOffload
        self.data['tcpSegmentation'] = tcpSegmentation
        self.data['zeroCopyXmit'] = zeroCopyXmit
    
    
    @property
    def csumOffload(self):
        '''(Optional) The flag to indicate whether or not checksum offloading is supported.
        '''
        return self.data['csumOffload']

    @property
    def tcpSegmentation(self):
        '''(Optional) The flag to indicate whether or not TCP segmentation offloading (TSO)
        is supported.
        '''
        return self.data['tcpSegmentation']

    @property
    def zeroCopyXmit(self):
        '''(Optional) The flag to indicate whether or not zero copy transmits are supported.
        '''
        return self.data['zeroCopyXmit']

