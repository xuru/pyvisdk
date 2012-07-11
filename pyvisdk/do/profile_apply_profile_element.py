
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ProfileApplyProfileElement(vim, *args, **kwargs):
    '''DataObject which represents an ApplyProfile element. An ApplyProfile element is
    an ApplyProfile for a set of host configuration settings which may be
    instanced. For example, there may be multiple virtual switch instances
    represented by individual ApplyProfileElement DataObjects.'''
    
    obj = vim.client.factory.create('ns0:ProfileApplyProfileElement')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'key', 'enabled' ]
    optional = [ 'policy', 'profileTypeName', 'profileVersion', 'property', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    