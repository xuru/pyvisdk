
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ExtensionOvfConsumerInfo(vim, *args, **kwargs):
    '''This data object contains configuration for extensions that also extend the OVF
    functionality of vCenter server.This feature is experimental in this version of
    the API and might change in future versions.'''
    
    obj = vim.client.factory.create('ns0:ExtensionOvfConsumerInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'callbackUrl', 'sectionType' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    