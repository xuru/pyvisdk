
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.history_collector import HistoryCollector

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class EventHistoryCollector(HistoryCollector):
    '''EventHistoryCollector provides a mechanism for retrieving historical data and
    updates when the server appends new events.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.EventHistoryCollector):
        super(EventHistoryCollector, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def latestPage(self):
        '''The items in the 'viewable latest page'. As new events that match the
        collector's EventFilterSpec are created, they are added to this page, and the
        oldest events are removed from the collector to keep the size of the page to
        that allowed by HistoryCollector#setLatestPageSize.'''
        return self.update('latestPage')

    
    
    def ReadNextEvents(self, maxCount):
        '''Reads the 'scrollable view' from the current position. The scrollable position
        is moved to the next newer page after the read. No item is returned when the
        end of the collector is reached.
        
        :param maxCount: The maximum number of items in the page.
        
        '''
        return self.delegate("ReadNextEvents")(maxCount)
    
    def ReadPreviousEvents(self, maxCount):
        '''Reads the 'scrollable view' from the current position. The scrollable position
        is moved to the next older page after the read. No item is returned when the
        head of the collector is reached.
        
        :param maxCount: The maximum number of items in the page.
        
        '''
        return self.delegate("ReadPreviousEvents")(maxCount)