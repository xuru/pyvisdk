
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def NamePasswordAuthentication(vim, *args, **kwargs):
    '''NamePasswordAuthentication contains the information necessary to authenticate
    within a guest using a name and password. This is the typical method for
    authentication within a guest and the one currently used by VIX. This method of
    authentication is stateless.To use NamePasswordAuthentication, populate
    username and password with the appropriate login information. You should not
    use AcquireCredentialsInGuest or ReleaseCredentialsInGuest for
    NamePasswordAuthentication.Once populated, you can use
    NamePasswordAuthentication in any guest operations function call.'''
    
    obj = vim.client.factory.create('ns0:NamePasswordAuthentication')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'password', 'username', 'interactiveSession' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    