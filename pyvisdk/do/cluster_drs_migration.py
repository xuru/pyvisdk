
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterDrsMigration(vim, *args, **kwargs):
    '''Describes a single virtual machine migration.'''
    
    obj = vim.client.factory.create('ns0:ClusterDrsMigration')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'destination', 'key', 'source', 'time', 'vm' ]
    optional = [ 'cpuLoad', 'destinationCpuLoad', 'destinationMemoryLoad', 'memoryLoad',
        'sourceCpuLoad', 'sourceMemoryLoad', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    