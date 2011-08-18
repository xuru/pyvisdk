# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def EvaluationLicenseSource(vim, *args, **kwargs):
    '''Specify an evaluation license source. Feature licensing is not required while
    the remaining hours is greater than zero.'''
    
    obj = vim.client.factory.create('ns0:EvaluationLicenseSource')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'remainingHours' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    