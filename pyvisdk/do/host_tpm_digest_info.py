
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostTpmDigestInfo(vim, *args, **kwargs):
    '''This data object type describes the digest values in the Platform Configuration
    Register (PCR) of a Trusted Platform Module (TPM) device.'''
    
    obj = vim.client.factory.create('ns0:HostTpmDigestInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'pcrNumber', 'digestMethod', 'digestValue' ]
    optional = [ 'objectName', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    