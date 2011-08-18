# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AlarmTriggeringAction(vim, *args, **kwargs):
    '''This data object type describes one or more triggering transitions and an
    action to be done when an alarm is triggered.There are four triggering
    transitions; at least one of them must be provided. A gray state is considered
    the same as a green state, for the purpose of detecting transitions.'''
    
    obj = vim.client.factory.create('ns0:AlarmTriggeringAction')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 3:
        raise IndexError('Expected at least 4 arguments got: %d' % len(args))
        
    signature = [ 'action', 'green2yellow', 'red2yellow' ]
    inherited = [ 'transitionSpecs', 'yellow2green', 'yellow2red' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    