
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def FileQueryFlags(vim, *args, **kwargs):
    '''The FileInfo.Details data object type is a set of flags for a search request.
    This search request specifies which details to return for each matching file.
    This data object type is here to ensure that there is one flag corresponding to
    each FileInfo property other than the path name, which a search always returns.'''
    
    obj = vim.client.factory.create('ns0:FileQueryFlags')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'fileOwner', 'fileSize', 'fileType', 'modification' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    