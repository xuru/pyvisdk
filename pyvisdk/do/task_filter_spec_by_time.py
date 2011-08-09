
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class TaskFilterSpecByTime(DynamicData):
    '''This data object type specifies a time range used to filter task history.
    '''
    
    def __init__(self, beginTime, endTime, timeType):
        # MUST define these
        super(TaskFilterSpecByTime, self).__init__()
    
        self.data['beginTime'] = beginTime
        self.data['endTime'] = endTime
        self.data['timeType'] = timeType
    
    
    @property
    def beginTime(self):
        '''The beginning of the time range. If this property is not specified, then tasks are
        collected from the earliest time in the database.
        '''
        return self.data['beginTime']

    @property
    def endTime(self):
        '''The end of the time range. If this property is not specified, then tasks are
        collected up to the latest time in the database.
        '''
        return self.data['endTime']

    @property
    def timeType(self):
        '''The time stamp to filter: queued, started, or completed time.
        '''
        return self.data['timeType']

