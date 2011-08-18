# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

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
        raise IndexError('Expected at least 1 arguments got: %d' % len(args))
        
    signature = [  ]
    inherited = [ 'guiRunOnce', 'guiUnattended', 'identification', 'licenseFilePrintData',
        'userData' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    