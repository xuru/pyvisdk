
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineBootOptions(DynamicData):
    '''The VirtualMachineBootOptions data object defines the boot-time behavior of a
        virtual machine.You can use the delay options to specify a time interval
        during which you can enter the virtual machine BIOS setup. These options
        provide a solution for the situation that occurs when the console attaches
        to the virtual machine after the boot sequence has passed the BIOS setup
        entry point.
    '''
    
    def __init__(self, bootDelay, bootRetryDelay, bootRetryEnabled, enterBIOSSetup):
        # MUST define these
        super(VirtualMachineBootOptions, self).__init__()
    
        self.data['bootDelay'] = bootDelay
        self.data['bootRetryDelay'] = bootRetryDelay
        self.data['bootRetryEnabled'] = bootRetryEnabled
        self.data['enterBIOSSetup'] = enterBIOSSetup
    
    
    @property
    def bootDelay(self):
        '''Delay in milliseconds before starting the boot sequence. The boot delay specifies
        a time interval between virtual machine power on or restart and the
        beginning of the boot sequence.
        '''
        return self.data['bootDelay']

    @property
    def bootRetryDelay(self):
        '''Delay in milliseconds before a boot retry. The boot retry delay specifies a time
        interval between virtual machine boot failure and the subsequent attempt
        to boot again. The virtual machine uses this value only if
        bootRetryEnabled is true.
        '''
        return self.data['bootRetryDelay']

    @property
    def bootRetryEnabled(self):
        '''If set to
        '''
        return self.data['bootRetryEnabled']

    @property
    def enterBIOSSetup(self):
        '''If set to
        '''
        return self.data['enterBIOSSetup']

