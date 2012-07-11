
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HistoryCollector(BaseEntity):
    '''This managed object type enables clients to retrieve historical data and
    receive updates when the server appends new data to a collection. This is a
    base type for item-specific types related to event or task history. Historical
    data is inherently append-only, although a server administrator may
    periodically purge old data.Typically, a client creates a history collector by
    using a filter on a potentially large set, such as all the events in a
    datacenter. The collector provides access to the items that match the filter,
    which could also be a relatively large set.The items in a collector are always
    ordered by date and time of creation. Item properties normally include this
    time stamp.The client may set the "viewable latest page" for the collector,
    which is the contiguous subset of the items that are of immediate interest.
    These items are available as the "latestPage" property, which the client may
    retrieve and monitor by using the PropertyCollector managed object.Clients can
    change the page size of the "latestPage" by using setLatestPageSize().The
    client may use the following features of the history collector.*
    RewindCollector - Moves the "scrollable view" to the oldest item (the default
    setting). * readNext - Retrieves all the items in the collector, from the
    oldest item to the newest item. Retrieves either tasks or events depending on
    the operation. * readPrev - Retrieves all items (excluding the "viewable latest
    page") in the collector, from the newest item to the oldest item. Retrieves
    either tasks or events depending on the operation. * ResetCollector - Moves the
    "scrollable view" to the item immediately preceding the "viewable latest page".'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HistoryCollector):
        super(HistoryCollector, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def filter(self):
        '''The filter used to create this collector.'''
        return self.update('filter')

    
    
    def DestroyCollector(self):
        '''Destroys this collector.
        
        '''
        return self.delegate("DestroyCollector")()
    
    def ResetCollector(self):
        '''Moves the "scrollable view" to the item immediately preceding the "viewable
        latest page". If you use "readPrev", ReadPreviousTasks or ReadPreviousEvents,
        all items are retrieved from the newest item to the oldest item.
        
        '''
        return self.delegate("ResetCollector")()
    
    def RewindCollector(self):
        '''Moves the "scrollable view" to the oldest item. If you use ReadNextTasks or
        ReadNextEvents, all items are retrieved from the oldest item to the newest
        item. This is the default setting when the collector is created.
        
        '''
        return self.delegate("RewindCollector")()
    
    def SetCollectorPageSize(self, maxCount):
        '''Sets the "viewable latest page" size to contain at most the number of items
        specified by the maxCount parameter).
        
        :param maxCount: The maximum number of items in the page.
        
        '''
        return self.delegate("SetCollectorPageSize")(maxCount)