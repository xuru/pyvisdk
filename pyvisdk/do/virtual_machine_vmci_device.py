
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineVMCIDevice(vim, *args, **kwargs):
    '''The VirtualMachineVMCIDevice data object represents a virtual communication
    device that supports the VMCI (Virtual Machine Communication Interface). Each
    virtual machine has a VMCI device that handles interprocess socket-based
    communication. VMCI device information is available in the virtual machine
    hardware device list (VirtualMachine.config.hardware.device[]).An application
    running on a virtual machine uses the VMCI Sockets API for communication with
    other virtual machines on the same host, or for communication with the host.
    For information about using the vSphere VMCI Sockets API, see the .'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineVMCIDevice')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'key' ]
    optional = [ 'allowUnrestrictedCommunication', 'id', 'backing', 'connectable',
        'controllerKey', 'deviceInfo', 'unitNumber', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    