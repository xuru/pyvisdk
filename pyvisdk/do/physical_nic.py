
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PhysicalNic(vim, *args, **kwargs):
    '''This data object type describes the physical network adapter as seen by the
    primary operating system.'''
    
    obj = vim.client.factory.create('ns0:PhysicalNic')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))

    required = [ 'device', 'mac', 'pci', 'spec', 'wakeOnLanSupported' ]
    optional = [ 'autoNegotiateSupported', 'driver', 'fcoeConfiguration', 'key', 'linkSpeed',
        'resourcePoolSchedulerAllowed', 'resourcePoolSchedulerDisallowedReason',
        'validLinkSpecification', 'vmDirectPathGen2Supported',
        'vmDirectPathGen2SupportedMode', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    