
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

    required = [ 'authenticationCapabilities', 'authenticationProperties',
        'discoveryCapabilities', 'discoveryProperties', 'ipCapabilities',
        'ipProperties', 'iScsiName', 'isSoftwareBased', 'bus', 'device', 'model',
        'status' ]
    optional = [ 'advancedOptions', 'canBeDisabled', 'configuredSendTarget',
        'configuredStaticTarget', 'currentSpeedMb', 'digestCapabilities',
        'digestProperties', 'iScsiAlias', 'maxSpeedMb', 'networkBindingSupport',
        'supportedAdvancedOptions', 'driver', 'key', 'pci', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    