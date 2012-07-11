
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostConnectInfo(vim, *args, **kwargs):
    '''This data object type contains information about a single host that can be used
    by the connection wizard. This can be returned without adding the host to
    VirtualCenter.'''
    
    obj = vim.client.factory.create('ns0:HostConnectInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'host' ]
    optional = [ 'clusterSupported', 'datastore', 'inDasCluster', 'license', 'network',
        'serverIp', 'vimAccountNameRequired', 'vm', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    