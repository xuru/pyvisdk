
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def Capability(vim, *args, **kwargs):
    '''A particular product may or may not support certain features. This data object
    indicates whether or not a service instance implements these features. This
    data object type indicates the circumstances under which an operation throws a
    NotSupported fault.Support for some features is indicated by the presence or
    absence of the manager object from the service instance. For example, the
    AlarmManager manager object indicates collecting alarms is supported. Other
    features indicate whether or not a given operation on an object throws a
    NotSupported fault.Some capabilities depend on the host or virtual machine
    version. These are specified by using the vim.host.Capability and
    vim.vm.Capability objects.'''
    
    obj = vim.client.factory.create('ns0:Capability')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'multiHostSupported', 'provisioningSupported', 'userShellAccessSupported' ]
    optional = [ 'supportedEVCMode', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    