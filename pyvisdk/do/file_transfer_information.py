
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def FileTransferInformation(vim, *args, **kwargs):
    '''Represents the information about a InitiateFileTransferFromGuest operation of
    GuestFileManager object.The user can use the URL provided in url property to
    transfer the file from the guest. The user should send a HTTP GET request to
    the URL. Entire file content will be returned in the body of the response
    message.'''
    
    obj = vim.client.factory.create('ns0:FileTransferInformation')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'attributes', 'size', 'url' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    