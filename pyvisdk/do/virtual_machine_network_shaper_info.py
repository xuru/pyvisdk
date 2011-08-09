
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineNetworkShaperInfo(DynamicData):
    '''Network traffic shaping specification.Traffic shaping is used to configure the
        network utilization characteristics of a virtual machine.
    '''
    
    def __init__(self, averageBps, burstSize, enabled, peakBps):
        # MUST define these
        super(VirtualMachineNetworkShaperInfo, self).__init__()
    
        self.data['averageBps'] = averageBps
        self.data['burstSize'] = burstSize
        self.data['enabled'] = enabled
        self.data['peakBps'] = peakBps
    
    
    @property
    def averageBps(self):
        '''Average bandwidth, in bits per second.
        '''
        return self.data['averageBps']

    @property
    def burstSize(self):
        '''Burst size, in bytes.
        '''
        return self.data['burstSize']

    @property
    def enabled(self):
        '''Is the shaper enabled?
        '''
        return self.data['enabled']

    @property
    def peakBps(self):
        '''Peak bandwidth, in bits per second.
        '''
        return self.data['peakBps']

