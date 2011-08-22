
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DVSConfigInfo(vim, *args, **kwargs):
    '''Configuration of a DistributedVirtualSwitch.'''
    
    obj = vim.client.factory.create('ns0:DVSConfigInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 12:
        raise IndexError('Expected at least 13 arguments got: %d' % len(args))
        
    signature = [ 'configVersion', 'contact', 'createTime', 'defaultPortConfig', 'maxPorts',
        'name', 'networkResourceManagementEnabled', 'numPorts', 'numStandalonePorts',
        'productInfo', 'uplinkPortPolicy', 'uuid' ]
    inherited = [ 'description', 'extensionKey', 'host', 'policy', 'targetInfo',
        'uplinkPortgroup', 'vendorSpecificConfig' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    