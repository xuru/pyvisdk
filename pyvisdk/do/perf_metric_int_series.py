# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PerfMetricIntSeries(vim, *args, **kwargs):
    '''This data object type describes integer metric values. The size of the array
    must match the size of sampleInfo property in the PerfEntityMetric that
    contains this series.'''
    
    obj = vim.client.factory.create('ns0:PerfMetricIntSeries')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'id', 'value' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    