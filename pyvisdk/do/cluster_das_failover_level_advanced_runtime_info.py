
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
        
    signature = [ 'slotInfo', 'totalGoodHosts', 'totalHosts', 'totalSlots', 'totalVms',
        'unreservedSlots', 'usedSlots' ]
    inherited = [ 'dasHostInfo', 'hostSlots' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    