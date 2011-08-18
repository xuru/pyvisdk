# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VirtualMachineConfigOption(vim, *args, **kwargs):
    '''This configuration data object type contains information about the execution
    environment for a virtual machine. This includes information about which
    features are supported, such as:* Which guest operating systems are supported.
    * How devices are emulated. For example, that a CD-ROM drive can be emulated
    with a file or that a serial port can be emulated with a pipe.VirtualCenter can
    provide a broader environment than any single physical host. This is a
    departure from traditional virtualization approaches, which rely on the host
    system to define the environment for virtual machines. This data object
    describes environment capabilities and is used by VirtualCenter to choose hosts
    on which to run virtual machines.'''
    
    obj = vim.client.factory.create('ns0:VirtualMachineConfigOption')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))
        
    signature = [ 'capabilities', 'datastore' ]
    inherited = [ 'defaultDevice', 'description', 'guestOSDefaultIndex', 'guestOSDescriptor',
        'hardwareOptions', 'supportedMonitorType', 'supportedOvfEnvironmentTransport',
        'supportedOvfInstallTransport', 'version' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    