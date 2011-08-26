
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def OvfCreateImportSpecResult(vim, *args, **kwargs):
    '''For example, this includes the list of items that the caller must upload in
    order to complete the import, but not the list of URLs to which the files must
    be uploaded. These paths are not known until the VMs have been created, ie.
    until ResourcePool.importVApp has been called.'''
    
    obj = vim.client.factory.create('ns0:OvfCreateImportSpecResult')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'error', 'fileItem', 'importSpec', 'warning' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    