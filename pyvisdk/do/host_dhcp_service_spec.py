
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDhcpServiceSpec(vim, *args, **kwargs):
    ''''''
    
    obj = vim.client.factory.create('ns0:HostDhcpServiceSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 8:
        raise IndexError('Expected at least 9 arguments got: %d' % len(args))
        
    signature = [ 'defaultLeaseDuration', 'ipSubnetAddr', 'ipSubnetMask', 'leaseBeginIp',
        'leaseEndIp', 'maxLeaseDuration', 'unlimitedLease', 'virtualSwitch' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    