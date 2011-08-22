
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineVMCIDeviceOption(vim, *args, **kwargs):
    '''The VirtualMachineVMCIDeviceOption data object contains the options for the
    virtual VMCI device (VirtualMachineVMCIDevice).'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineVMCIDeviceOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))
        
    signature = [ 'deprecated', 'hotRemoveSupported', 'plugAndPlay', 'type',
        'allowUnrestrictedCommunication' ]
    inherited = [ 'autoAssignController', 'backingOption', 'connectOption', 'controllerType',
        'defaultBackingOptionIndex', 'licensingLimit' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    