
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDiskRawDiskMappingVer1BackingOption(vim, *args, **kwargs):
    '''The VirtualDiskOption.RawDiskMappingVer1BackingOption object type contains the
    available options when backing a virtual disk using a raw device mapping on ESX
    Server 2.5 or 3.x.'''
    
    obj = vim.client.factory.create('ns0:VirtualDiskRawDiskMappingVer1BackingOption')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'compatibilityMode', 'diskMode', 'uuid', 'autoDetectAvailable', 'type' ]
    optional = [ 'descriptorFileNameExtensions', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    