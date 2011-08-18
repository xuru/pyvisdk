# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDatastoreBrowserSearchResults(vim, *args, **kwargs):
    '''This data object type contains the results of a search method for one
    datastore. A search method typically returns a set of these objects as an
    array.'''
    
    obj = vim.client.factory.create('ns0:HostDatastoreBrowserSearchResults')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'datastore', 'file', 'folderPath' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    