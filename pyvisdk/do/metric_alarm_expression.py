
from pyvisdk.do.alarm_expression import AlarmExpression
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class MetricAlarmExpression(AlarmExpression):
    '''An alarm expression that uses a metric as the condition that triggers an alarm.
        Base type.There are two alarm operands: yellow and red. At least one of
        them must be set. The value of the alarm expression is determined as
        follows:* If the host is not connected, the host metric expression is
        gray. * If the vm is not connected, the vm metric expression is gray. * If
        red is set but yellow is not, the expression is red when the metric is
        over (isAbove operator) or under (isBelow operator) the red value.
        Otherwise, the expression is green. * If yellow is set but red is not, the
        expression is yellow when the metric is over (isAbove) or under (isBelow)
        the yellow value. Otherwise, the expression is green. * If both yellow and
        red are set, the value of the expression is red when the metric is over
        (isAbove) or under (isBelow) the red value. Otherwise, the expression is
        yellow when the metric is over (isAbove) or under (isBelow) the yellow
        value. Otherwise, the expression is green.
    '''
    
    def __init__(self, metric, operator, red, redInterval, type, yellow, yellowInterval):
        # MUST define these
        super(MetricAlarmExpression, self).__init__()
    
        self.data['metric'] = metric
        self.data['operator'] = operator
        self.data['red'] = red
        self.data['redInterval'] = redInterval
        self.data['type'] = type
        self.data['yellow'] = yellow
        self.data['yellowInterval'] = yellowInterval
    
    
    @property
    def metric(self):
        '''The instance of the metric.
        '''
        return self.data['metric']

    @property
    def operator(self):
        '''The operation to be tested on the metric.
        '''
        return self.data['operator']

    @property
    def red(self):
        '''Whether or not to test for a red condition. If not set, do not calculate red
        status. If set, it contains the threshold value that triggers red status.
        '''
        return self.data['red']

    @property
    def redInterval(self):
        '''Time interval in seconds for which the red condition must be true before the red
        status is triggered. If unset, the red status is triggered immediately
        when the red condition becomes true.
        '''
        return self.data['redInterval']

    @property
    def type(self):
        '''Name of the object type containing the property.
        '''
        return self.data['type']

    @property
    def yellow(self):
        '''Whether or not to test for a yellow condition. If not set, do not calculate yellow
        status. If set, it contains the threshold value that triggers yellow
        status.
        '''
        return self.data['yellow']

    @property
    def yellowInterval(self):
        '''Time interval in seconds for which the yellow condition must be true before the
        yellow status is triggered. If unset, the yellow status is triggered
        immediately when the yellow condition becomes true.
        '''
        return self.data['yellowInterval']

