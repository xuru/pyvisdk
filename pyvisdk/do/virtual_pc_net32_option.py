
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualPCNet32Option(vim, *args, **kwargs):
    '''The VirtualPCNet32Option data object type defines the options for the
    VirtualPCNet32 data object type. Except for the boolean supportsMorphing
    option, the options are inherited from the VirtualEthernetCardOption data
    object type.'''
    
    obj = vim.client.factory.create('ns0:VirtualPCNet32Option')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 9:
        raise IndexError('Expected at least 10 arguments got: %d' % len(args))
        
    signature = [ 'deprecated', 'hotRemoveSupported', 'plugAndPlay', 'type', 'macType',
        'supportedOUI', 'vmDirectPathGen2Supported', 'wakeOnLanEnabled',
        'supportsMorphing' ]
    inherited = [ 'autoAssignController', 'backingOption', 'connectOption', 'controllerType',
        'defaultBackingOptionIndex', 'licensingLimit' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    