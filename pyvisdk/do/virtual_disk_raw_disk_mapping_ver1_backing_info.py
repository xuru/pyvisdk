
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualDiskRawDiskMappingVer1BackingInfo(vim, *args, **kwargs):
    '''This data object type contains information about backing a virtual disk using a
    raw device mapping. Supported for ESX Server 2.5 and 3.x.'''
    
    obj = vim.client.factory.create('ns0:VirtualDiskRawDiskMappingVer1BackingInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'fileName' ]
    optional = [ 'changeId', 'compatibilityMode', 'contentId', 'deviceName', 'diskMode',
        'lunUuid', 'parent', 'uuid', 'datastore', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    