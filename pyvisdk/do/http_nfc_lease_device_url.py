# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HttpNfcLeaseDeviceUrl(vim, *args, **kwargs):
    '''Provides a mapping from logical device IDs to upload/download URLs.For export,
    a single device id is returned based on the object identifiers for the
    objects.For import, two device ids are returned. One based on the object names
    used in the ImportSpec, and one based on the object identifiers for the created
    objects. This is immutable and would match the id if an ExportLease is latter
    created.'''
    
    obj = vim.client.factory.create('ns0:HttpNfcLeaseDeviceUrl')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'datastoreKey', 'disk', 'fileSize', 'importKey', 'key', 'sslThumbprint',
        'targetId', 'url' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    