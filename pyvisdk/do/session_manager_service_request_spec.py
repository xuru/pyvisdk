
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def SessionManagerServiceRequestSpec(vim, *args, **kwargs):
    '''This data object type describes a request to a service. It is used as argument
    to AcquireGenericServiceTicket. This is the base class for more specific
    service request specifications. E.g. for HTTP services the derived class will
    provide a URL property.'''
    
    obj = vim.client.factory.create('ns0:SessionManagerServiceRequestSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    