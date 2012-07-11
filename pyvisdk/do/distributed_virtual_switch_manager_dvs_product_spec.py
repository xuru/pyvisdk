
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DistributedVirtualSwitchManagerDvsProductSpec(vim, *args, **kwargs):
    '''This class is used to specify ProductSpec for the DVS. The two properties are
    strictly mutually exclusive. If both properties are set, then an
    InvalidArgument fault would be thrown.'''
    
    obj = vim.client.factory.create('ns0:DistributedVirtualSwitchManagerDvsProductSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'distributedVirtualSwitch', 'newSwitchProductSpec', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    