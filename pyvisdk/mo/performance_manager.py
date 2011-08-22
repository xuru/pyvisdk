
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.base_entity import BaseEntity
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
    group. Each page contains a table that includes data extracted from instances
    of the PerfCounterInfo data object, including the counter name, its Label,
    Unit, StatsType, RollupType, and Level:* * * * * * * Storage Capacity: * *
    Storage I/O: * * * * * * *Other performance-counter groups, in addition to
    those listed here, exist on the system. However, only the counter groups listed
    are considered of possible interest to third-party developers.This interface
    provides these query operations:* QueryPerfProviderSummary, for obtaining
    metatdata about performance providers * QueryPerfCounter and
    QueryPerfCounterByLevel for obtaining metadata about supported counters. *
    QueryPerf, QueryAvailablePerfMetric, and QueryPerfComposite for obtaining
    statistics for one or more entities: * Use QueryPerf to obtain metrics for
    multiple entities in a single call. * Use QueryPerfComposite to obtain
    statistics for a single entity with its descendent objectsstatistics for a
    host and all its virtual machines, for example.Some differences between ESX and
    vCenter Server implementations of this interface include:* For ESX systems,
    this interface provides access to real-time data, and to real-time data that
    has been rolled up into "PastDay" statistics (if applicable for the specific
    counter). * For vCenter Server systems, this interface provides access to real-
    time and historical data. vCenter Server collects statistics on a regular basis
    from all ESX systems that it manages, and aggregates the results based on the
    level settings for the server. * Default sampling interval is product- and
    version-specific: * ESX 3.x (and subsequent) systems: 20 second interval * ESX
    2.x systems: 60 second interval * VirtualCenter Server 2.5 (and subsequent
    vCenter Server) systems initially collect statistics data 10 minutes after
    system startup, and then hourly thereafter.See the Programming Guide for more
    information about using PerformanceManager.'''
    
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
    
    
    
    def CreatePerfInterval(self):
        '''Deprecated. As of API 2.5, use UpdatePerfInterval. The default historical
        intervals can be modified, but they cannot be created. Adds a new historical
        interval. Sampling period for new interval must be a multiple of an existing
        interval; must comprise a longer period of time; and must be uniquely named.
        :rtype: None
        :returns: 
        '''
        return self.delegate("CreatePerfInterval")()
    
    def QueryAvailablePerfMetric(self):
        '''Retrieves all performance counters for the specified managed object generated
        during a specified period of time. The time period can be specified using
        beginTime, endTime, or by interval ID.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryAvailablePerfMetric")()
    
    def QueryPerf(self):
        '''Retrieves the performance metrics for the specified entity (or entities) based
        on the properties specified in the PerfQuerySpec data object.Query Performance
        for VirtualCenter Server
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryPerf")()
    
    def QueryPerfComposite(self):
        '''Retrieves a PerfCompositeMetric data object that comprises statistics for the
        specified entity and its children entities. Only metrics for the first level of
        descendents are included in the PerfCompositeMetric object.Use this operation
        to obtain statistics for a host and its associated virtual machines, for
        example.Requires system.read privilege for every virtual machine on the target
        host, or the query fails with the NoPermission fault. Suported for HostSystem
        managed entities only.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryPerfComposite")()
    
    def QueryPerfCounter(self):
        '''Retrieves counter information for the specified list of counter IDs.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryPerfCounter")()
    
    def QueryPerfCounterByLevel(self):
        '''Retrieves the set of counters that are available at a specified collection
        level. The collection level determines the statistics that get stored in
        VirtualCenter. See PerfInterval for more information about VirtualCenter Server
        historical statistics collection.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryPerfCounterByLevel")()
    
    def QueryPerfProviderSummary(self):
        '''Retrieves the PerfProviderSummary data object that defines the capabilities of
        the specified managed object with respect to statistics, such as whether it
        supports current or summary statistics.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryPerfProviderSummary")()
    
    def RemovePerfInterval(self):
        '''Deprecated. As of API 2.5, use UpdatePerfInterval. Historical intervals cannot
        be removed. Removes an interval from the list.
        :rtype: None
        :returns: 
        '''
        return self.delegate("RemovePerfInterval")()
    
    def UpdatePerfInterval(self):
        '''Modifies VirtualCenter Server's built-in historical intervals, within certain
        limits.Supported Modifications
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdatePerfInterval")()