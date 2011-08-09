
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class Event(DynamicData):
    '''This event is the base data object type from which all events inherit. All event
        objects are data structures that describe events. While event data objects
        are data structures that describe events, event data type documentation
        may describe what the event records, rather than the data structure,
        itself.
    '''
    
    def __init__(self, chainId, changeTag, computeResource, createdTime, datacenter, ds, dvs, fullFormattedMessage, host, key, net, userName, vm):
        # MUST define these
        super(Event, self).__init__()
    
        self.data['chainId'] = chainId
        self.data['changeTag'] = changeTag
        self.data['computeResource'] = computeResource
        self.data['createdTime'] = createdTime
        self.data['datacenter'] = datacenter
        self.data['ds'] = ds
        self.data['dvs'] = dvs
        self.data['fullFormattedMessage'] = fullFormattedMessage
        self.data['host'] = host
        self.data['key'] = key
        self.data['net'] = net
        self.data['userName'] = userName
        self.data['vm'] = vm
    
    
    @property
    def chainId(self):
        '''The parent or group ID.
        '''
        return self.data['chainId']

    @property
    def changeTag(self):
        '''The user entered tag to identify the operations and their side effects
        '''
        return self.data['changeTag']

    @property
    def computeResource(self):
        '''The ComputeResource object of the event.
        '''
        return self.data['computeResource']

    @property
    def createdTime(self):
        '''The time the event was created.
        '''
        return self.data['createdTime']

    @property
    def datacenter(self):
        '''The Datacenter object of the event.
        '''
        return self.data['datacenter']

    @property
    def ds(self):
        '''The Datastore object of the event.
        '''
        return self.data['ds']

    @property
    def dvs(self):
        '''The DistributedVirtualSwitch object of the event.
        '''
        return self.data['dvs']

    @property
    def fullFormattedMessage(self):
        '''A formatted text message describing the event. The message may be localized.
        '''
        return self.data['fullFormattedMessage']

    @property
    def host(self):
        '''The Host object of the event.
        '''
        return self.data['host']

    @property
    def key(self):
        '''The event ID.
        '''
        return self.data['key']

    @property
    def net(self):
        '''The Network object of the event.
        '''
        return self.data['net']

    @property
    def userName(self):
        '''The user who caused the event.
        '''
        return self.data['userName']

    @property
    def vm(self):
        '''The VirtualMachine object of the event.
        '''
        return self.data['vm']

