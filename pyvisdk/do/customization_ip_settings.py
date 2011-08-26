
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationIPSettings(vim, *args, **kwargs):
    ''''''
    
    obj = vim.client.factory.create('ns0:CustomizationIPSettings')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'ip' ]
    inherited = [ 'dnsDomain', 'dnsServerList', 'gateway', 'ipV6Spec', 'netBIOS', 'primaryWINS',
        'secondaryWINS', 'subnetMask' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    