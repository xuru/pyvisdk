
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def TicketedSessionAuthentication(vim, *args, **kwargs):
    '''TicketedSessionAuthentication contains the information necessary to use
    previously obtained credentials in the guest. The ticketed session is not
    stateless and stores state inside of the guest.A TicketedSessionAuthentication
    object will be returned as the result of a successful call to
    AcquireCredentialsInGuest. You can use this object in any guest operations
    function call.When you no longer need the TicketedSessionAuthentication object,
    you should call ReleaseCredentialsInGuest to free associated resources and
    session data.'''
    
    obj = vim.client.factory.create('ns0:TicketedSessionAuthentication')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'ticket', 'interactiveSession' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    