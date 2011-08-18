# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def OvfCreateImportSpecParams(vim, *args, **kwargs):
    '''Parameters for deploying an OVF.'''
    
    obj = vim.client.factory.create('ns0:OvfCreateImportSpecParams')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'deploymentOption', 'locale', 'msgBundle', 'diskProvisioning', 'entityName',
        'hostSystem', 'ipAllocationPolicy', 'ipProtocol', 'networkMapping',
        'propertyMapping', 'resourceMapping' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    