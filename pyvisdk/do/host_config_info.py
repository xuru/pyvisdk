# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostConfigInfo(vim, *args, **kwargs):
    '''This data object type encapsulates a typical set of host configuration
    information that is useful for displaying and configuring a host.VirtualCenter
    can retrieve this set of information very efficiently even for a large set of
    hosts.'''
    
    obj = vim.client.factory.create('ns0:HostConfigInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'activeDiagnosticPartition', 'adminDisabled', 'authenticationManagerInfo',
        'autoStart', 'capabilities', 'consoleReservation', 'datastoreCapabilities',
        'datastorePrincipal', 'dateTimeInfo', 'featureVersion', 'fileSystemVolume',
        'firewall', 'flags', 'host', 'hyperThread', 'ipmi', 'localSwapDatastore',
        'multipathState', 'network', 'offloadCapabilities', 'option', 'optionDef',
        'pciPassthruInfo', 'powerSystemCapability', 'powerSystemInfo', 'product',
        'service', 'sslThumbprintInfo', 'storageDevice', 'systemFile',
        'systemResources', 'virtualMachineReservation', 'virtualNicManagerInfo',
        'vmotion' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    