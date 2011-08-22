
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineMemoryReservationSpec(vim, *args, **kwargs):
    '''The VirtualMachineReservationSpec data object specifies configurable parameters
    for virtual machine memory reservation.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineMemoryReservationSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'allocationPolicy', 'virtualMachineReserved' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    