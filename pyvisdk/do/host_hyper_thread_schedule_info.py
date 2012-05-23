
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostHyperThreadScheduleInfo(vim, *args, **kwargs):
    '''This data object type describes the CpuSchedulerSystem configuration for
    optimizing hyperthreading. The primary hyperthreading optimization employed by
    the CpuSchedulerSystem is to utilize hyperthreads as additional schedulable
    resources. Although hyperthreads provide limited additional concurrency,
    certain workloads (such as idling) can take advantage of these hyperthreads.
    This is particularly useful for SMP virtual machines that use gang scheduling.
    (Gang scheduling refers to a situation in which all of a parallel program's
    tasks are grouped into a "gang" and concurrently scheduled on distinct
    processors of a parallel computer system.)Changes to the hyperthreading
    optimization can take effect only after a system restart. Therefore, while it
    is possible to change the configuration at any time, the change will take
    effect only on the next boot.'''
    
    obj = vim.client.factory.create('ns0:HostHyperThreadScheduleInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'active', 'available', 'config' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    