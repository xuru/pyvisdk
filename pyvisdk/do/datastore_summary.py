
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DatastoreSummary(vim, *args, **kwargs):
    '''Summary information about the datastore. The status fields and managed object
    reference is not set when an object of this type is created. These fields and
    references are typically set later when these objects are associated with a
    host.'''
    
    obj = vim.client.factory.create('ns0:DatastoreSummary')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 7 arguments got: %d' % len(args))

    required = [ 'accessible', 'capacity', 'freeSpace', 'name', 'type', 'url' ]
    optional = [ 'datastore', 'maintenanceMode', 'multipleHostAccess', 'uncommitted',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    