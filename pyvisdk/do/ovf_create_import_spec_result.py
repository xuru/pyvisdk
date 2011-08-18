# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def OvfCreateImportSpecResult(vim, *args, **kwargs):
    '''The CreateImportSpecResult contains all information regarding the import that
    can be extracted from the OVF descriptor.For example, this includes the list of
    items that the caller must upload in order to complete the import, but not the
    list of URLs to which the files must be uploaded. These paths are not known
    until the VMs have been created, ie. until ResourcePool.importVApp has been
    called.'''
    
    obj = vim.client.factory.create('ns0:OvfCreateImportSpecResult')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'error', 'fileItem', 'importSpec', 'warning' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    