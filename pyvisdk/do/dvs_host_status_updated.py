
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DvsHostStatusUpdated(vim, *args, **kwargs):
    '''A host has it's status or statusDetail updated.'''
    
    obj = vim.client.factory.create('ns0:DvsHostStatusUpdated')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'hostMember', 'chainId', 'createdTime', 'key', 'userName' ]
    optional = [ 'newStatus', 'newStatusDetail', 'oldStatus', 'oldStatusDetail', 'changeTag',
        'computeResource', 'datacenter', 'ds', 'dvs', 'fullFormattedMessage', 'host',
        'net', 'vm', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    