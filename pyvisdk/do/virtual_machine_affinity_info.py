
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineAffinityInfo(vim, *args, **kwargs):
    '''Specification of scheduling affinity.Scheduling affinity is used for explicitly
    specifying which processors or NUMA nodes may be used by a virtual machine.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineAffinityInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'affinitySet' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    