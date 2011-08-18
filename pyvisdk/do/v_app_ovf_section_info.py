# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VAppOvfSectionInfo(vim, *args, **kwargs):
    '''The OvfSection encapsulates uninterpreted meta-data sections in an OVF
    descriptor. When an OVF package is imported, non-required / non-interpreted
    sections will be stored as OvfSection object. During the creation of an OVF
    package, these sections will be placed in the OVF descriptor.'''
    
    obj = vim.client.factory.create('ns0:VAppOvfSectionInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'atEnvelopeLevel', 'contents', 'key', 'namespace', 'type' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    