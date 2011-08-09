
from pyvisdk.do.host_host_bus_adapter import HostHostBusAdapter
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostFibreChannelHba(HostHostBusAdapter):
    '''This data object type describes the Fibre Channel host bus adapter.
    '''
    
    def __init__(self, nodeWorldWideName, portType, portWorldWideName, speed):
        # MUST define these
        super(HostFibreChannelHba, self).__init__()
    
        self.data['nodeWorldWideName'] = nodeWorldWideName
        self.data['portType'] = portType
        self.data['portWorldWideName'] = portWorldWideName
        self.data['speed'] = speed
    
    
    @property
    def nodeWorldWideName(self):
        '''The world wide node name for the adapter.
        '''
        return self.data['nodeWorldWideName']

    @property
    def portType(self):
        '''The type of the fiber channel port.
        '''
        return self.data['portType']

    @property
    def portWorldWideName(self):
        '''The world wide port name for the adapter.
        '''
        return self.data['portWorldWideName']

    @property
    def speed(self):
        '''The current operating speed of the adapter in bits per second.
        '''
        return self.data['speed']

