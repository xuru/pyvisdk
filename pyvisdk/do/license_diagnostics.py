# -*- coding: ascii -*-

import logging

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
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'lastStatusUpdate', 'licenseFeatureUnknowns', 'licenseRequestFailures',
        'licenseRequests', 'opFailureMessage', 'opState', 'sourceLastChanged',
        'sourceLatency', 'sourceLost' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    