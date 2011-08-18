# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def FileInfo(vim, *args, **kwargs):
    '''This data object type contains rudimentary information about a file in a
    datastore. The information here is not meant to cover all information in
    traditional file systems, but rather to provide sufficient information for
    files that are associated with virtual machines. Derived types describe the
    known file types for a datastore.'''
    
    obj = vim.client.factory.create('ns0:FileInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'fileSize', 'modification', 'owner', 'path' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    