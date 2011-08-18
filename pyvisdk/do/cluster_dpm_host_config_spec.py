# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterDpmHostConfigSpec(vim, *args, **kwargs):
    '''The ClusterDpmHostConfigSpec data object provides information that the Server
    uses to update the DPM configuration for a single host (identified by the key
    property). The host DPM configuration overrides the cluster default DPM setting
    (ClusterConfigSpecEx.dpmConfig).The vSphere API defines three update operations
    (ArrayUpdateSpec.operation).Use the ReconfigureComputeResource_Task method to
    update the DPM configuration. If you set the modify parameter to true, you can
    use any of the three operations (add, edit, or remove). If you set the modify
    parameter to false, you can use only the add operation.'''
    
    obj = vim.client.factory.create('ns0:ClusterDpmHostConfigSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'operation' ]
    inherited = [ 'removeKey', 'info' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    