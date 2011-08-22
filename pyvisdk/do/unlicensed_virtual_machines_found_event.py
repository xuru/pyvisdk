
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def UnlicensedVirtualMachinesFoundEvent(vim, *args, **kwargs):
    '''This event records that we discovered unlicensed virtual machines on the
    specified host. After this event is entered into the event log, we expect to
    see a corresponding (@link vim.event.Event.UnlicensedVirtualMachinesEvent
    UnlicensedVirtualMachinesEvent) (@link vim.ManagedEntity.configIssue
    configIssue) on the host.'''
    
    obj = vim.client.factory.create('ns0:UnlicensedVirtualMachinesFoundEvent')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))
        
    signature = [ 'chainId', 'createdTime', 'key', 'userName', 'available' ]
    inherited = [ 'changeTag', 'computeResource', 'datacenter', 'ds', 'dvs',
        'fullFormattedMessage', 'host', 'net', 'vm' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    