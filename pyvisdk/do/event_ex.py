
from pyvisdk.do.event import Event
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class EventEx(Event):
    '''EventEx is a dynamically typed Event class, whose type is indicated by its
        eventTypeId property.A collection of eventTypeIds is registered by
        Extensions, which can now pass in optional type information for each
        eventTypeId which indicates the applicable argument names and types, among
        other properties.EventEx allows event arguments of any type, though today,
        the system only supports "string" and "moid" (a string which can be
        interpreted as an object ID in the system) as argument types. In the
        future, the system may optionally strongly check the types of the
        arguments in the event against the declared type information, based on how
        the event type is declared.EventEx also allows arbitrary "event object"s -
        the object which the event refers to. You can put in any object identifier
        as the objectId, but objectType should be filled in only if the object is
        actually present in the VC Server's ManagedEntity inventory.
    '''
    
    def __init__(self, arguments, eventTypeId, fault, message, objectId, objectName, objectType, severity):
        # MUST define these
        super(EventEx, self).__init__()
    
        self.data['arguments'] = arguments
        self.data['eventTypeId'] = eventTypeId
        self.data['fault'] = fault
        self.data['message'] = message
        self.data['objectId'] = objectId
        self.data['objectName'] = objectName
        self.data['objectType'] = objectType
        self.data['severity'] = severity
    
    
    @property
    def arguments(self):
        '''The event arguments associated with the event
        '''
        return self.data['arguments']

    @property
    def eventTypeId(self):
        '''The type of the event.
        '''
        return self.data['eventTypeId']

    @property
    def fault(self):
        '''The fault that triggered the event, if any
        '''
        return self.data['fault']

    @property
    def message(self):
        '''An arbitrary message string, not localized.
        '''
        return self.data['message']

    @property
    def objectId(self):
        '''The ID of the object (VM, Host, Folder..) which the event pertains to. Federated
        or local inventory path.
        '''
        return self.data['objectId']

    @property
    def objectName(self):
        '''The name of the object
        '''
        return self.data['objectName']

    @property
    def objectType(self):
        '''the type of the object, if known to the VirtualCenter inventory
        '''
        return self.data['objectType']

    @property
    def severity(self):
        '''The severity level of the message: null=>info.
        '''
        return self.data['severity']

