
import logging
from pyvisdk.exceptions import InvalidArgumentError

# This module is NOT auto-generated
# Inspired by decompiled Java classes from vCenter's internalvim25stubs.jar
# Unless states otherside, the methods and attributes were not used by esxcli,
# and thus not tested

log = logging.getLogger(__name__)

def VimEsxCLIhardwarepcilistPciDevice(vim, *args, **kwargs):
    obj = vim.client.factory.create('ns0:VimEsxCLIhardwarepcilistPciDevice')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'Address', 'Bus', 'Chassis', 'ConfiguredOwner', 'CurrentOwner', 'DependentDevice', 'DeviceClass', 'DeviceClassName', 'DeviceID', 'DeviceName', 'FPTSharable', 'Flags', 'Function', 'IRQ', 'InterruptLine', 'InterruptVector', 'ModuleID', 'ModuleName', 'PCIPin', 'ParentDevice', 'PassthruCapable', 'PhysicalSlot', 'ProgrammingInterface', 'ResetMethod', 'RevisionID', 'Segment', 'Slot', 'SlotDescription', 'SpawnedBus', 'SubDeviceID', 'SubVendorID', 'VMkernelName', 'VendorID', 'VendorName' ]

    for name, arg in zip(required + optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj