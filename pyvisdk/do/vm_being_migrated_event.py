
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmBeingMigratedEvent(vim, *args, **kwargs):
    '''This event records that a virtual machine is being migrated.'''
    
    obj = vim.client.factory.create('ns0:VmBeingMigratedEvent')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 7 arguments got: %d' % len(args))

    required = [ 'destHost', 'template', 'chainId', 'createdTime', 'key', 'userName' ]
    optional = [ 'destDatacenter', 'destDatastore', 'changeTag', 'computeResource',
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
    