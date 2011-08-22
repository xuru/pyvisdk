
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostConnectSpec(vim, *args, **kwargs):
    '''Specifies the parameters needed to add a single host. This includes a small set
    of optional information about the host configuration. This allows the network
    and datastore configuration of the host to be synchronized with the naming
    conventions of the datacenter, as well as the configuration of a vim account
    (the username/password for the virtual machine files that is created on disk).'''
    
    obj = vim.client.factory.create('ns0:HostConnectSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'force' ]
    inherited = [ 'hostName', 'managementIp', 'password', 'port', 'sslThumbprint', 'userName',
        'vimAccountName', 'vimAccountPassword', 'vmFolder' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    