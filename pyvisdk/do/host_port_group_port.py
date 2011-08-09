
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPortGroupPort(DynamicData):
    '''A Port data object type is a runtime representation of network connectivity
        between a network service or virtual machine and a virtual switch. This is
        different from a port group in that the port group represents the
        configuration aspects of the network connection. The Port object provides
        runtime statistics.
    '''
    
    def __init__(self, key, mac, type):
        # MUST define these
        super(HostPortGroupPort, self).__init__()
    
        self.data['key'] = key
        self.data['mac'] = mac
        self.data['type'] = type
    
    
    @property
    def key(self):
        '''The linkable identifier.
        '''
        return self.data['key']

    @property
    def mac(self):
        '''The Media Access Control (MAC) address of network service of the virtual machine
        connected on this port.
        '''
        return self.data['mac']

    @property
    def type(self):
        '''The type of component connected on this port. Must be one of the values of
        PortGroupConnecteeType.
        '''
        return self.data['type']

