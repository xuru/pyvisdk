
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostServiceTicket(vim, *args, **kwargs):
    '''For example, when a client requests a ticket from an ESX Server, the returned
    ticket may omit the optional host and port. In such a case, the client
    establishes an out-of-band ticketed connection to the same server host and on
    the same port on which it made the connection to request the ticket. If this
    request is made to the VirtualCenter server, but the server does not provide
    the required service directly, then the server provides a hostname and port for
    a server that accepts the ticketed connection and provides the service.'''
    
    obj = vim.client.factory.create('ns0:HostServiceTicket')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))
        
    signature = [ 'service', 'serviceVersion', 'sessionId' ]
    inherited = [ 'host', 'port', 'sslThumbprint' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    