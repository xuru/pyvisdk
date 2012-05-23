
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def UserSession(vim, *args, **kwargs):
    '''Information about a current user session.'''
    
    obj = vim.client.factory.create('ns0:UserSession')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 8:
        raise IndexError('Expected at least 9 arguments got: %d' % len(args))

    required = [ 'extensionSession', 'fullName', 'key', 'lastActiveTime', 'locale', 'loginTime',
        'messageLocale', 'userName' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    