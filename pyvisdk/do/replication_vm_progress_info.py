
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ReplicationVmProgressInfo(vim, *args, **kwargs):
    '''A set of statistics related to the progress of the current operation (full sync
    or lwd).'''
    
    obj = vim.client.factory.create('ns0:ReplicationVmProgressInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'bytesToTransfer', 'bytesTransferred', 'progress' ]
    optional = [ 'checksumComparedBytes', 'checksumTotalBytes', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    