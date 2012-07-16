
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VMwareDVSPortSetting(vim, *args, **kwargs):
    '''This class defines the VMware specific configuration for
    DistributedVirtualPort.'''
    
    obj = vim.client.factory.create('ns0:VMwareDVSPortSetting')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'ipfixEnabled', 'qosTag', 'securityPolicy', 'txUplink', 'uplinkTeamingPolicy',
        'vlan', 'blocked', 'inShapingPolicy', 'networkResourcePoolKey',
        'outShapingPolicy', 'vendorSpecificConfig', 'vmDirectPathGen2Allowed',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    