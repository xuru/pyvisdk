
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.history_collector import HistoryCollector
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class TaskHistoryCollector(HistoryCollector):
    '''TaskHistoryCollector provides a mechanism for retrieving historical data and
        updates when the server appends new tasks.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.TaskHistoryCollector):
        # MUST define these
        super(TaskHistoryCollector, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def latestPage(self):
        '''The items in the 'viewable latest page'. As new items are added to the collector,
        they are appended at the end of the page. The oldest item is removed from
        the collector whenever there are more items in the collector than allowed
        (by 'setLatestPageSize').
        '''
        return self.update('latestPage')


    def ReadNextTasks(self, maxCount):
        '''Reads the 'scrollable view' from the current position. The scrollable position is
        moved to the next newer page after the read. No item is returned when the
        end of the collector is reached.

        :param maxCount: The maximum number of items in the page.


        :rtype: TaskInfo[] 

        '''
        
        return self.delegate("ReadNextTasks")(maxCount)
        

    def ReadPreviousTasks(self, maxCount):
        '''Reads the 'scrollable view' from the current position. The scrollable position is
        then moved to the next older page after the read. No item is returned when
        the head of the collector is reached.

        :param maxCount: The maximum number of items in the page.


        :rtype: TaskInfo[] 

        '''
        
        return self.delegate("ReadPreviousTasks")(maxCount)
        
