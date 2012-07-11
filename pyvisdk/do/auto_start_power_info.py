
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
    virtual machine before starting the next virtual machine in the sequence.* For
    a power-on operation, if waitForHeartbeat is true, then the power-on sequence
    continues after the first heartbeat has been received. If waitForHeartbeat is
    false, the system waits for the specified delay and then continues the power-on
    sequence. * For a power-off operation, if delay is non-zero, the requested
    power-off action is invoked (powerOff, suspend, guestShutdown) on the virtual
    machine and the system waits until the number of seconds specified in the delay
    have passed.If startAction and stopAction for a virtual machine are both set to
    none, that virtual machine is removed from the AutoStart sequence. Virtual
    machines can be configured both to wait for a period of time before starting
    and to wait for a heartbeat. In such a case, the waiting virtual machine only
    waits until either of these conditions are met. In other words, a virtual
    machine starts in either of the following cases:* After receiving a heartbeat
    but before the start delay has elapsed * After the start delay has elapsed but
    before receiving a heartbeatThis provides a better experience since as soon as
    one virtual machine begins sending heartbeats, indicating it has successfully
    started up, the next machine will begin starting up. This happens even if the
    startDelay has not yet elapsed. Similarly, if one virtual machine fails to
    begin sending heartbeats, perhaps because it could not start up, other machines
    are not blocked from starting up since the startDelay eventually elapses.'''
    
    obj = vim.client.factory.create('ns0:AutoStartPowerInfo')

    # do some validation checking...
    if (len(args) + len(kwargs)) < 7:
        raise IndexError('Expected at least 8 arguments got: %d' % len(args))

    required = [ 'key', 'startAction', 'startDelay', 'startOrder', 'stopAction', 'stopDelay',
        'waitForHeartbeat' ]
    optional = [ 'dynamicProperty', 'dynamicType' ]

    for name, arg in zip(required+optional, args):
        setattr(obj, name, arg)

    for name, value in kwargs.items():
        if name in required + optional:
            setattr(obj, name, value)
        else:
            raise InvalidArgumentError("Invalid argument: %s.  Expected one of %s" % (name, ", ".join(required + optional)))

    return obj
    