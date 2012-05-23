
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineScsiPassthroughInfo(vim, *args, **kwargs):
    '''Description of a generic SCSI device, including information about the device
    ID.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineScsiPassthroughInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'physicalUnitNumber', 'scsiClass', 'vendor', 'name' ]
    optional = [ 'configurationTag', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    