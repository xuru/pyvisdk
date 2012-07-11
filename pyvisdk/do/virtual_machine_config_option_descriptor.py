
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineConfigOptionDescriptor(vim, *args, **kwargs):
    '''Contains the definition of a unique key that can be used to retrieve a
    configOption object.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineConfigOptionDescriptor')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'createSupported', 'defaultConfigOption', 'key' ]
    optional = [ 'description', 'host', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    