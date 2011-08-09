
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AlarmSetting(DynamicData):
    '''Tolerance and frequency limits of an alarm.
    '''
    
    def __init__(self, reportingFrequency, toleranceRange):
        # MUST define these
        super(AlarmSetting, self).__init__()
    
        self.data['reportingFrequency'] = reportingFrequency
        self.data['toleranceRange'] = toleranceRange
    
    
    @property
    def reportingFrequency(self):
        '''How often the alarm is triggered, measured in seconds.
        '''
        return self.data['reportingFrequency']

    @property
    def toleranceRange(self):
        '''Tolerance range for the metric triggers, measured in one hundredth percentage.
        '''
        return self.data['toleranceRange']

