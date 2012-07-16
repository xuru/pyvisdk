
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def ComputeResourceHostSPBMLicenseInfo(vim, *args, **kwargs):
    '''The ComputeResourceHostSPBMLicenseInfo data object encapsulates the
    SPBM(Storage Policy Based Management) license information for a host.'''
    
    obj = vim.client.factory.create('ns0:ComputeResourceHostSPBMLicenseInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 3 arguments got: %d' % len(args))

    required = [ 'host', 'licenseState' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    