
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineFileLayoutEx(vim, *args, **kwargs):
    '''Detailed description of files that make up a virtual machine on disk. The file
    layout is broken into 4 major sections:* Configuration: Files stored in the
    configuration directory * Log: Files stored in the log directory * Disk: Files
    stored relative to a disk configuration file * Snapshot: Stored in the snapshot
    directoryOften the same directory is used for configuration, log, disk and
    snapshots.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineFileLayoutEx')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'timestamp' ]
    optional = [ 'disk', 'file', 'snapshot', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    