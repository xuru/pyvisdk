
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def FaultToleranceSecondaryConfigInfo(vim, *args, **kwargs):
    '''FaultToleranceSecondaryConfigInfo is a data object type containing Fault
    Tolerance settings for a secondary virtual machine in a fault tolerance group'''
    
    obj = vim.client.factory.create('ns0:FaultToleranceSecondaryConfigInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'primaryVM', 'configPaths', 'instanceUuids', 'role' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    