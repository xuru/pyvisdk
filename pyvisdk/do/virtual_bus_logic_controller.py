
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualBusLogicController(vim, *args, **kwargs):
    '''VirtualBusLogicController is the data object that represents a BusLogic SCSI
    controller.'''
    
    obj = vim.client.factory.create('ns0:VirtualBusLogicController')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'sharedBus', 'busNumber', 'key' ]
    optional = [ 'hotAddRemove', 'scsiCtlrUnitNumber', 'device', 'backing', 'connectable',
        'controllerKey', 'deviceInfo', 'unitNumber', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    