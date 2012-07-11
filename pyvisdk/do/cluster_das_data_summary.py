
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ClusterDasDataSummary(vim, *args, **kwargs):
    '''This class contains the summary of the data that DAS needs/uses. The actual
    data is available in ClusterDasDataDetails and can be retrieved using the
    RetrieveDasData method. This class is meant for VMware internal use only.'''
    
    obj = vim.client.factory.create('ns0:ClusterDasDataSummary')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))

    required = [ 'clusterConfigVersion', 'compatListVersion', 'hostListVersion' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    