
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AutoStartPowerInfo(DynamicData):
    '''This object type describes the power-on / power-off behavior for a given virtual
        machine. Virtual machines can be configured to wait for a period of time
        before starting or to wait to receive a successful heartbeat from a
        virtual machine before starting the next virtual machine in the sequence.*
        For a power-on operation, if waitForHeartbeat is true, then the power-on
        sequence continues after the first heartbeat has been received. If
        waitForHeartbeat is false, the system waits for the specified delay and
        then continues the power-on sequence. * For a power-off operation, if
        delay is non-zero, the requested power-off action is invoked (powerOff,
        suspend, guestShutdown) on the virtual machine and the system waits until
        the number of seconds specified in the delay have passed.If startAction
        and stopAction for a virtual machine are both set to none, that virtual
        machine is removed from the AutoStart sequence. Virtual machines can be
        configured both to wait for a period of time before starting and to wait
        for a heartbeat. In such a case, the waiting virtual machine only waits
        until either of these conditions are met. In other words, a virtual
        machine starts in either of the following cases:* After receiving a
        heartbeat but before the start delay has elapsed * After the start delay
        has elapsed but before receiving a heartbeatThis provides a better
        experience since as soon as one virtual machine begins sending heartbeats,
        indicating it has successfully started up, the next machine will begin
        starting up. This happens even if the startDelay has not yet elapsed.
        Similarly, if one virtual machine fails to begin sending heartbeats,
        perhaps because it could not start up, other machines are not blocked from
        starting up since the startDelay eventually elapses.
    '''
    
    def __init__(self, key, startAction, startDelay, startOrder, stopAction, stopDelay, waitForHeartbeat):
        # MUST define these
        super(AutoStartPowerInfo, self).__init__()
    
        self.data['key'] = key
        self.data['startAction'] = startAction
        self.data['startDelay'] = startDelay
        self.data['startOrder'] = startOrder
        self.data['stopAction'] = stopAction
        self.data['stopDelay'] = stopDelay
        self.data['waitForHeartbeat'] = waitForHeartbeat
    
    
    @property
    def key(self):
        '''Virtual machine to power on or power off.
        '''
        return self.data['key']

    @property
    def startAction(self):
        '''How to start the virtual machine. Valid settings are none or powerOn. If set to
        none, then the virtual machine does not participate in auto-start.
        '''
        return self.data['startAction']

    @property
    def startDelay(self):
        '''Delay in seconds before continuing with the next virtual machine in the order of
        machines to be started. If the delay is specified as -1, then the system
        default is used.
        '''
        return self.data['startDelay']

    @property
    def startOrder(self):
        '''The autostart priority of this virtual machine. Virtual machines with a lower
        number are powered on first. On host shutdown, the virtual machines are
        shut down in reverse order, meaning those with a higher number are powered
        off first.
        '''
        return self.data['startOrder']

    @property
    def stopAction(self):
        '''Defines the stop action for the virtual machine. Can be set to none,
        systemDefault, powerOff, or suspend. If set to none, then the virtual
        machine does not participate in auto-stop.
        '''
        return self.data['stopAction']

    @property
    def stopDelay(self):
        '''Delay in seconds before continuing with the next virtual machine in the order
        sequence. If the delay is -1, then the system default is used.
        '''
        return self.data['stopDelay']

    @property
    def waitForHeartbeat(self):
        '''
        '''
        return self.data['waitForHeartbeat']

