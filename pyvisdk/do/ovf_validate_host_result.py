# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def OvfValidateHostResult(vim, *args, **kwargs):
    ''''''
    
    obj = vim.client.factory.create('ns0:OvfValidateHostResult')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'downloadSize', 'error', 'flatDeploymentSize', 'sparseDeploymentSize',
        'supportedDiskProvisioning', 'warning' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    