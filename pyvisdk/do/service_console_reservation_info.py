
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ServiceConsoleReservationInfo(vim, *args, **kwargs):
    '''The ServiceConsoleReservationInfo data object type describes the amount of
    memory that is being reserved by the service console. Memory reserved for use
    by the service console is a hard reservation that cannot be changed except
    across hardware restarts.This memory that is reserved for the service console
    is used primarily to provide system management services. In addition, a small
    overhead is needed by each virtual machine on the service console.The only
    property of the data object that can be changed directly is the
    serviceConsoleReservedCfg property. This property indicates how much memory
    should be reserved for the service console on the next boot. In most cases,
    this amount is the same as the current reservation.'''
    
    obj = vim.client.factory.create('ns0:ServiceConsoleReservationInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'serviceConsoleReserved', 'serviceConsoleReservedCfg', 'unreserved' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    