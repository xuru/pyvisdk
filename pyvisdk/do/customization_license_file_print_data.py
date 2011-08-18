# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationLicenseFilePrintData(vim, *args, **kwargs):
    '''The LicenseFilePrintData type maps directly to the LicenseFilePrintData key in
    the answer file. These values are transferred into the file that VirtualCenter
    stores on the target virtual disk. For more detailed information, see the
    document . LicenseFilePrintData provides licensing information for Windows
    server operating systems.'''
    
    obj = vim.client.factory.create('ns0:CustomizationLicenseFilePrintData')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'autoMode', 'autoUsers' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    