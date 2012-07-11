
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VMwareDVSConfigInfo(vim, *args, **kwargs):
    '''This class defines the VMware specific configuration for
    DistributedVirtualSwitch.'''
    
    obj = vim.client.factory.create('ns0:VMwareDVSConfigInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 13:
        raise IndexError('Expected at least 14 arguments got: %d' % len(args))

    required = [ 'maxMtu', 'configVersion', 'contact', 'createTime', 'defaultPortConfig',
        'maxPorts', 'name', 'networkResourceManagementEnabled', 'numPorts',
        'numStandalonePorts', 'productInfo', 'uplinkPortPolicy', 'uuid' ]
    optional = [ 'ipfixConfig', 'linkDiscoveryProtocolConfig', 'pvlanConfig', 'vspanSession',
        'description', 'extensionKey', 'host', 'policy', 'switchIpAddress',
        'targetInfo', 'uplinkPortgroup', 'vendorSpecificConfig', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    