
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ToolsConfigInfo(vim, *args, **kwargs):
    '''ToolsConfigInfo is a data object type containing settings for the VMware Tools
    software running in the guest operating system.'''
    
    obj = vim.client.factory.create('ns0:ToolsConfigInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'afterPowerOn', 'afterResume', 'beforeGuestReboot', 'beforeGuestShutdown',
        'beforeGuestStandby', 'lastInstallInfo', 'pendingCustomization',
        'syncTimeWithHost', 'toolsUpgradePolicy', 'toolsVersion', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    