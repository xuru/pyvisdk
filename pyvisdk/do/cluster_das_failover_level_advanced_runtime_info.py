
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterDasFailoverLevelAdvancedRuntimeInfo(vim, *args, **kwargs):
    '''Advanced runtime information related to the high availability service for a
    cluster that has been configured with a failover level admission control
    policy. See ClusterFailoverLevelAdmissionControlPolicy.'''
    
    obj = vim.client.factory.create('ns0:ClusterDasFailoverLevelAdvancedRuntimeInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 8 arguments got: %d' % len(args))

    required = [ 'slotInfo', 'totalGoodHosts', 'totalHosts', 'totalSlots', 'totalVms',
        'unreservedSlots', 'usedSlots' ]
    optional = [ 'hostSlots', 'dasHostInfo', 'heartbeatDatastoreInfo', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    