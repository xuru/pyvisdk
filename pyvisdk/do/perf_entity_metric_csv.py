# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PerfEntityMetricCSV(vim, *args, **kwargs):
    '''This data object type stores metric values for a specific entity in CSV format.'''
    
    obj = vim.client.factory.create('ns0:PerfEntityMetricCSV')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'entity', 'sampleInfoCSV', 'value' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    