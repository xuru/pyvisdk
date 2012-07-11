
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PerfQuerySpec(vim, *args, **kwargs):
    '''This data object specifies the query parameters, including the managed object
    reference to the target entity for statistics retrieval.* If the optional
    intervalId is omitted, the metrics are returned in their originally sampled
    interval. * When an intervalId is specified, the server tries to summarize the
    information for the specified intervalId. However, if that interval does not
    exist or has no data, the server summarizes the information using the best
    interval available. * If the range between startTime and endTime crosses
    multiple sample interval periods, the result contains data from the longest
    interval in the period.'''
    
    obj = vim.client.factory.create('ns0:PerfQuerySpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'entity' ]
    optional = [ 'endTime', 'format', 'intervalId', 'maxSample', 'metricId', 'startTime',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    