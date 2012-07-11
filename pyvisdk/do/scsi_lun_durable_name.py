
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ScsiLunDurableName(vim, *args, **kwargs):
    '''This data object type represents an SMI-S "Correlatable and Durable Name" which
    is an identifier for a logical unit number (LUN) that is generated using a
    common algorithm. The algorithm divides the identifier into multiple namespaces
    where each namespace uses a different set of properties of the LUN to generate
    the identifier. The namespace itself is encoded in the identifier.'''
    
    obj = vim.client.factory.create('ns0:ScsiLunDurableName')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'namespace', 'namespaceId' ]
    optional = [ 'data', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    