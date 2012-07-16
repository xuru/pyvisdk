
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def SessionManagerGenericServiceTicket(vim, *args, **kwargs):
    '''This data object represents a ticket which grants access to some service. The
    ticket may be used only once and is valid only for the
    SessionManagerServiceRequestSpec with which it was acquired. For HTTP service
    requests (when spec is of type HttpServiceRequestSpec) the returned ticket must
    be used by setting id as the value of a special cookie in the HTTP request. For
    CGI requests the name of this cookie is 'vmware_cgi_ticket'. The use of the
    returned ticket for other services is to be defined.'''
    
    obj = vim.client.factory.create('ns0:SessionManagerGenericServiceTicket')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'id' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    