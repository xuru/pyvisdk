
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def SendEmailAction(vim, *args, **kwargs):
    '''This data object type defines an email that is triggered by an alarm. You can
    use any elements of the ActionParameter enumerated list as part of your strings
    to provide information available at runtime.'''
    
    obj = vim.client.factory.create('ns0:SendEmailAction')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'body', 'ccList', 'subject', 'toList' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    