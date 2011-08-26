
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def PhysicalNic(vim, *args, **kwargs):
    ''''''
    
    obj = vim.client.factory.create('ns0:PhysicalNic')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 5:
        raise IndexError('Expected at least 6 arguments got: %d' % len(args))
        
    signature = [ 'device', 'mac', 'pci', 'spec', 'wakeOnLanSupported' ]
    inherited = [ 'autoNegotiateSupported', 'driver', 'key', 'linkSpeed',
        'resourcePoolSchedulerAllowed', 'resourcePoolSchedulerDisallowedReason',
        'validLinkSpecification', 'vmDirectPathGen2Supported',
        'vmDirectPathGen2SupportedMode' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    