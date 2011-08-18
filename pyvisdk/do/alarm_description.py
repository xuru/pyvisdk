# -*- coding: ascii -*-

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AlarmDescription(vim, *args, **kwargs):
    '''Static strings for alarms.'''
    
    obj = vim.client.factory.create('ns0:AlarmDescription')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 10:
        raise IndexError('Expected at least 0 arguments got: %d' % len(args))
        
    args_list = [ 'action', 'datastoreConnectionState', 'entityStatus', 'expr',
        'hostSystemConnectionState', 'hostSystemPowerState', 'metricOperator',
        'stateOperator', 'virtualMachineGuestHeartbeatStatus',
        'virtualMachinePowerState' ]
    
    for name, arg in zip(args_list, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        setattr(obj, name, value)

    return obj
    