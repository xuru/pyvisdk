
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDatastoreBrowserSearchSpec(vim, *args, **kwargs):
    '''The data object type describes a search for files in one or more datastores.
    The properties do not include the starting datastore path because that path is
    a separate parameter to the search method.A SearchSpec contains the query
    parameters and some global search modifiers.'''
    
    obj = vim.client.factory.create('ns0:HostDatastoreBrowserSearchSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'details', 'matchPattern', 'query', 'searchCaseInsensitive',
        'sortFoldersFirst', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    