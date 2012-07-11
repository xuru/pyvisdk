
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def FcoeConfig(vim, *args, **kwargs):
    '''This data object type describes an FCoE configuration as it pertains to an
    underlying physical NIC. Terminology is borrowed from T11's working draft of
    the Fibre Channel Backbone 5 standard (FC-BB-5). The draft can be found at
    http://www.t11.org.'''
    
    obj = vim.client.factory.create('ns0:FcoeConfig')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'capabilities', 'fcoeActive', 'priorityClass', 'sourceMac', 'vlanRange' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    