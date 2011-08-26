
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostListSummary(vim, *args, **kwargs):
    '''VirtualCenter can retrieve this information very efficiently, even for a large
    set of hosts.'''
    
    obj = vim.client.factory.create('ns0:HostListSummary')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))
        
    signature = [ 'config', 'overallStatus', 'quickStats', 'rebootRequired' ]
    inherited = [ 'currentEVCModeKey', 'customValue', 'hardware', 'host', 'managementServerIp',
        'maxEVCModeKey', 'runtime' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    