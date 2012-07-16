
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def FileInfo(vim, *args, **kwargs):
    '''This data object type contains rudimentary information about a file in a
    datastore. The information here is not meant to cover all information in
    traditional file systems, but rather to provide sufficient information for
    files that are associated with virtual machines. Derived types describe the
    known file types for a datastore.'''
    
    obj = vim.client.factory.create('ns0:FileInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'path' ]
    optional = [ 'fileSize', 'modification', 'owner', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    