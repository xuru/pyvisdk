
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.history_collector import HistoryCollector
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class EventHistoryCollector(HistoryCollector):
    '''EventHistoryCollector provides a mechanism for retrieving historical data and
        updates when the server appends new events.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.EventHistoryCollector):
        # MUST define these
        super(EventHistoryCollector, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def ReadNextEvents(self, maxCount):
        '''Reads the 'scrollable view' from the current position. The scrollable position is
        moved to the next newer page after the read. No item is returned when the
        end of the collector is reached.

        :param maxCount: The maximum number of items in the page.


        :rtype: Event[] 

        '''
        
        return self.delegate("ReadNextEvents")(maxCount)
        

    def ReadPreviousEvents(self, maxCount):
        '''Reads the 'scrollable view' from the current position. The scrollable position is
        moved to the next older page after the read. No item is returned when the
        head of the collector is reached.

        :param maxCount: The maximum number of items in the page.


        :rtype: Event[] 

        '''
        
        return self.delegate("ReadPreviousEvents")(maxCount)
        
