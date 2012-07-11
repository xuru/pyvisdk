
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PerformanceManagerCounterLevelMapping(vim, *args, **kwargs):
    '''PerformanceManagerCounterLevelMapping class captures the counter and level
    mapping. Any counter has two aspects: aggregate value or the per-device value.
    For example, cpu.usage.average on a host is an aggregate counter and
    cpu.usage.average on pcpus in a host is a per-device counters. There is a need
    to be able to specify different levels for the two versions. Currently, all
    per-device stats are collected at level greater than or equal to 3. In order to
    be able to configure the level of collections for aggregate and per-device
    counters we have two optional level fields.
    PerformanceManagerCounterLevelMapping is used to update the levels for a
    counter.'''
    
    obj = vim.client.factory.create('ns0:PerformanceManagerCounterLevelMapping')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'counterId' ]
    optional = [ 'aggregateLevel', 'perDeviceLevel', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    