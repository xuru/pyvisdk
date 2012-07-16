
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def FcoeConfigVlanRange(vim, *args, **kwargs):
    '''Used to represent inclusive intervals of VLAN IDs. Valid VLAN IDs fall within
    the range [0,4094], and the low value of a VlanRange must be less than or equal
    to the high value.'''
    
    obj = vim.client.factory.create('ns0:FcoeConfigVlanRange')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'vlanHigh', 'vlanLow' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    