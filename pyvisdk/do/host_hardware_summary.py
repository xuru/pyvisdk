# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostHardwareSummary(vim, *args, **kwargs):
    '''This data object type summarizes hardware used by the host.'''
    
    obj = vim.client.factory.create('ns0:HostHardwareSummary')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 9:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'cpuMhz', 'cpuModel', 'memorySize', 'model', 'numCpuCores', 'numCpuPkgs',
        'numCpuThreads', 'numHBAs', 'numNics', 'otherIdentifyingInfo', 'uuid', 'vendor' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    