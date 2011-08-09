
from pyvisdk.do.virtual_device import VirtualDevice
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineVMCIDevice(VirtualDevice):
    '''The VirtualMachineVMCIDevice data object represents a virtual communication device
        that supports the VMCI (Virtual Machine Communication Interface). Each
        virtual machine has a VMCI device that handles interprocess socket-based
        communication. VMCI device information is available in the virtual machine
        hardware device list (VirtualMachine.config.hardware.device[]).An
        application running on a virtual machine uses the VMCI Sockets API for
        communication with other virtual machines on the same host, or for
        communication with the host. For information about using the vSphere VMCI
        Sockets API, see the .
    '''
    
    def __init__(self, allowUnrestrictedCommunication, id):
        # MUST define these
        super(VirtualMachineVMCIDevice, self).__init__()
    
        self.data['allowUnrestrictedCommunication'] = allowUnrestrictedCommunication
        self.data['id'] = id
    
    
    @property
    def allowUnrestrictedCommunication(self):
        '''Determines the extent of VMCI communication with this virtual machine. Set this
        property to true to allow VMCI communication with all virtual machines on
        the host and with trusted services. Set this property to false to allow
        VMCI communication only with trusted services such as the hypervisor on
        the host.
        '''
        return self.data['allowUnrestrictedCommunication']

    @property
    def id(self):
        '''Unique identifier for VMCI socket access to this virtual machine. Use this value
        to identify this virtual machine in calls to the VMCI Sockets API.
        Applications running on other virtual machines on this host will use this
        value to connect to this virtual machine. You can cast this value to a
        32-bit unsigned integer.
        '''
        return self.data['id']

