
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AboutInfo(vim, *args, **kwargs):
    '''This data object type describes system information including the name, type,
    version, and build number.'''
    
    obj = vim.client.factory.create('ns0:AboutInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 9:
        raise IndexError('Expected at least 10 arguments got: %d' % len(args))
        
    signature = [ 'apiType', 'apiVersion', 'build', 'fullName', 'name', 'osType',
        'productLineId', 'vendor', 'version' ]
    inherited = [ 'instanceUuid', 'licenseProductName', 'licenseProductVersion', 'localeBuild',
        'localeVersion' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    