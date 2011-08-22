
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
        
    signature = [ 'configSpec' ]
    inherited = [ 'entityConfig', 'resPoolEntity' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    