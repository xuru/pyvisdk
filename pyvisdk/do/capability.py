
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def Capability(vim, *args, **kwargs):
    '''Support for some features is indicated by the presence or absence of the
    manager object from the service instance. For example, the AlarmManager manager
    object indicates collecting alarms is supported. Other features indicate
    whether or not a given operation on an object throws a NotSupported fault.Some
    capabilities depend on the host or virtual machine version. These are specified
    by using the vim.host.Capability and vim.vm.Capability objects.'''
    
    obj = vim.client.factory.create('ns0:Capability')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))
        
    signature = [ 'multiHostSupported', 'provisioningSupported', 'userShellAccessSupported' ]
    inherited = [ 'supportedEVCMode' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    