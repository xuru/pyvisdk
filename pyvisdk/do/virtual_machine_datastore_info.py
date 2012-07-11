
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineDatastoreInfo(vim, *args, **kwargs):
    '''DatastoreInfo describes a datastore that a virtual disk can be stored on.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineDatastoreInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'capability', 'datastore', 'maxFileSize', 'mode', 'name' ]
    optional = [ 'vStorageSupport', 'configurationTag', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    