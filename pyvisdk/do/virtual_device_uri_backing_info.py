
from pyvisdk.do.virtual_device_backing_info import VirtualDeviceBackingInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDeviceURIBackingInfo(VirtualDeviceBackingInfo):
    '''The data object type defines information for using a network socket as backing for
        a virtual device.
    '''
    
    def __init__(self, direction, proxyURI, serviceURI):
        # MUST define these
        super(VirtualDeviceURIBackingInfo, self).__init__()
    
        self.data['direction'] = direction
        self.data['proxyURI'] = proxyURI
        self.data['serviceURI'] = serviceURI
    
    
    @property
    def direction(self):
        '''The direction of the connection. For possible values see
        VirtualDeviceURIBackingOptionDirection
        '''
        return self.data['direction']

    @property
    def proxyURI(self):
        '''Identifies a proxy service that provides network access to the
        '''
        return self.data['proxyURI']

    @property
    def serviceURI(self):
        '''Identifies the local host or a system on the network, depending on the value of
        '''
        return self.data['serviceURI']

