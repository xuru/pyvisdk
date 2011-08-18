# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AlarmTriggeringActionTransitionSpec(vim, *args, **kwargs):
    '''Specification indicating which on transitions this action fires. The existence
    of a Spec indicates that this action fires on transitions from that Spec's
    startState to finalState.There are only four acceptable {startState,
    finalState} pairs: {green, yellow}, {yellow, red}, {red, yellow} and {yellow,
    green}. At least one of these pairs must be specified. Any deviation from the
    above will render the enclosing AlarmSpec invalid.'''
    
    obj = vim.client.factory.create('ns0:AlarmTriggeringActionTransitionSpec')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'finalState', 'repeats', 'startState' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    