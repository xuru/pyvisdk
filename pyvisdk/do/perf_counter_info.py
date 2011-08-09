
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PerfCounterInfo(DynamicData):
    '''This data object type contains metadata for a performance counter. See
        PerformanceManager for definitions of available counters.
    '''
    
    def __init__(self, associatedCounterId, groupInfo, key, level, nameInfo, perDeviceLevel, rollupType, statsType, unitInfo):
        # MUST define these
        super(PerfCounterInfo, self).__init__()
    
        self.data['associatedCounterId'] = associatedCounterId
        self.data['groupInfo'] = groupInfo
        self.data['key'] = key
        self.data['level'] = level
        self.data['nameInfo'] = nameInfo
        self.data['perDeviceLevel'] = perDeviceLevel
        self.data['rollupType'] = rollupType
        self.data['statsType'] = statsType
        self.data['unitInfo'] = unitInfo
    
    
    @property
    def associatedCounterId(self):
        '''The counter IDs associated with the same performance counter name for the same
        device type. For example, the rollup types for CPU Usage for a host are
        average, minimum, and maximum. Therefore, their counter IDs are
        associated.
        '''
        return self.data['associatedCounterId']

    @property
    def groupInfo(self):
        '''The group of the performance counter with its label and summary details. Counter
        groups include "cpu," "mem," "net," "disk," "system," "rescpu," and
        "clusterServices," for example.
        '''
        return self.data['groupInfo']

    @property
    def key(self):
        '''A system-generated number that uniquely identifies the counter in the context of
        the system. The performance counter ID.
        '''
        return self.data['key']

    @property
    def level(self):
        '''Minimum level at which metrics of this type will be collected by VirtualCenter
        Server. The value for this property for any performance counter is a
        number from 1 to 4. The higher the setting, the more data is collected by
        VirtualCenter Server. The default setting for VirtualCenter Server is 1,
        which collects the minimal amount of performance data that is typically
        useful to administrators and developers alike. The specific level of each
        counter is documented in the respective counter-documentation pages, by
        group. See PerformanceManager for links to the counter group pages.
        '''
        return self.data['level']

    @property
    def nameInfo(self):
        '''The name of the counter with label and summary details. For example, the counter
        with name "usage" for the "cpu" group of performance counters.
        '''
        return self.data['nameInfo']

    @property
    def perDeviceLevel(self):
        '''Minimum level at which the per device metrics of this type will be collected by
        vCenter Server. The value for this property for any performance counter is
        a number from 1 to 4. By default all per device metrics are calculated at
        level 3 or more. If a certain per device counter is collected at a certain
        level, the aggregate metric is also calculated at that level, i.e.,
        perDeviceLevel is greater than or equal to level.
        '''
        return self.data['perDeviceLevel']

    @property
    def rollupType(self):
        '''The counter type. Valid values include average, maximum, minimum, latest,
        summation, or none. This determines the type of statistical values that
        are returned for the counter. None means that the counter is never rolled
        up.
        '''
        return self.data['rollupType']

    @property
    def statsType(self):
        '''Statistics type for the counter. Valid values include absolute, delta, or rate.
        '''
        return self.data['statsType']

    @property
    def unitInfo(self):
        '''The unit for the values of the performance counter with its label and summary
        details. See PerformanceManagerUnit for a description of the valid values.
        '''
        return self.data['unitInfo']

