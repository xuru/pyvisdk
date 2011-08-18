# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

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
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'datastoreKey', 'disk', 'fileSize', 'importKey', 'key', 'sslThumbprint',
        'targetId', 'url' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    