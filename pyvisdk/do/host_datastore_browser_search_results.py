
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDatastoreBrowserSearchResults(vim, *args, **kwargs):
    '''This data object type contains the results of a search method for one
    datastore. A search method typically returns a set of these objects as an
    array.'''
    
    obj = vim.client.factory.create('ns0:HostDatastoreBrowserSearchResults')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'datastore', 'file', 'folderPath' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    