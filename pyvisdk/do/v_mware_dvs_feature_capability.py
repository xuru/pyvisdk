
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def VMwareDVSFeatureCapability(vim, *args, **kwargs):
    '''Indicators of support for version-specific DVS features that are only available
    on a VMware-class switch.'''
    
    obj = vim.client.factory.create('ns0:VMwareDVSFeatureCapability')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))
        
    signature = [ 'networkResourceManagementSupported', 'vmDirectPathGen2Supported' ]
    inherited = [ 'networkResourcePoolHighShareValue', 'nicTeamingPolicy' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    