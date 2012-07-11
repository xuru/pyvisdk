
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PerfMetricId(vim, *args, **kwargs):
    '''This data object type contains information that associates a performance
    counter with a performance metric. When constructing this data object for the
    metricId property of the PerfQuerySpec to submit to one of the
    PerformanceManager query operations, the instance property supports these
    special characters:* An asterisk (*) to specify all instances of the metric for
    the specified counterId * Double-quotes ("") to specify aggregated statistics'''
    
    obj = vim.client.factory.create('ns0:PerfMetricId')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'counterId', 'instance' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    