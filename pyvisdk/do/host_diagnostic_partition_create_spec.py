
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDiagnosticPartitionCreateSpec(vim, *args, **kwargs):
    '''The diagnostic create specification is used by the system to create a new
    diagnostic partition on a SCSI disk.'''
    
    obj = vim.client.factory.create('ns0:HostDiagnosticPartitionCreateSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'diagnosticType', 'id', 'partition', 'storageType' ]
    optional = [ 'active', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    