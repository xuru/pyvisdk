# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

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
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'fileSize', 'modification', 'owner', 'path' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    