
from pyvisdk.do.virtual_device_option import VirtualDeviceOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineVMCIDeviceOption(VirtualDeviceOption):
    '''The VirtualMachineVMCIDeviceOption data object contains the options for the
        virtual VMCI device (VirtualMachineVMCIDevice).
    '''
    
    def __init__(self, allowUnrestrictedCommunication):
        # MUST define these
        super(VirtualMachineVMCIDeviceOption, self).__init__()
    
        self.data['allowUnrestrictedCommunication'] = allowUnrestrictedCommunication
    
    
    @property
    def allowUnrestrictedCommunication(self):
        '''Indicates support for VMCI communication and specifies the default operation. If
        defaultValue is set to true, the virtual machine can participate in VMCI
        communication with all other virtual machines on the host. Otherwise, VMCI
        communication will be restricted to trusted services such as the
        hypervisor on the host.
        '''
        return self.data['allowUnrestrictedCommunication']

