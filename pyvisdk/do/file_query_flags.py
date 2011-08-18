# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def FileQueryFlags(vim, *args, **kwargs):
    '''The FileInfo.Details data object type is a set of flags for a search request.
    This search request specifies which details to return for each matching file.
    This data object type is here to ensure that there is one flag corresponding to
    each FileInfo property other than the path name, which a search always returns.'''
    
    obj = vim.client.factory.create('ns0:FileQueryFlags')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 4:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'fileOwner', 'fileSize', 'fileType', 'modification' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    