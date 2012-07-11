
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineConfigSummary(vim, *args, **kwargs):
    '''A subset of virtual machine configuration.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineConfigSummary')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'name', 'template', 'vmPathName' ]
    optional = [ 'annotation', 'cpuReservation', 'ftInfo', 'guestFullName', 'guestId',
        'installBootRequired', 'instanceUuid', 'managedBy', 'memoryReservation',
        'memorySizeMB', 'numCpu', 'numEthernetCards', 'numVirtualDisks', 'product',
        'uuid', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    