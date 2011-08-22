
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualAppSummary(vim, *args, **kwargs):
    '''This data object type encapsulates a typical set of resource pool information
    that is useful for list views and summary pages.'''
    
    obj = vim.client.factory.create('ns0:VirtualAppSummary')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))
        
    signature = [ 'config', 'name', 'runtime' ]
    inherited = [ 'configuredMemoryMB', 'quickStats', 'installBootRequired', 'instanceUuid',
        'product', 'suspended', 'vAppState' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    