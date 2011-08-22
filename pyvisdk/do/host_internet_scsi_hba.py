
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostInternetScsiHba(vim, *args, **kwargs):
    '''This data object type describes the iSCSI host bus adapter interface.'''
    
    obj = vim.client.factory.create('ns0:HostInternetScsiHba')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 12:
        raise IndexError('Expected at least 13 arguments got: %d' % len(args))
        
    signature = [ 'bus', 'device', 'model', 'status', 'authenticationCapabilities',
        'authenticationProperties', 'discoveryCapabilities', 'discoveryProperties',
        'ipCapabilities', 'ipProperties', 'iScsiName', 'isSoftwareBased' ]
    inherited = [ 'driver', 'key', 'pci', 'advancedOptions', 'configuredSendTarget',
        'configuredStaticTarget', 'currentSpeedMb', 'digestCapabilities',
        'digestProperties', 'iScsiAlias', 'maxSpeedMb', 'supportedAdvancedOptions' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    