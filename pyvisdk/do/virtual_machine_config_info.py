# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineConfigInfo(vim, *args, **kwargs):
    '''The ConfigInfo data object type encapsulates the configuration settings and
    virtual hardware for a virtual machine. This type holds all the information
    that is present in the .vmx configuration file for the virtual machine.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineConfigInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'alternateGuestName' ]
    inherited = [ 'annotation', 'bootOptions', 'changeTrackingEnabled', 'changeVersion',
        'consolePreferences', 'cpuAffinity', 'cpuAllocation', 'cpuFeatureMask',
        'cpuHotAddEnabled', 'cpuHotRemoveEnabled', 'datastoreUrl', 'defaultPowerOps',
        'extraConfig', 'files', 'flags', 'ftInfo', 'guestFullName', 'guestId',
        'hardware', 'hotPlugMemoryIncrementSize', 'hotPlugMemoryLimit', 'instanceUuid',
        'locationId', 'memoryAffinity', 'memoryAllocation', 'memoryHotAddEnabled',
        'modified', 'name', 'networkShaper', 'npivDesiredNodeWwns',
        'npivDesiredPortWwns', 'npivNodeWorldWideName', 'npivOnNonRdmDisks',
        'npivPortWorldWideName', 'npivTemporaryDisabled', 'npivWorldWideNameType',
        'swapPlacement', 'template', 'tools', 'uuid', 'vAppConfig', 'vAssertsEnabled',
        'version' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    