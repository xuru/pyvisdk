
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualPCIControllerOption(vim, *args, **kwargs):
    ''''''
    
    obj = vim.client.factory.create('ns0:VirtualPCIControllerOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 15:
        raise IndexError('Expected at least 16 arguments got: %d' % len(args))
        
    signature = [ 'deprecated', 'hotRemoveSupported', 'plugAndPlay', 'type', 'devices',
        'numEthernetCards', 'numParaVirtualSCSIControllers',
        'numPCIPassthroughDevices', 'numSasSCSIControllers', 'numSCSIControllers',
        'numSoundCards', 'numVideoCards', 'numVmciDevices', 'numVmiRoms',
        'numVmxnet3EthernetCards' ]
    inherited = [ 'autoAssignController', 'backingOption', 'connectOption', 'controllerType',
        'defaultBackingOptionIndex', 'licensingLimit', 'supportedDevice' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    