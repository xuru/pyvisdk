
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineConfigSpec(vim, *args, **kwargs):
    '''The ConfigSpec data object type encapsulates configuration settings when
    creating or reconfiguring a virtual machine. To support incremental changes,
    these properties are all optional.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineConfigSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    required = [  ]
    optional = [ 'alternateGuestName', 'annotation', 'bootOptions', 'changeTrackingEnabled',
        'changeVersion', 'consolePreferences', 'cpuAffinity', 'cpuAllocation',
        'cpuFeatureMask', 'cpuHotAddEnabled', 'cpuHotRemoveEnabled', 'deviceChange',
        'extraConfig', 'files', 'flags', 'ftInfo', 'guestId', 'instanceUuid',
        'locationId', 'memoryAffinity', 'memoryAllocation', 'memoryHotAddEnabled',
        'memoryMB', 'name', 'networkShaper', 'npivDesiredNodeWwns',
        'npivDesiredPortWwns', 'npivNodeWorldWideName', 'npivOnNonRdmDisks',
        'npivPortWorldWideName', 'npivTemporaryDisabled', 'npivWorldWideNameOp',
        'npivWorldWideNameType', 'numCPUs', 'powerOpInfo', 'swapPlacement', 'tools',
        'uuid', 'vAppConfig', 'vAppConfigRemoved', 'vAssertsEnabled', 'version',
        'dynamicProperty', 'dynamicType' ]
    
    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    