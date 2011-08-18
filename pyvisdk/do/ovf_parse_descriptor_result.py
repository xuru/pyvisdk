# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def OvfParseDescriptorResult(vim, *args, **kwargs):
    ''''''
    
    obj = vim.client.factory.create('ns0:OvfParseDescriptorResult')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 2 arguments got: %d' % len(args))
        
    signature = [ 'annotation' ]
    inherited = [ 'approximateDownloadSize', 'approximateFlatDeploymentSize',
        'approximateSparseDeploymentSize', 'defaultDeploymentOption',
        'defaultEntityName', 'deploymentOption', 'entityName', 'error', 'eula',
        'ipAllocationScheme', 'ipProtocols', 'network', 'productInfo', 'property_',
        'virtualApp', 'warning' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    