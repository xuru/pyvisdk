
import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def LicenseDiagnostics(vim, *args, **kwargs):
    '''This data object type provides summary status and diagnostic information for
    LicenseManager. Counters in this property can be reset to zero. The property
    specified as a discontinuity is used to determine when this last occurred.'''
    
    obj = vim.client.factory.create('ns0:LicenseDiagnostics')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 9:
        raise IndexError('Expected at least 10 arguments got: %d' % len(args))

    required = [ 'lastStatusUpdate', 'licenseFeatureUnknowns', 'licenseRequestFailures',
        'licenseRequests', 'opFailureMessage', 'opState', 'sourceLastChanged',
        'sourceLatency', 'sourceLost' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    