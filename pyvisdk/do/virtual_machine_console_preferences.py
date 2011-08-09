
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineConsolePreferences(DynamicData):
    '''Preferences for the legacy console application that affect the way it behaves
        during power operations on the virtual machine.
    '''
    
    def __init__(self, closeOnPowerOffOrSuspend, enterFullScreenOnPowerOn, powerOnWhenOpened):
        # MUST define these
        super(VirtualMachineConsolePreferences, self).__init__()
    
        self.data['closeOnPowerOffOrSuspend'] = closeOnPowerOffOrSuspend
        self.data['enterFullScreenOnPowerOn'] = enterFullScreenOnPowerOn
        self.data['powerOnWhenOpened'] = powerOnWhenOpened
    
    
    @property
    def closeOnPowerOffOrSuspend(self):
        '''Close the console application when the virtual machine is powered off or
        suspended.
        '''
        return self.data['closeOnPowerOffOrSuspend']

    @property
    def enterFullScreenOnPowerOn(self):
        '''Enter full screen mode when this virtual machine is powered on.
        '''
        return self.data['enterFullScreenOnPowerOn']

    @property
    def powerOnWhenOpened(self):
        '''Power on the virtual machine when it is opened in the console.
        '''
        return self.data['powerOnWhenOpened']

