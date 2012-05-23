
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def StorageIOAllocationInfo(vim, *args, **kwargs):
    '''The IOAllocationInfo specifies the shares and the limit for storage I/O
    resource.The storage I/O resource is allocated to virtual machines based on
    their shares and limit. We do not support reservation for storage I/O resource.
    And we do not support storage I/O resource management on resource pools.Each
    virtual machine has one IOAllocationInfo object per virtual disk. For example,
    we can specify that a virtual machine has 500 shares on the first virtual disk,
    1000 shares on the second virtual disk, etc.'''
    
    obj = vim.client.factory.create('ns0:StorageIOAllocationInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'limit', 'shares', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    