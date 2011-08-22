
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DatastoreMountPathDatastorePair(vim, *args, **kwargs):
    '''Contains a mapping of an old mount path and its corresponding resignatured or
    remounted datastore'''
    
    obj = vim.client.factory.create('ns0:DatastoreMountPathDatastorePair')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))
        
    signature = [ 'datastore', 'oldMountPath' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    