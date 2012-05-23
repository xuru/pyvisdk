
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VAppConfigInfo(vim, *args, **kwargs):
    '''Configuration of a vApp container.'''
    
    obj = vim.client.factory.create('ns0:VAppConfigInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'annotation', 'installBootRequired', 'installBootStopDelay', 'ipAssignment' ]
    optional = [ 'entityConfig', 'instanceUuid', 'managedBy', 'eula', 'ovfEnvironmentTransport',
        'ovfSection', 'product', 'property', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    