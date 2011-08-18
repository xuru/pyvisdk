# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AlarmInfo(vim, *args, **kwargs):
    '''Attributes of an alarm.'''
    
    obj = vim.client.factory.create('ns0:AlarmInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 6:
        raise IndexError('Expected at least 7 arguments got: %d' % len(args))
        
    signature = [ 'alarm', 'creationEventId', 'entity', 'key', 'lastModifiedTime',
        'lastModifiedUser' ]
    inherited = [ 'action', 'actionFrequency', 'description', 'enabled', 'expression', 'name',
        'setting' ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    