# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def DiagnosticManagerLogHeader(vim, *args, **kwargs):
    '''A header that is returned with a set of log entries. This header describes
    where entries are located in the log file. Log files typically grow
    dynamically, so indexes based on line numbers may become inaccurate.'''
    
    obj = vim.client.factory.create('ns0:DiagnosticManagerLogHeader')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 2:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'lineEnd', 'lineStart', 'lineText' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    