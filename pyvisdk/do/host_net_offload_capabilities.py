
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostNetOffloadCapabilities(vim, *args, **kwargs):
    '''This data object type is used both to publish the list of offload capabilities
    and to contain offload capability policy settings. The network policy logic is
    built on a two-level inheritance scheme which requires that all settings be
    optional. As a result, all properties on the NetOffloadCapabilities object must
    be optional.See HostNetworkPolicy'''
    
    obj = vim.client.factory.create('ns0:HostNetOffloadCapabilities')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'csumOffload', 'tcpSegmentation', 'zeroCopyXmit' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    