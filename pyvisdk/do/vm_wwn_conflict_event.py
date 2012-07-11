
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmWwnConflictEvent(vim, *args, **kwargs):
    '''This event records a conflict of virtual machine WWNs (World Wide Name).'''
    
    obj = vim.client.factory.create('ns0:VmWwnConflictEvent')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 7 arguments got: %d' % len(args))

    required = [ 'wwn', 'template', 'chainId', 'createdTime', 'key', 'userName' ]
    optional = [ 'conflictedHosts', 'conflictedVms', 'changeTag', 'computeResource',
        'datacenter', 'ds', 'dvs', 'fullFormattedMessage', 'host', 'net', 'vm',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    