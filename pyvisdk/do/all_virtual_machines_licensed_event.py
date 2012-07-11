
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AllVirtualMachinesLicensedEvent(vim, *args, **kwargs):
    '''This event records that the previously unlicensed virtual machines on the
    specified host are now licensed. After this event is entered into the event
    log, we expect to see that the (@link
    vim.event.Event.UnlicensedVirtualMachinesEvent UnlicensedVirtualMachinesEvent)
    (@link vim.ManagedEntity.configIssue configIssue) is removed from the host.'''
    
    obj = vim.client.factory.create('ns0:AllVirtualMachinesLicensedEvent')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'chainId', 'createdTime', 'key', 'userName' ]
    optional = [ 'changeTag', 'computeResource', 'datacenter', 'ds', 'dvs',
        'fullFormattedMessage', 'host', 'net', 'vm', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    