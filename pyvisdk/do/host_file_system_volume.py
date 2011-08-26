
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostFileSystemVolume(vim, *args, **kwargs):
    '''Typically a FileSystem is exposed as a datatoreSee DatastoreInfoSee
    HostVmfsVolumeSee HostNasVolumeSee HostLocalFileSystemVolume'''
    
    obj = vim.client.factory.create('ns0:HostFileSystemVolume')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))
        
    signature = [ 'capacity', 'name', 'type' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    