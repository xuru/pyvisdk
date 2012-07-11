
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DatastoreFileEvent(vim, *args, **kwargs):
    '''Base class for events related to datastore file and directory
    operations.Property inherited from DatastoreEvent refers to the destination
    datastore in case there is more than datastore involved in the operation.'''
    
    obj = vim.client.factory.create('ns0:DatastoreFileEvent')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'targetFile', 'chainId', 'createdTime', 'key', 'userName' ]
    optional = [ 'datastore', 'changeTag', 'computeResource', 'datacenter', 'ds', 'dvs',
        'fullFormattedMessage', 'host', 'net', 'vm', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    