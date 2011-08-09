
from pyvisdk.do.event import Event
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HealthStatusChangedEvent(Event):
    '''Event used to report change in health status of VirtualCenter components.
    '''
    
    def __init__(self, componentId, componentName, newStatus, oldStatus):
        # MUST define these
        super(HealthStatusChangedEvent, self).__init__()
    
        self.data['componentId'] = componentId
        self.data['componentName'] = componentName
        self.data['newStatus'] = newStatus
        self.data['oldStatus'] = oldStatus
    
    
    @property
    def componentId(self):
        '''Unique ID of the VirtualCenter component.
        '''
        return self.data['componentId']

    @property
    def componentName(self):
        '''Component name.
        '''
        return self.data['componentName']

    @property
    def newStatus(self):
        '''Current health status of the component.
        '''
        return self.data['newStatus']

    @property
    def oldStatus(self):
        '''Previous health status of the component.
        '''
        return self.data['oldStatus']

