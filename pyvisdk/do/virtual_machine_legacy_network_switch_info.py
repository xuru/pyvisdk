
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineLegacyNetworkSwitchInfo(vim, *args, **kwargs):
    '''The LegacyNetworkSwitchInfo data object type contains information about the
    legacy network switches available on the host.* VMware Server - Options
    available for the "custom" NetworkBackingType. * ESX Server - The "esxnet"
    NetworkBackingType.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineLegacyNetworkSwitchInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'name' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    