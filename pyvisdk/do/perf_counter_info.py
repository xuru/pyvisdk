
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PerfCounterInfo(vim, *args, **kwargs):
    '''This data object type contains metadata for a performance counter. See
    PerformanceManager for definitions of available counters.'''
    
    obj = vim.client.factory.create('ns0:PerfCounterInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 7 arguments got: %d' % len(args))

    required = [ 'groupInfo', 'key', 'nameInfo', 'rollupType', 'statsType', 'unitInfo' ]
    optional = [ 'associatedCounterId', 'level', 'perDeviceLevel', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    