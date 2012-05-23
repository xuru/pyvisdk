
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

    required = [ 'name', 'resourcePoolSpec', 'vAppConfigSpec' ]
    optional = [ 'child', 'entityConfig', 'instantiationOst', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    