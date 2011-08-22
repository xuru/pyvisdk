
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualAppImportSpec(vim, *args, **kwargs):
    '''A VAppImportSpec is used by ResourcePool.importVApp when importing vApps
    (single VM or multi-VM).It provides all information needed to import a
    VirtualApp.See also ImportSpec.'''
    
    obj = vim.client.factory.create('ns0:VirtualAppImportSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))
        
    signature = [ 'name', 'resourcePoolSpec', 'vAppConfigSpec' ]
    inherited = [ 'entityConfig', 'child' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    