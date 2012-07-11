
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterDrsVmConfigSpec(vim, *args, **kwargs):
    '''Updates the per-virtual-machine DRS configuration.To update the DRS
    configuration of a virtual machine, a copy of this object is included in the
    ClusterConfigSpecEx object passed to the method
    ReconfigureComputeResource_Task.If is used to incrementally update the cluster
    configuration (i.e., the parameter is true), then three operations are provided
    for updating the DRS configuration for a virtual machine. These operations are
    listed below (see ArrayUpdateSpec for more information on these operations).*
    add: add a configuration for the virtual machine, overwritting the existing
    configuration if one exists * edit: incrmentally update the existing
    configuration; an existing configuration must exist * remove: remove the
    existing configuration; an existing configuration must existIf, instead, this
    method is used to overwrite the cluster configuration (i.e., the parameter is
    false) thereby creating a new configuration, only the add operation is allowed.
    In this case, creates a DRS configuration for a virtual machine in the new
    cluster configuration.'''
    
    obj = vim.client.factory.create('ns0:ClusterDrsVmConfigSpec')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))

    required = [ 'operation' ]
    optional = [ 'info', 'removeKey', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    