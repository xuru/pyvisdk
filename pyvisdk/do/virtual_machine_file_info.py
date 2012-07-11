
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineFileInfo(vim, *args, **kwargs):
    '''The FileInfo data object type contains the locations of virtual machine files
    other than the virtual disk files. The configurable parameters are all in the
    FileInfo object.The object also contains a FileLayout object that returns a
    complete list of additional files that makes up the virtual machine
    configuration. This is a read-only structure and is returned when the
    configuration is read. This is ignored during configuration and can be left
    out.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineFileInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'logDirectory', 'snapshotDirectory', 'suspendDirectory', 'vmPathName',
        'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    