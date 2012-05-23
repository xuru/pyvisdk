
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiskDimensionsChs(vim, *args, **kwargs):
    '''This data object type describes dimensions using the cylinder, head, sector
    (CHS) coordinate system. This coordinate system is generally needed for
    partitioning for legacy reasons. When defining partitions, many partitioning
    utilities do not function correctly when certain CHS constraints are not met.'''
    
    obj = vim.client.factory.create('ns0:HostDiskDimensionsChs')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'cylinder', 'head', 'sector' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    