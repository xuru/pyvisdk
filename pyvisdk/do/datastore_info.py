# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DatastoreInfo(vim, *args, **kwargs):
    '''Detailed information about a datastore. This is a base type for derived types
    that have more specific details about a datastore. See HostVmfsVolume See
    HostNasVolume See HostLocalFileSystemVolume'''
    
    obj = vim.client.factory.create('ns0:DatastoreInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))
        
    signature = [ 'freeSpace', 'maxFileSize', 'name' ]
    inherited = [ 'timestamp', 'url' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    