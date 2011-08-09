
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VMwareDVSPvlanMapEntry(DynamicData):
    '''The class represents a PVLAN id.
    '''
    
    def __init__(self, primaryVlanId, pvlanType, secondaryVlanId):
        # MUST define these
        super(VMwareDVSPvlanMapEntry, self).__init__()
    
        self.data['primaryVlanId'] = primaryVlanId
        self.data['pvlanType'] = pvlanType
        self.data['secondaryVlanId'] = secondaryVlanId
    
    
    @property
    def primaryVlanId(self):
        '''The primary VLAN ID. The VLAN IDs of 0 and 4095 are reserved and cannot be used in
        this property.
        '''
        return self.data['primaryVlanId']

    @property
    def pvlanType(self):
        '''The type of PVLAN. See VmwareDistributedVirtualSwitchPvlanPortType for valid
        values.
        '''
        return self.data['pvlanType']

    @property
    def secondaryVlanId(self):
        '''The secondary VLAN ID. The VLAN IDs of 0 and 4095 are reserved and cannot be used
        in this property.
        '''
        return self.data['secondaryVlanId']

