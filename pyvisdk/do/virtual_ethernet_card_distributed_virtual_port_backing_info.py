
from pyvisdk.do.virtual_device_backing_info import VirtualDeviceBackingInfo
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualEthernetCardDistributedVirtualPortBackingInfo(VirtualDeviceBackingInfo):
    '''The class defines a VirtualEthernetCard backing that connects the device to a
        distributed virtual switch port or portgroup.
    '''
    
    def __init__(self, port):
        # MUST define these
        super(VirtualEthernetCardDistributedVirtualPortBackingInfo, self).__init__()
    
        self.data['port'] = port
    
    
    @property
    def port(self):
        '''The DistributedVirtualPort or DistributedVirtualPortgroup connection. To specify a
        port connection, set this property to a
        DistributedVirtualSwitchPortConnection object. To specific a portgroup
        connection, set this property to a DistributedVirtualSwitchPortConnection
        object.
        '''
        return self.data['port']

