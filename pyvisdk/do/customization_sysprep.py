# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def CustomizationSysprep(vim, *args, **kwargs):
    '''An object representation of a Windows answer file. The sysprep type encloses
    all the individual keys listed in a file. For more detailed information, see
    the document .'''
    
    obj = vim.client.factory.create('ns0:CustomizationSysprep')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'guiRunOnce', 'guiUnattended', 'identification', 'licenseFilePrintData',
        'userData' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    