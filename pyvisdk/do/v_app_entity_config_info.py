
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VAppEntityConfigInfo(DynamicData):
    '''This object type describes the behavior of an entity (virtual machine or sub-vApp
        container) in a vApp container.The auto-start/auto-stop configurations
        control the behavior of the start/stop vApp operations.An virtual machine
        entity can be configured to wait for a period of time before starting or
        to wait to receive a successful heartbeat from a virtual machine before
        starting the next virtual machine in the sequence.* For a power-on
        operation, if waitForHeartbeat is true, then the power-on sequence
        continues after the the first heartbeat has been received. If
        waitingForGuest is false, the system waits for the specified delay and
        then continues the power-on sequence. * For a power-off operation, if
        delay is non-zero, the requested power-off action is invoked (powerOff,
        suspend, guestShutdown) on the virtual machine and the system waits until
        the number of seconds specified in the delay have passed.If startAction
        and stopAction for an entity are both set to none, that entity does not
        participate in the sequence.The start/stop delay and waitingForGuest is
        not used if the entity is a vApp container. For a vApp the only value
        values for startAction is none or powerOn, and the valid values for
        stopAction is none or powerOff.
    '''
    
    def __init__(self, destroyWithParent, key, startAction, startDelay, startOrder, stopAction, stopDelay, tag, waitingForGuest):
        # MUST define these
        super(VAppEntityConfigInfo, self).__init__()
    
        self.data['destroyWithParent'] = destroyWithParent
        self.data['key'] = key
        self.data['startAction'] = startAction
        self.data['startDelay'] = startDelay
        self.data['startOrder'] = startOrder
        self.data['stopAction'] = stopAction
        self.data['stopDelay'] = stopDelay
        self.data['tag'] = tag
        self.data['waitingForGuest'] = waitingForGuest
    
    
    @property
    def destroyWithParent(self):
        '''Whether the entity should be removed, when this vApp is removed. This is only set
        for linked children.
        '''
        return self.data['destroyWithParent']

    @property
    def key(self):
        '''Entity to power on or power off. This can be a virtual machine or a vApp.
        '''
        return self.data['key']

    @property
    def startAction(self):
        '''How to start the entity. Valid settings are none or powerOn. If set to none, then
        the entity does not participate in auto-start.
        '''
        return self.data['startAction']

    @property
    def startDelay(self):
        '''Delay in seconds before continuing with the next entity in the order of entities
        to be started.
        '''
        return self.data['startDelay']

    @property
    def startOrder(self):
        '''Specifies the start order for this entity. Entities are started from lower numbers
        to higher-numbers and reverse on shutdown. Multiple entities with the same
        start-order can be started in parallel and the order is unspecified. This
        value must be 0 or higher.
        '''
        return self.data['startOrder']

    @property
    def stopAction(self):
        '''Defines the stop action for the entity. Can be set to none, powerOff,
        guestShutdown, or suspend. If set to none, then the entity does not
        participate in auto-stop.
        '''
        return self.data['stopAction']

    @property
    def stopDelay(self):
        '''Delay in seconds before continuing with the next entity in the order sequence.
        This is only used if the stopAction is guestShutdown.
        '''
        return self.data['stopDelay']

    @property
    def tag(self):
        '''Tag for entity.
        '''
        return self.data['tag']

    @property
    def waitingForGuest(self):
        '''Determines if the virtual machine should start after receiving a heartbeat, from
        the guest. When a virtual machine is next in the start order, the system
        either waits a specified period of time for a virtual machine to power on
        or it waits until it receives a successful heartbeat from a powered on
        virtual machine. By default, this is set to false.
        '''
        return self.data['waitingForGuest']

