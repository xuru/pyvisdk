
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def OvfFile(vim, *args, **kwargs):
    '''Represents a file that the caller has downloaded and stored somewhere
    appropriate.An instance of this class is used to tell OvfManager about the
    choices the caller made about a file. This information is needed when the OVF
    descriptor is generated with createDescriptor.'''
    
    obj = vim.client.factory.create('ns0:OvfFile')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'deviceId', 'path', 'size' ]
    optional = [ 'capacity', 'chunkSize', 'compressionMethod', 'populatedSize',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    