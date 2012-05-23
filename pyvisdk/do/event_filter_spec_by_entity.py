
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def EventFilterSpecByEntity(vim, *args, **kwargs):
    '''This option specifies a managed entity used to filter event history. If the
    specified managed entity is a Folder or a ResourcePool, the query will actually
    be performed on the entities contained within that Folder or ResourcePool, so
    you cannot query for events on Folders and ResourcePools themselves this way.'''
    
    obj = vim.client.factory.create('ns0:EventFilterSpecByEntity')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'entity', 'recursion' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    