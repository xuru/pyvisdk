
from pyvisdk.do.virtual_machine_device_runtime_info_device_runtime_state import VirtualMachineDeviceRuntimeInfoDeviceRuntimeState
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineDeviceRuntimeInfoVirtualEthernetCardRuntimeState(VirtualMachineDeviceRuntimeInfoDeviceRuntimeState):
    '''Runtime state of a virtual ethernet card device.
    '''
    
    def __init__(self, vmDirectPathGen2Active, vmDirectPathGen2InactiveReasonExtended, vmDirectPathGen2InactiveReasonOther, vmDirectPathGen2InactiveReasonVm):
        # MUST define these
        super(VirtualMachineDeviceRuntimeInfoVirtualEthernetCardRuntimeState, self).__init__()
    
        self.data['vmDirectPathGen2Active'] = vmDirectPathGen2Active
        self.data['vmDirectPathGen2InactiveReasonExtended'] = vmDirectPathGen2InactiveReasonExtended
        self.data['vmDirectPathGen2InactiveReasonOther'] = vmDirectPathGen2InactiveReasonOther
        self.data['vmDirectPathGen2InactiveReasonVm'] = vmDirectPathGen2InactiveReasonVm
    
    
    @property
    def vmDirectPathGen2Active(self):
        '''Flag to indicate whether VMDirectPath Gen 2 is active on this device. If false,
        the reason(s) for inactivity will be provided in one or more of
        vmDirectPathGen2InactiveReasonVm, vmDirectPathGen2InactiveReasonOther, and
        vmDirectPathGen2InactiveReasonExtended.
        '''
        return self.data['vmDirectPathGen2Active']

    @property
    def vmDirectPathGen2InactiveReasonExtended(self):
        '''If vmDirectPathGen2Active is false, this property may contain an explanation
        provided by the platform, beyond the reasons (if any) enumerated in
        vmDirectPathGen2InactiveReasonVm and/or
        vmDirectPathGen2InactiveReasonOther.
        '''
        return self.data['vmDirectPathGen2InactiveReasonExtended']

    @property
    def vmDirectPathGen2InactiveReasonOther(self):
        '''If vmDirectPathGen2Active is false, this array will be populated with reasons for
        the inactivity that are not related to virtual machine state or
        configuration (chosen from VmDirectPathGen2InactiveReasonOther). Virtual
        machine related reasons for inactivity will be provided in
        vmDirectPathGen2InactiveReasonVm. If there is a reason for inactivity that
        cannot be described by the available constants,
        vmDirectPathGen2InactiveReasonExtended will be populated with an
        additional explanation provided by the platform.
        '''
        return self.data['vmDirectPathGen2InactiveReasonOther']

    @property
    def vmDirectPathGen2InactiveReasonVm(self):
        '''If vmDirectPathGen2Active is false, this array will be populated with reasons for
        the inactivity that are related to virtual machine state or configuration
        (chosen from VmDirectPathGen2InactiveReasonVm). Other reasons for
        inactivity will be provided in vmDirectPathGen2InactiveReasonOther. If
        there is a reason for inactivity that cannot be described by the available
        constants, vmDirectPathGen2InactiveReasonExtended will be populated with
        an additional explanation provided by the platform.
        '''
        return self.data['vmDirectPathGen2InactiveReasonVm']

