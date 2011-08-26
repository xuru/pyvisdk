
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ServiceConsoleReservationInfo(vim, *args, **kwargs):
    '''This memory that is reserved for the service console is used primarily to
    provide system management services. In addition, a small overhead is needed by
    each virtual machine on the service console.The only property of the data
    object that can be changed directly is the serviceConsoleReservedCfg property.
    This property indicates how much memory should be reserved for the service
    console on the next boot. In most cases, this amount is the same as the current
    reservation.'''
    
    obj = vim.client.factory.create('ns0:ServiceConsoleReservationInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))
        
    signature = [ 'serviceConsoleReserved', 'serviceConsoleReservedCfg', 'unreserved' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    