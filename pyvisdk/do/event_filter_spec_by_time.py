
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class EventFilterSpecByTime(DynamicData):
    '''This option specifies a time range used to filter event history.
    '''
    
    def __init__(self, beginTime, endTime):
        # MUST define these
        super(EventFilterSpecByTime, self).__init__()
    
        self.data['beginTime'] = beginTime
        self.data['endTime'] = endTime
    
    
    @property
    def beginTime(self):
        '''The beginning of the time range. If this property is not set, then events are
        collected from the earliest time in the database.
        '''
        return self.data['beginTime']

    @property
    def endTime(self):
        '''The end of the time range. If this property is not specified, then events are
        collected up to the latest time in the database.
        '''
        return self.data['endTime']

