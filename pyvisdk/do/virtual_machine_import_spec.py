# -*- coding: ascii -*-

import logging

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
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'entityConfig', 'configSpec', 'resPoolEntity' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    