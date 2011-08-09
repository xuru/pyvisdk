
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVirtualNicSpec(DynamicData):
    '''This data object type describes the VirtualNic configuration containing both the
        configured properties on a VirtualNic and identification information.
    '''
    
    def __init__(self, distributedVirtualPort, ip, mac, mtu, portgroup, tsoEnabled):
        # MUST define these
        super(HostVirtualNicSpec, self).__init__()
    
        self.data['distributedVirtualPort'] = distributedVirtualPort
        self.data['ip'] = ip
        self.data['mac'] = mac
        self.data['mtu'] = mtu
        self.data['portgroup'] = portgroup
        self.data['tsoEnabled'] = tsoEnabled
    
    
    @property
    def distributedVirtualPort(self):
        '''The DistributedVirtualPort that is connected to the vnic.
        '''
        return self.data['distributedVirtualPort']

    @property
    def ip(self):
        '''The IP configuration on the virtual network adapter.
        '''
        return self.data['ip']

    @property
    def mac(self):
        '''The media access control (MAC) address of the virtual network adapter.
        '''
        return self.data['mac']

    @property
    def mtu(self):
        '''The maximum transmission unit for packets size in bytes for the virtual nic. This
        property is applicable to vmkernel virtual nics and will be ignored if
        specified for service console virtual nics. If not specified, the system
        default value shall be used.
        '''
        return self.data['mtu']

    @property
    def portgroup(self):
        '''The Portgroup to which the Vnic connects. While reconfiguring a virtual nic, this
        field indicates the new portgroup the virtualnic should connect to. This
        can be specified only if distributedVirtualPort is not specified.
        '''
        return self.data['portgroup']

    @property
    def tsoEnabled(self):
        '''Flag enabling or disabling tcp segmentation offset for a virtual nic. This
        property is applicable to vmkernel virtual nics and will be ignored if
        specified for service console vitual nics. If not specified, a default
        value of true shall be used.
        '''
        return self.data['tsoEnabled']

