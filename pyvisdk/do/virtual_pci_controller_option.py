
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualPCIControllerOption(vim, *args, **kwargs):
    '''This data object type contains the options for a virtual PCI Controller.'''
    
    obj = vim.client.factory.create('ns0:VirtualPCIControllerOption')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 15:
        raise IndexError('Expected at least 16 arguments got: %d' % len(args))

    required = [ 'numEthernetCards', 'numParaVirtualSCSIControllers',
        'numPCIPassthroughDevices', 'numSasSCSIControllers', 'numSCSIControllers',
        'numSoundCards', 'numVideoCards', 'numVmciDevices', 'numVmiRoms',
        'numVmxnet3EthernetCards', 'devices', 'deprecated', 'hotRemoveSupported',
        'plugAndPlay', 'type' ]
    optional = [ 'supportedDevice', 'autoAssignController', 'backingOption', 'connectOption',
        'controllerType', 'defaultBackingOptionIndex', 'licensingLimit',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    