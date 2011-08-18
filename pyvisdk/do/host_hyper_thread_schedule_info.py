# -*- coding: ascii -*-

import logging

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
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'active', 'available', 'config' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    