
import logging
from pyvisdk.exceptions import InvalidArgumentError

# This module is NOT auto-generated
# Inspired by decompiled Java classes from vCenter's internalvim25stubs.jar
# Unless states otherside, the methods and attributes were not used by esxcli,
# and thus not tested

log = logging.getLogger(__name__)

def VimEsxCLIstoragecoredevicelistScsiDevice(vim, *args, **kwargs):
    obj = vim.client.factory.create('ns0:VimEsxCLIstoragecoredevicelistScsiDevice')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'AttachedFilters', 'DevfsPath', 'Device', 'DeviceType', 'DisplayName', 'HasSettableDisplayName', 'IsLocal', 'IsOffline', 'IsPerenniallyReserved', 'IsPseudo', 'IsRDMCapable', 'IsRemovable', 'IsSSD', 'Model', 'MultipathPlugin', 'OtherUIDs', 'Revision', 'SCSILevel', 'Size', 'Status', 'ThinProvisioningStatus', 'VAAIStatus', 'Vendor' ]

    for name, arg in zip(required + optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj