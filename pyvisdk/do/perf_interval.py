
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PerfInterval(DynamicData):
    '''This data object type contains metadata about a performance interval.* For
        VirtualCenter Server systems, instances of this data object are referred
        to as ?historical intervals? because they control how data collected from
        the ESX systems will be aggregated and stored in the database. * For ESX
        system, this data object is typically referred to simply as the ?interval?
        or ?performance interval? because ESX does not aggregate statistical
        data.For ESX systems, a single instance of this data object exists. It
        cannot be modified. It has these properties:VirtualCenter Server system
        provides four instances of this data object by default, that apply
        globally to all system entities.VirtualCenter Server uses the
        specifications configured in its historical intervals to collect metrics
        from the ESX systems that it manages. The quantity of data collected
        depends on the level settings for the server, and the level associated
        with a specific counter. Both factors may change from one version of the
        products to the next. In general, the lower the number, the smaller the
        amount of data collected. For VirtualCenter Server 2.5, for example, the
        levels 1 through 4 collected data as follows:Default properties for the
        four built-in historical intervals include:All values are in seconds. The
        default setting for vCenter Server is level 1, which retains sampled
        statistical data as follows:* 5-minute samples for the past day *
        30-minute samples for the past week * 2-hour samples for the past month *
        1-day samples for the past yearData older than a year is purged from the
        vCenter Server database.Prior to version 2.5 of the API, this data object
        could be used in conjunction with the CreatePerfInterval operation, to
        define new, custom historical intervals. That operation has been
        deprecated: Adding and deleting objects of this type is no longer
        supported. However, the default historical intervals can be enabled or
        disabled, and can be modified within certain limits (with the
        UpdatePerfInterval operation).
    '''
    
    def __init__(self, enabled, key, length, level, name, samplingPeriod):
        # MUST define these
        super(PerfInterval, self).__init__()
    
        self.data['enabled'] = enabled
        self.data['key'] = key
        self.data['length'] = length
        self.data['level'] = level
        self.data['name'] = name
        self.data['samplingPeriod'] = samplingPeriod
    
    
    @property
    def enabled(self):
        '''Indicates whether the interval is enabled (true) or disabled (false). Disabling a
        historical interval prevents vCenter Server from collecting metrics for
        that interval and all higher (longer) intervals.
        '''
        return self.data['enabled']

    @property
    def key(self):
        '''A unique identifier for the interval.
        '''
        return self.data['key']

    @property
    def length(self):
        '''Number of seconds that the statistics corresponding to this interval are kept on
        the system.
        '''
        return self.data['length']

    @property
    def level(self):
        '''Statistics collection level for this historical interval. vCenter Server will
        aggregate only those statistics that match the value of this property for
        this historical interval. For ESX, the value of this property is null. For
        vCenter Server, the value will be a number from 1 to 4.
        '''
        return self.data['level']

    @property
    def name(self):
        '''The name of the historical interval. A localized string that provides a name for
        the interval. Names include: * "Past Day" * "Past Week" * "Past Month" *
        "Past Year" The name is not meaningful in terms of system behavior. That
        is, the interval named ?Past Week? works as it does because of its length,
        level, and so on, not because of the value of this string.
        '''
        return self.data['name']

    @property
    def samplingPeriod(self):
        '''Number of seconds that data is sampled for this interval. The real-time
        samplingPeriod is 20 seconds.
        '''
        return self.data['samplingPeriod']

