
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineMemoryReservationInfo(vim, *args, **kwargs):
    '''The VirtualMachineReservationInfo data object type describes the amount of
    memory that is being reserved for virtual machines on the host, and how
    additional memory may be acquired.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineMemoryReservationInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'allocationPolicy', 'virtualMachineMax', 'virtualMachineMin',
        'virtualMachineReserved' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    