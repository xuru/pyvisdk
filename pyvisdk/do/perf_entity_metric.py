# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PerfEntityMetric(vim, *args, **kwargs):
    '''This data object type stores values and metadata for metrics associated with a
    specific entity, in 'normal' format.'''
    
    obj = vim.client.factory.create('ns0:PerfEntityMetric')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'entity', 'sampleInfo', 'value' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    