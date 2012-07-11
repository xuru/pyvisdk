
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostServiceTicket(vim, *args, **kwargs):
    '''Return value for ticketable host services. The server has the option to provide
    a hostname and port for a future ticket-authenticated connection to a service
    on a host. If the service provider does not return a host the client must
    connect to the same host it used to request the ticket. In case the service
    provider does not return a port, except in the case of connecting to CIM
    interfaces, the client must connect using the same port it used to request the
    ticket. In the case of connecting to a CIM interface the standard well known
    port number for the particular service will be used for the connection.For
    example, when a client requests a ticket from an ESX Server, the returned
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

    required = [ 'service', 'serviceVersion', 'sessionId' ]
    optional = [ 'host', 'port', 'sslThumbprint', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    