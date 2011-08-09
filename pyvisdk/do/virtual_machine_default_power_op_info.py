
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineDefaultPowerOpInfo(DynamicData):
    '''The DefaultPowerOpInfo data object type holds the configured defaults for the
        power operations on a virtual machine. The properties indicated whether to
        do a "soft" or guest initiated operation, or a "hard" operation.
    '''
    
    def __init__(self, defaultPowerOffType, defaultResetType, defaultSuspendType, powerOffType, resetType, standbyAction, suspendType):
        # MUST define these
        super(VirtualMachineDefaultPowerOpInfo, self).__init__()
    
        self.data['defaultPowerOffType'] = defaultPowerOffType
        self.data['defaultResetType'] = defaultResetType
        self.data['defaultSuspendType'] = defaultSuspendType
        self.data['powerOffType'] = powerOffType
        self.data['resetType'] = resetType
        self.data['standbyAction'] = standbyAction
        self.data['suspendType'] = suspendType
    
    
    @property
    def defaultPowerOffType(self):
        '''Default operation for power off: soft or hard
        '''
        return self.data['defaultPowerOffType']

    @property
    def defaultResetType(self):
        '''Default operation for reset: soft or hard
        '''
        return self.data['defaultResetType']

    @property
    def defaultSuspendType(self):
        '''Default operation for suspend: soft or hard
        '''
        return self.data['defaultSuspendType']

    @property
    def powerOffType(self):
        '''Describes the default power off type for this virtual machine. The possible values
        are specified by the PowerOpType. * hard - Perform power off by using the
        PowerOff method. * soft - Perform power off by using the ShutdownGuest
        method. * preset - The preset value is specified in the
        defaultPowerOffType section. This setting is advisory and clients can
        choose to ignore it.
        '''
        return self.data['powerOffType']

    @property
    def resetType(self):
        '''Describes the default reset type for this virtual machine. The possible values are
        specified by the PowerOpType. * hard - Perform reset by using the Reset
        method. * soft - Perform reset by using the RebootGuest method. * preset -
        The preset value is specified in the defaultResetType section. This
        setting is advisory and clients can choose to ignore it.
        '''
        return self.data['resetType']

    @property
    def standbyAction(self):
        '''Behavior of virtual machine when it receives the S1 ACPI call.
        '''
        return self.data['standbyAction']

    @property
    def suspendType(self):
        '''Describes the default suspend type for this virtual machine. The possible values
        are specified by the PowerOpType. * hard - Perform suspend by using the
        Suspend method. * soft - Perform suspend by using the StandbyGuest method.
        * preset - The preset value is specified in the defaultSuspendType
        section. This setting is advisory and clients can choose to ignore it.
        '''
        return self.data['suspendType']

