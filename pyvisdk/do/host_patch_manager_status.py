
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPatchManagerStatus(vim, *args, **kwargs):
    ''''''
    
    obj = vim.client.factory.create('ns0:HostPatchManagerStatus')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 7 arguments got: %d' % len(args))

    required = [ 'applicable', 'id', 'installed', 'reconnectRequired', 'restartRequired',
        'vmOffRequired' ]
    optional = [ 'installState', 'integrity', 'prerequisitePatch', 'reason',
        'supersededPatchIds', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    