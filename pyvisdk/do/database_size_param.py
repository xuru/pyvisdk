# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DatabaseSizeParam(vim, *args, **kwargs):
    '''DatabaseSizeParam contains information about a sample inventory. Using this
    information, database size requirements for that sample inventory can be
    computed. Depending on the accuracy of estimate desired, users can choose to
    specify the number of different types of managed entities. The numHosts and
    numVirtualMachines are the only two required fields. Rest are all optional
    fields filled up by Virtual Center based on some heuristics. These parameters
    need not represent a real inventory. The user can use these parameters to
    estimate the database size required by a hypothetical VirtualCenter setup.'''
    
    obj = vim.client.factory.create('ns0:DatabaseSizeParam')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'inventoryDesc', 'perfStatsDesc' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    