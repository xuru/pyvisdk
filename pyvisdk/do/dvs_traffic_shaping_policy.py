
from pyvisdk.do.inheritable_policy import InheritablePolicy
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVSTrafficShapingPolicy(InheritablePolicy):
    '''This data object type describes traffic shaping policy.
    '''
    
    def __init__(self, averageBandwidth, burstSize, enabled, peakBandwidth):
        # MUST define these
        super(DVSTrafficShapingPolicy, self).__init__()
    
        self.data['averageBandwidth'] = averageBandwidth
        self.data['burstSize'] = burstSize
        self.data['enabled'] = enabled
        self.data['peakBandwidth'] = peakBandwidth
    
    
    @property
    def averageBandwidth(self):
        '''The average bandwidth in bits per second if shaping is enabled on the port.
        '''
        return self.data['averageBandwidth']

    @property
    def burstSize(self):
        '''The maximum burst size allowed in bytes if shaping is enabled on the port.
        '''
        return self.data['burstSize']

    @property
    def enabled(self):
        '''The flag to indicate whether or not traffic shaper is enabled on the port.
        '''
        return self.data['enabled']

    @property
    def peakBandwidth(self):
        '''The peak bandwidth during bursts in bits per second if traffic shaping is enabled
        on the port.
        '''
        return self.data['peakBandwidth']

