
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationSysprepFailed(vim, *args, **kwargs):
    '''Sysprep failed to run in the guest during customization. This will most like
    have been caused by the fact that the wrong sysprep was used for the guest, so
    we include the version information in the event.'''
    
    obj = vim.client.factory.create('ns0:CustomizationSysprepFailed')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 8 arguments got: %d' % len(args))

    required = [ 'sysprepVersion', 'systemVersion', 'template', 'chainId', 'createdTime', 'key',
        'userName' ]
    optional = [ 'logLocation', 'changeTag', 'computeResource', 'datacenter', 'ds', 'dvs',
        'fullFormattedMessage', 'host', 'net', 'vm', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    