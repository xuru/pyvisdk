
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ImportSpec(vim, *args, **kwargs):
    '''An ImportSpec is used when importing VMs or vApps.It can be built from scratch,
    or it can be generated from an OVF descriptor using the service interface
    OvfManager.This class is the abstract base for VirtualMachineImportSpec and
    VirtualAppImportSpec. These three classes form a composite structure that
    allows us to contain arbitrarily complex entitites in a single ImportSpec.'''
    
    obj = vim.client.factory.create('ns0:ImportSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'entityConfig', 'instantiationOst', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    