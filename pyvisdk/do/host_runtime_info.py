
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostRuntimeInfo(DynamicData):
    '''This data object type describes the runtime state of a host.
    '''
    
    def __init__(self, bootTime, connectionState, healthSystemRuntime, inMaintenanceMode, powerState, standbyMode, tpmPcrValues):
        # MUST define these
        super(HostRuntimeInfo, self).__init__()
    
        self.data['bootTime'] = bootTime
        self.data['connectionState'] = connectionState
        self.data['healthSystemRuntime'] = healthSystemRuntime
        self.data['inMaintenanceMode'] = inMaintenanceMode
        self.data['powerState'] = powerState
        self.data['standbyMode'] = standbyMode
        self.data['tpmPcrValues'] = tpmPcrValues
    
    
    @property
    def bootTime(self):
        '''The time when the host was booted.
        '''
        return self.data['bootTime']

    @property
    def connectionState(self):
        '''The host connection state. See the description in the enums for the
        ConnectionState data object type.
        '''
        return self.data['connectionState']

    @property
    def healthSystemRuntime(self):
        '''Available system health status
        '''
        return self.data['healthSystemRuntime']

    @property
    def inMaintenanceMode(self):
        '''The flag to indicate whether or not the host is in maintenance mode. This flag is
        set when the host has entered the maintenance mode. It is not set during
        the entering phase of maintenance mode.
        '''
        return self.data['inMaintenanceMode']

    @property
    def powerState(self):
        '''The host power state. See the description in the enums for the PowerState data
        object type.
        '''
        return self.data['powerState']

    @property
    def standbyMode(self):
        '''The host's standby mode. For valid values see HostStandbyMode. The property is
        only populated by vCenter server. If queried directly from a ESX host, the
        property is is unset.
        '''
        return self.data['standbyMode']

    @property
    def tpmPcrValues(self):
        '''The array of PCR digest values stored in the TPM device since the last host boot
        time.
        '''
        return self.data['tpmPcrValues']

