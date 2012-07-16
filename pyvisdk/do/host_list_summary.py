
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostListSummary(vim, *args, **kwargs):
    '''This data object type encapsulates a typical set of host information that is
    useful for list views and summary pages.VirtualCenter can retrieve this
    information very efficiently, even for a large set of hosts.'''
    
    obj = vim.client.factory.create('ns0:HostListSummary')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'config', 'overallStatus', 'quickStats', 'rebootRequired' ]
    optional = [ 'currentEVCModeKey', 'customValue', 'hardware', 'host', 'managementServerIp',
        'maxEVCModeKey', 'runtime', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    