
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PerformanceManager(BaseEntity):
    '''This managed object type provides the service interface for obtaining
    statistical data about various aspects of system performance, as generated and
    maintained by the system's performance providers. A "performance provider"
    (PerfProviderSummary) is any managed object that generates utilization or other
    performance metrics. Performance providers include managed entities, such as
    hosts, virtual machines, compute resources, resource pools, datastores, and
    networks. Performance providers also include physical or virtual devices
    associated with these objects, such as virtual host-bus adapters and network-
    interface controllers (NICs)Each performance providerthe instrumented device
    or entityhas its own set of counters that provides metadata about its
    available metrics. Each counter has a unique key, referred to as the counterId.
    The actual performance metrics generated at runtime are identified by this
    counterId. Counters are organized by groups of finite system resources, such as
    , , , and so on. The links in this list contain documentation for performance
    counters, by group. Each page contains a table that includes data extracted
    from instances of the PerfCounterInfo data object, including the counter name,
    its Label, Unit, StatsType, RollupType, and Level:* * * * * * * * * Storage
    Capacity: * * Storage I/O: * * * * * * * *Other performance-counter groups, in
    addition to those listed here, exist on the system. However, only the counter
    groups listed are considered of possible interest to third-party
    developers.This interface provides these query operations:*
    QueryPerfProviderSummary, for obtaining metatdata about performance providers *
    QueryPerfCounter and QueryPerfCounterByLevel for obtaining metadata about
    supported counters. * QueryPerf, QueryAvailablePerfMetric, and
    QueryPerfComposite for obtaining statistics for one or more entities: * Use
    QueryPerf to obtain metrics for multiple entities in a single call. * Use
    QueryPerfComposite to obtain statistics for a single entity with its descendent
    objectsstatistics for a host and all its virtual machines, for example.Some
    differences between ESX and vCenter Server implementations of this interface
    include:* For ESX systems, this interface provides access to real-time data,
    and to real-time data that has been rolled up into "PastDay" statistics (if
    applicable for the specific counter). * For vCenter Server systems, this
    interface provides access to real-time and historical data. vCenter Server
    collects statistics on a regular basis from all ESX systems that it manages,
    and aggregates the results based on the level settings for the server. *
    Default sampling interval is product- and version-specific: * ESX 3.x (and
    subsequent) systems: 20 second interval * ESX 2.x systems: 60 second interval *
    VirtualCenter Server 2.5 (and subsequent vCenter Server) systems initially
    collect statistics data 10 minutes after system startup, and then hourly
    thereafter.See the Programming Guide for more information about using
    PerformanceManager.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.PerformanceManager):
        super(PerformanceManager, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def description(self):
        '''The static description strings.'''
        return self.update('description')
    @property
    def historicalInterval(self):
        '''A list of intervals configured on the system.'''
        return self.update('historicalInterval')
    @property
    def perfCounter(self):
        '''A list of all supported performance counters in the system.'''
        return self.update('perfCounter')

    
    
    def CreatePerfInterval(self, intervalId):
        '''<b>Deprecated.</b> <i>As of API 2.5, use UpdatePerfInterval. The default
        historical intervals can be modified, but they cannot be created.</i> Adds a
        new historical interval. Sampling period for new interval must be a multiple of
        an existing interval; must comprise a longer period of time; and must be
        uniquely named.
        
        :param intervalId: A custom interval, specified as the number of seconds to hold data in the database, a user-specified unique name, and a sampling period (in seconds).
        
        '''
        return self.delegate("CreatePerfInterval")(intervalId)
    
    def QueryAvailablePerfMetric(self, entity, beginTime=None, endTime=None, intervalId=None):
        '''Retrieves all performance counters for the specified managed object generated
        during a specified period of time. The time period can be specified using
        beginTime, endTime, or by interval ID.
        
        :param entity: The managed object that provides performance metrics.
        
        :param beginTime: Starting time (server time) for a period of time from which to return available metrics. If not specified, defaults to oldest available metric for the specified entity.
        
        :param endTime: Ending time (server time) for a period of time from which to return available performance metrics. If not specified, defaults to the most recently generated metric for the specified entity.
        
        :param intervalId: Period of time from which to retrieve metrics, defined by intervalId (rather than beginTime or endTime). Valid intervalIds include: * For real-time counters, the refreshRate of the performance provider. * For historical counters, the historical interval. If this parameter is not specified, the system returns available metrics for historical statistics.
        
        '''
        return self.delegate("QueryAvailablePerfMetric")(entity, beginTime, endTime, intervalId)
    
    def QueryPerf(self, querySpec):
        '''Retrieves the performance metrics for the specified entity (or entities) based
        on the properties specified in the PerfQuerySpec data object.Retrieves the
        performance metrics for the specified entity (or entities) based on the
        properties specified in the PerfQuerySpec data object.
        
        :param querySpec: An array of PerfQuerySpec objects. Each PerfQuerySpec object specifies a managed object reference for an entity, plus optional criteria for filtering results. Only metrics for entities that can be resolved and that are valid performance providers are returned in any result.
        
        '''
        return self.delegate("QueryPerf")(querySpec)
    
    def QueryPerfComposite(self, querySpec):
        '''Retrieves a PerfCompositeMetric data object that comprises statistics for the
        specified entity and its children entities. Only metrics for the first level of
        descendents are included in the PerfCompositeMetric object.Retrieves a
        PerfCompositeMetric data object that comprises statistics for the specified
        entity and its children entities. Only metrics for the first level of
        descendents are included in the PerfCompositeMetric object.Retrieves a
        PerfCompositeMetric data object that comprises statistics for the specified
        entity and its children entities. Only metrics for the first level of
        descendents are included in the PerfCompositeMetric object.
        
        :param querySpec: A PerfQuerySpec object specifying the query parameters. This PerfQuerySpec object specifies a managed object for which composite statistics should be retrieved, with specific optional criteria for filtering the results.
        
        '''
        return self.delegate("QueryPerfComposite")(querySpec)
    
    def QueryPerfCounter(self, counterId):
        '''Retrieves counter information for the specified list of counter IDs.
        
        :param counterId: An array of one or more counterIds representing performance counters for which information is being retrieved.
        
        '''
        return self.delegate("QueryPerfCounter")(counterId)
    
    def QueryPerfCounterByLevel(self, level):
        '''Retrieves the set of counters that are available at a specified collection
        level. The collection level determines the statistics that get stored in
        VirtualCenter. See PerfInterval for more information about VirtualCenter Server
        historical statistics collection.
        
        :param level: A number between 1 and 4 that specifies the collection level.
        
        '''
        return self.delegate("QueryPerfCounterByLevel")(level)
    
    def QueryPerfProviderSummary(self, entity):
        '''Retrieves the PerfProviderSummary data object that defines the capabilities of
        the specified managed object with respect to statistics, such as whether it
        supports current or summary statistics.
        
        :param entity: Reference to a managed object that provides performance data. If the entity specified by managed object reference is not a performance provider, an "InvalidArgument" exception is thrown.
        
        '''
        return self.delegate("QueryPerfProviderSummary")(entity)
    
    def RemovePerfInterval(self, samplePeriod):
        '''<b>Deprecated.</b> <i>As of API 2.5, use UpdatePerfInterval. Historical
        intervals cannot be removed.</i> Removes an interval from the list.
        
        :param samplePeriod: The sampling period, in seconds, for the specified interval being removed.
        
        '''
        return self.delegate("RemovePerfInterval")(samplePeriod)
    
    def ResetCounterLevelMapping(self, counters):
        '''Restores a set of performance counters to the default level of data collection.
        See the <a href="#counterTables">performance counter tables</a> for the default
        collection level for individual counters.
        
        :param counters: An array of counter ids.
        
        '''
        return self.delegate("ResetCounterLevelMapping")(counters)
    
    def UpdateCounterLevelMapping(self, counterLevelMap):
        '''Changes the level of data collection for a set of performance counters. See the
        <a href="#counterTables">performance counter tables</a> for the default
        collection level for individual counters.
        
        :param counterLevelMap: An array of PerformanceManagerCounterLevelMapping objects. The levels for the counters passed in are changed to the passed in values. If the optional aggregateLevel field is left unset then only the perDeviceLevel is configured. If the optional perDeviceLevel is left unset then only the aggregateLevel is configured. If there are multiple entries in the passed in array for the same counterId being updated then the last entry containing the counterId takes effect.
        
        '''
        return self.delegate("UpdateCounterLevelMapping")(counterLevelMap)
    
    def UpdatePerfInterval(self, interval):
        '''Modifies VirtualCenter Server's built-in historical intervals, within certain
        limits.Modifies VirtualCenter Server's built-in historical intervals, within
        certain limits.
        
        :param interval: The historical interval being modified, a complete data object comprising values for enabled, interval ID, length of time to maintain statistics for this interval in the database, level, name, and samplingPeriod properties.
        
        '''
        return self.delegate("UpdatePerfInterval")(interval)