
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineVMCIDevice(vim, *args, **kwargs):
    '''An application running on a virtual machine uses the VMCI Sockets API for
    communication with other virtual machines on the same host, or for
    communication with the host. For information about using the vSphere VMCI
    Sockets API, see the .'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineVMCIDevice')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'key' ]
    inherited = [ 'backing', 'connectable', 'controllerKey', 'deviceInfo', 'unitNumber',
        'allowUnrestrictedCommunication', 'id' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    