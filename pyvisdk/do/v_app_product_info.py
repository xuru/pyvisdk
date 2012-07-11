
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VAppProductInfo(vim, *args, **kwargs):
    '''Information that describes what product a vApp contains, e.g., what software
    that is installed in the contained virtual machines.'''
    
    obj = vim.client.factory.create('ns0:VAppProductInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'key' ]
    optional = [ 'appUrl', 'classId', 'fullVersion', 'instanceId', 'name', 'productUrl',
        'vendor', 'vendorUrl', 'version', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    