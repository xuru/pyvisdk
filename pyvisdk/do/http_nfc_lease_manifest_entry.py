# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HttpNfcLeaseManifestEntry(vim, *args, **kwargs):
    '''Provides a manifest for downloaded (exported) files and disks.'''
    
    obj = vim.client.factory.create('ns0:HttpNfcLeaseManifestEntry')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'capacity', 'disk', 'key', 'populatedSize', 'sha1', 'size' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    