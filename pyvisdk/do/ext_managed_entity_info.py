
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ExtManagedEntityInfo(vim, *args, **kwargs):
    '''This data object contains information about entities managed by this extension.
    The data can be used by clients to show extra information about managed virtual
    machines or vApps, such as a custom icon and a description of the entity.'''
    
    obj = vim.client.factory.create('ns0:ExtManagedEntityInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'type' ]
    optional = [ 'description', 'smallIconUrl', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    