
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualBusLogicControllerOption(vim, *args, **kwargs):
    '''This data object contains the options for a BusLogic SCSI controller.'''
    
    obj = vim.client.factory.create('ns0:VirtualBusLogicControllerOption')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 12:
        raise IndexError('Expected at least 13 arguments got: %d' % len(args))

    required = [ 'defaultSharedIndex', 'hotAddRemove', 'numSCSICdroms', 'numSCSIDisks',
        'numSCSIPassthrough', 'scsiCtlrUnitNumber', 'sharing', 'devices', 'deprecated',
        'hotRemoveSupported', 'plugAndPlay', 'type' ]
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
    