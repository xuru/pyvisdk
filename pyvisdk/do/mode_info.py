
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ModeInfo(vim, *args, **kwargs):
    '''The FileAccess.Modes data object type defines the known access modes for a
    datastore. The property values specify how to interpret the "what" property for
    a FileAccess object.'''
    
    obj = vim.client.factory.create('ns0:ModeInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))
        
    signature = [ 'full', 'modify', 'read', 'use' ]
    inherited = [ 'admin', 'browse' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    