
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostMultipathInfoPath(vim, *args, **kwargs):
    '''The HostMultipathInfoPath data object is a storage entity that represents a
    topological path from a host bus adapter to a SCSI logical unit. Each path is
    unique although each host bus adapter/SCSI logical unit pair can have multiple
    paths.Path objects are identified by a key. The specifics of how the key is
    formatted are dependent on the implementation. Example implementations include
    using strings like "vmhba1:0:0:0".'''
    
    obj = vim.client.factory.create('ns0:HostMultipathInfoPath')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'adapter', 'key', 'lun', 'name', 'pathState' ]
    optional = [ 'isWorkingPath', 'state', 'transport', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    