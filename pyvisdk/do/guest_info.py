
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def GuestInfo(vim, *args, **kwargs):
    '''Information about the guest operating system.Most of this information is
    collected by VMware Tools. In general, be sure you have VMware Tools installed
    and that the virtual machine is running when you access this information.'''
    
    obj = vim.client.factory.create('ns0:GuestInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'guestState' ]
    optional = [ 'appHeartbeatStatus', 'disk', 'guestFamily', 'guestFullName', 'guestId',
        'guestOperationsReady', 'hostName', 'interactiveGuestOperationsReady',
        'ipAddress', 'ipStack', 'net', 'screen', 'toolsRunningStatus', 'toolsStatus',
        'toolsVersion', 'toolsVersionStatus', 'toolsVersionStatus2', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    