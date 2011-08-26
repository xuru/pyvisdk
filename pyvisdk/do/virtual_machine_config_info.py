
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineConfigInfo(vim, *args, **kwargs):
    ''''''
    
    obj = vim.client.factory.create('ns0:VirtualMachineConfigInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 13:
        raise IndexError('Expected at least 14 arguments got: %d' % len(args))
        
    signature = [ 'alternateGuestName', 'changeVersion', 'defaultPowerOps', 'files', 'flags',
        'guestFullName', 'guestId', 'hardware', 'modified', 'name', 'template', 'uuid',
        'version' ]
    inherited = [ 'annotation', 'bootOptions', 'changeTrackingEnabled', 'consolePreferences',
        'cpuAffinity', 'cpuAllocation', 'cpuFeatureMask', 'cpuHotAddEnabled',
        'cpuHotRemoveEnabled', 'datastoreUrl', 'extraConfig', 'ftInfo',
        'hotPlugMemoryIncrementSize', 'hotPlugMemoryLimit', 'instanceUuid',
        'locationId', 'memoryAffinity', 'memoryAllocation', 'memoryHotAddEnabled',
        'networkShaper', 'npivDesiredNodeWwns', 'npivDesiredPortWwns',
        'npivNodeWorldWideName', 'npivOnNonRdmDisks', 'npivPortWorldWideName',
        'npivTemporaryDisabled', 'npivWorldWideNameType', 'swapPlacement', 'tools',
        'vAppConfig', 'vAssertsEnabled' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    