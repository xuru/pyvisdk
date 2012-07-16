
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def NoMaintenanceModeDrsRecommendationForVM(vim, *args, **kwargs):
    '''This event records that DRS did not recommend a migration for a powered on
    virtual machine, even though its host is going into maintenance mode. DRS may
    not be able to recommend a migration for a virtual machine for reasons, include
    but not limited to:* No other connected host is compatible with this virtual
    machine. * None of the other compatible hosts have sufficient resources to
    satisfy the reservation requirements of this virtual machine. * Moving to any
    other host would violate a DRS rule. For example, all other compatible hosts
    have some incompatible virtual machines running. * DRS is disabled on this
    virtual machine. * This virtual machine was still in the process of migrating
    into the host going into maintenance mode and was not considered by DRS. * This
    virtual machine was in the process of migrating to another host when the host
    tried to enter maintenance mode.'''
    
    obj = vim.client.factory.create('ns0:NoMaintenanceModeDrsRecommendationForVM')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'template', 'chainId', 'createdTime', 'key', 'userName' ]
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
    