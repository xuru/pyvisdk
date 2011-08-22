
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostCnxFailedCcagentUpgradeEvent(vim, *args, **kwargs):
    '''This event records a failure to connect to a host due to a conflict with an
    upgrade or installation of the host agent.'''
    
    obj = vim.client.factory.create('ns0:HostCnxFailedCcagentUpgradeEvent')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))
        
    signature = [ 'chainId', 'createdTime', 'key', 'userName' ]
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
    