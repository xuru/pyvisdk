
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostListSummaryQuickStats(vim, *args, **kwargs):
    '''Basic host statistics.Included in the host statistics are fairness scores.
    Fairness scores are represented in units with relative values, meaning they are
    evaluated relative to the scores of other hosts. They should not be thought of
    as having any particular absolute value. Each fairness unit represents an
    increment of 0.001 in a fairness score. The further the fairness score diverges
    from 1, the less fair the allocation. Therefore, a fairness score of 990,
    representing 0.990, is more fair than a fairness score of 1015, which
    represents 1.015. This is because 1.015 is further from 1 than 0.990.'''
    
    obj = vim.client.factory.create('ns0:HostListSummaryQuickStats')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'distributedCpuFairness', 'distributedMemoryFairness', 'overallCpuUsage',
        'overallMemoryUsage', 'uptime', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    