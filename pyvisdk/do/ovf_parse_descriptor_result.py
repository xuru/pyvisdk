
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
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 5 arguments got: %d' % len(args))

    required = [ 'annotation', 'defaultDeploymentOption', 'defaultEntityName', 'virtualApp' ]
    optional = [ 'annotatedOst', 'approximateDownloadSize', 'approximateFlatDeploymentSize',
        'approximateSparseDeploymentSize', 'deploymentOption', 'entityName', 'error',
        'eula', 'ipAllocationScheme', 'ipProtocols', 'network', 'productInfo',
        'property', 'warning', 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    