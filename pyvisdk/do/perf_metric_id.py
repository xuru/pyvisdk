
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PerfMetricId(DynamicData):
    '''This data object type contains information that associates a performance counter
        with a performance metric. When constructing this data object for the
        metricId property of the PerfQuerySpec to submit to one of the
        PerformanceManager query operations, the instance property supports these
        special characters:* An asterisk (*) to specify all instances of the
        metric for the specified counterId * Double-quotes ("") to specify
        aggregated statistics
    '''
    
    def __init__(self, counterId, instance):
        # MUST define these
        super(PerfMetricId, self).__init__()
    
        self.data['counterId'] = counterId
        self.data['instance'] = instance
    
    
    @property
    def counterId(self):
        '''The ID of the counter for the metric.
        '''
        return self.data['counterId']

    @property
    def instance(self):
        '''An identifier that is derived from configuration names for the device associated
        with the metric. It identifies the instance of the metric with its source.
        This property may be empty. * For memory and aggregated statistics, this
        property is empty. * For host and virtual machine devices, this property
        contains the name of the device, such as the name of the host-bus adapter
        or the name of the virtual Ethernet adapter. For example,
        ?mpx.vmhba33:C0:T0:L0? or ?vmnic0:? * For a CPU, this property identifies
        the numeric position within the CPU core, such as 0, 1, 2, 3. * For a
        virtual disk, this property identifies the file type: * DISKFILE, for
        virtual machine base-disk files * SWAPFILE, for virtual machine swap files
        * DELTAFILE, for virtual machine snapshot overhead files * OTHERFILE, for
        all other files of a virtual machine
        '''
        return self.data['instance']

