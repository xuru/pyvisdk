
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def OvfFile(vim, *args, **kwargs):
    '''An instance of this class is used to tell OvfManager about the choices the
    caller made about a file. This information is needed when the OVF descriptor is
    generated with createDescriptor.'''
    
    obj = vim.client.factory.create('ns0:OvfFile')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))
        
    signature = [ 'deviceId', 'path', 'size' ]
    inherited = [ 'capacity', 'chunkSize', 'compressionMethod', 'populatedSize' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    