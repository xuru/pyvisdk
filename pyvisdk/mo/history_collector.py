
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HistoryCollector(BaseEntity):
    '''This managed object type enables clients to retrieve historical data and receive
        updates when the server appends new data to a collection. This is a base
        type for item-specific types related to event or task history. Historical
        data is inherently append-only, although a server administrator may
        periodically purge old data.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HistoryCollector):
        # MUST define these
        super(HistoryCollector, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def filter(self):
        '''
        The filter used to create this collector.
        '''
        return self.update('filter')


    def ResetCollector(self):
        '''Moves the "scrollable view" to the item immediately preceding the "viewable latest
        page". If you use "readPrev", ReadPreviousTasks or ReadPreviousEvents, all
        items are retrieved from the newest item to the oldest item.
        '''
        
        return self.delegate("ResetCollector")()
        

    def SetCollectorPageSize(self, maxCount):
        '''Sets the "viewable latest page" size to contain at most the number of items
        specified by the maxCount parameter).

        :param maxCount: The maximum number of items in the page.

        '''
        
        return self.delegate("SetCollectorPageSize")(maxCount)
        

    def DestroyCollector(self):
        '''Destroys this collector.
        '''
        
        return self.delegate("DestroyCollector")()
        

    def RewindCollector(self):
        '''Moves the "scrollable view" to the oldest item. If you use ReadNextTasks or
        ReadNextEvents, all items are retrieved from the oldest item to the newest
        item. This is the default setting when the collector is created.
        '''
        
        return self.delegate("RewindCollector")()
        
