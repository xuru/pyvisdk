
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterVmToolsMonitoringSettings(vim, *args, **kwargs):
    '''vSphere HA Virtual Machine Health Monitoring service setting.Virtual Machine
    Health Monitoring service checks the VMware Tools heartbeat of a virtual
    machine. If heartbeats have not been received within a specified time interval,
    Virtual Machine Health Monitoring service declares the virtual machine as
    failed and resets the virtual machine.VmToolsMonitoringSetting consists of
    configuration settings for Virtual Machine Health Monitoring Service.All fields
    are defined as optional. In case of a reconfiguration, fields left unset are
    not changed.'''
    
    obj = vim.client.factory.create('ns0:ClusterVmToolsMonitoringSettings')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))

    required = [  ]
    optional = [ 'clusterSettings', 'enabled', 'failureInterval', 'maxFailures',
        'maxFailureWindow', 'minUpTime', 'vmMonitoring', 'dynamicProperty',
        'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    