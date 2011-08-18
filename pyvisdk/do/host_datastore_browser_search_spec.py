# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def HostDatastoreBrowserSearchSpec(vim, *args, **kwargs):
    '''The data object type describes a search for files in one or more datastores.
    The properties do not include the starting datastore path because that path is
    a separate parameter to the search method.A SearchSpec contains the query
    parameters and some global search modifiers.'''
    
    obj = vim.client.factory.create('ns0:HostDatastoreBrowserSearchSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 0:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'details', 'matchPattern', 'query', 'searchCaseInsensitive', 'sortFoldersFirst' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    