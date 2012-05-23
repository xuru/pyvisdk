
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPciDevice(vim, *args, **kwargs):
    '''This data object type describes information about a single Peripheral Component
    Interconnect (PCI) device.'''
    
    obj = vim.client.factory.create('ns0:HostPciDevice')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 11:
        raise IndexError('Expected at least 12 arguments got: %d' % len(args))

    required = [ 'bus', 'classId', 'deviceId', 'deviceName', 'function', 'id', 'slot',
        'subDeviceId', 'subVendorId', 'vendorId', 'vendorName' ]
    optional = [ 'parentBridge', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    