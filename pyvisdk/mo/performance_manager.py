
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PerformanceManager(BaseEntity):
    '''* * * * * * * Storage Capacity: * * Storage I/O: * * * * * * *
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.PerformanceManager):
        # MUST define these
        super(PerformanceManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def description(self):
        '''The static description strings.
        '''
        return self.update('description')

    @property
    def historicalInterval(self):
        '''A list of intervals configured on the system.
        '''
        return self.update('historicalInterval')

    @property
    def perfCounter(self):
        '''A list of all supported performance counters in the system.
        '''
        return self.update('perfCounter')


    def CreatePerfInterval(self, intervalId):
        '''Deprecated. As of API 2.5, use UpdatePerfInterval. The default historical
        intervals can be modified, but they cannot be created. Adds a new
        historical interval. Sampling period for new interval must be a multiple
        of an existing interval; must comprise a longer period of time; and must
        be uniquely named.

        :param intervalId: A custom interval, specified as the number of seconds to hold data in the
        database, a user-specified unique name, and a sampling period (in
        seconds).

        '''
        
        return self.delegate("CreatePerfInterval")(intervalId)
        

    def QueryAvailablePerfMetric(self, entity, beginTime, endTime, intervalId):
        '''Retrieves all performance counters for the specified managed object generated
        during a specified period of time. The time period can be specified using
        beginTime, endTime, or by interval ID.

        :param entity: The managed object that provides performance metrics.

        :param beginTime: Starting time (server time) for a period of time from which to return available
        metrics. If not specified, defaults to oldest available metric for the
        specified entity.

        :param endTime: Ending time (server time) for a period of time from which to return available
        performance metrics. If not specified, defaults to the most recently
        generated metric for the specified entity.

        :param intervalId: Period of time from which to retrieve metrics, defined by intervalId (rather than
        beginTime or endTime). Valid intervalIds include: * For real-time
        counters, the refreshRate of the performance provider. * For historical
        counters, the historical interval. If this parameter is not specified, the
        system returns available metrics for historical statistics.


        :rtype: PerfMetricId[] 

        '''
        
        return self.delegate("QueryAvailablePerfMetric")(entity,beginTime,endTime,intervalId)
        

    def QueryPerf(self, querySpec):
        '''Retrieves the performance metrics for the specified entity (or entities) based on
        the properties specified in the PerfQuerySpec data object.Query
        Performance for VirtualCenter Server

        :param querySpec: An array of PerfQuerySpec objects. Each PerfQuerySpec object specifies a managed
        object reference for an entity, plus optional criteria for filtering
        results. Only metrics for entities that can be resolved and that are valid
        performance providers are returned in any result.


        :rtype: PerfEntityMetricBase[] 

        '''
        
        return self.delegate("QueryPerf")(querySpec)
        

    def QueryPerfComposite(self, querySpec):
        '''Retrieves a PerfCompositeMetric data object that comprises statistics for the
        specified entity and its children entities. Only metrics for the first
        level of descendents are included in the PerfCompositeMetric object.Use
        this operation to obtain statistics for a host and its associated virtual
        machines, for example.Requires system.read privilege for every virtual
        machine on the target host, or the query fails with the NoPermission
        fault. Suported for HostSystem managed entities only.

        :param querySpec: A PerfQuerySpec object specifying the query parameters. This PerfQuerySpec object
        specifies a managed object for which composite statistics should be
        retrieved, with specific optional criteria for filtering the results.


        :rtype: PerfCompositeMetric 

        '''
        
        return self.delegate("QueryPerfComposite")(querySpec)
        

    def QueryPerfCounter(self, counterId):
        '''Retrieves counter information for the specified list of counter IDs.

        :param counterId: An array of one or more counterIds representing performance counters for which
        information is being retrieved.


        :rtype: PerfCounterInfo[] 

        '''
        
        return self.delegate("QueryPerfCounter")(counterId)
        

    def QueryPerfCounterByLevel(self, level):
        '''Retrieves the set of counters that are available at a specified collection level.
        The collection level determines the statistics that get stored in
        VirtualCenter. See PerfInterval for more information about VirtualCenter
        Server historical statistics collection.

        :param level: A number between 1 and 4 that specifies the collection level.


        :rtype: PerfCounterInfo[] 

        '''
        
        return self.delegate("QueryPerfCounterByLevel")(level)
        

    def QueryPerfProviderSummary(self, entity):
        '''Retrieves the PerfProviderSummary data object that defines the capabilities of the
        specified managed object with respect to statistics, such as whether it
        supports current or summary statistics.

        :param entity: Reference to a managed object that provides performance data. If the entity
        specified by managed object reference is not a performance provider, an
        "InvalidArgument" exception is thrown.


        :rtype: PerfProviderSummary 

        '''
        
        return self.delegate("QueryPerfProviderSummary")(entity)
        

    def RemovePerfInterval(self, samplePeriod):
        '''Deprecated. As of API 2.5, use UpdatePerfInterval. Historical intervals cannot be
        removed. Removes an interval from the list.

        :param samplePeriod: The sampling period, in seconds, for the specified interval being removed.

        '''
        
        return self.delegate("RemovePerfInterval")(samplePeriod)
        

    def UpdatePerfInterval(self, interval):
        '''Modifies VirtualCenter Server's built-in historical intervals, within certain
        limits.Supported Modifications

        :param interval: The historical interval being modified, a complete data object comprising values
        for enabled, interval ID, length of time to maintain statistics for this
        interval in the database, level, name, and samplingPeriod properties.

        '''
        
        return self.delegate("UpdatePerfInterval")(interval)
        
