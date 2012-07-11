
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VmDasBeingResetWithScreenshotEvent(vim, *args, **kwargs):
    '''This event records when a virtual machine is reset by HA VM Health Monitoring
    on hosts that support the create screenshot api'''
    
    obj = vim.client.factory.create('ns0:VmDasBeingResetWithScreenshotEvent')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 7 arguments got: %d' % len(args))

    required = [ 'screenshotFilePath', 'template', 'chainId', 'createdTime', 'key', 'userName' ]
    optional = [ 'reason', 'changeTag', 'computeResource', 'datacenter', 'ds', 'dvs',
        'fullFormattedMessage', 'host', 'net', 'vm', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    