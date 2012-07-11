
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostPatchManagerStatusPrerequisitePatch(vim, *args, **kwargs):
    '''Updates that are required to be installed before this update can be installed
    on the server. In addition to being installed on the server, an update can have
    additional requirement on the server or services running on the server
    pertaining to the prerequisite update.'''
    
    obj = vim.client.factory.create('ns0:HostPatchManagerStatusPrerequisitePatch')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'id' ]
    optional = [ 'installState', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    