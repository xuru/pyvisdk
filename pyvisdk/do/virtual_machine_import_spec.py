
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineImportSpec(vim, *args, **kwargs):
    '''A VmImportSpec is used by ResourcePool.importVApp when importing entities.It
    provides all information needed to import a VirtualMachine. So far, this
    coincides with VirtualMachineConfigSpec.A VmImportSpec can be contained in a
    VirtualAppImportSpec as part of the ImportSpec for an entity.See also
    ImportSpec.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineImportSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'configSpec' ]
    optional = [ 'resPoolEntity', 'entityConfig', 'instantiationOst', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    