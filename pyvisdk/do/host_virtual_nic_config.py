
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVirtualNicConfig(DynamicData):
    '''This data object type describes the VirtualNic configuration representing both the
        configured properties on a VirtualNic and identification information.
    '''
    
    def __init__(self, changeOperation, device, portgroup, spec):
        # MUST define these
        super(HostVirtualNicConfig, self).__init__()
    
        self.data['changeOperation'] = changeOperation
        self.data['device'] = device
        self.data['portgroup'] = portgroup
        self.data['spec'] = spec
    
    
    @property
    def changeOperation(self):
        '''The change operation to apply on this configuration specification.
        '''
        return self.data['changeOperation']

    @property
    def device(self):
        '''VirtualNic device to which configuration applies.
        '''
        return self.data['device']

    @property
    def portgroup(self):
        '''If the vnic is connecting to a vSwitch, this property is the name of portgroup
        connected. If the vnic is connecting to a DistributedVirtualSwitch, this
        property is ignored.
        '''
        return self.data['portgroup']

    @property
    def spec(self):
        '''The specification of the virtual network adapter.
        '''
        return self.data['spec']

