# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def RunScriptAction(vim, *args, **kwargs):
    '''This data object type specifies a script that is triggered by an alarm. You can
    use any elements of the ActionParameter enumerated list as part of your script
    to provide information available at runtime.'''
    
    obj = vim.client.factory.create('ns0:RunScriptAction')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 1:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'script' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    