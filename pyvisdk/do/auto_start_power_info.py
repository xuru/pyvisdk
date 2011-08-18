# -*- coding: ascii -*-

import logging
from pyvisdk.exceptions import InvalidArgumentError

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

def AutoStartPowerInfo(vim, *args, **kwargs):
    '''This object type describes the power-on / power-off behavior for a given
    virtual machine. Virtual machines can be configured to wait for a period of
    time before starting or to wait to receive a successful heartbeat from a
    virtual machine before starting the next virtual machine in the sequence.If
    startAction and stopAction for a virtual machine are both set to none, that
    virtual machine is removed from the AutoStart sequence. Virtual machines can be
    configured both to wait for a period of time before starting and to wait for a
    heartbeat. In such a case, the waiting virtual machine only waits until either
    of these conditions are met. In other words, a virtual machine starts in either
    of the following cases:This provides a better experience since as soon as one
    virtual machine begins sending heartbeats, indicating it has successfully
    started up, the next machine will begin starting up. This happens even if the
    startDelay has not yet elapsed. Similarly, if one virtual machine fails to
    begin sending heartbeats, perhaps because it could not start up, other machines
    are not blocked from starting up since the startDelay eventually elapses.'''
    
    obj = vim.client.factory.create('ns0:AutoStartPowerInfo')
    
    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 8 arguments got: %d' % len(args))
        
    signature = [ 'key', 'startAction', 'startDelay', 'startOrder', 'stopAction', 'stopDelay',
        'waitForHeartbeat' ]
    inherited = [  ]
    
    for name, arg in zip(signature+inherited, args):
        setattr(obj, name, arg)
    
    for name, value in kwargs.items():
        if name in signature + inherited:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(signature + inherited)))

    return obj
    