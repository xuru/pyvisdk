
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PerfProviderSummary(DynamicData):
    '''This data object type contains information about a performance provider, the type
        of statistics it generates, and the refreshRate for statistics generation.
        A performance provider is any managed object that generates real-time or
        historical statistics (or both?the currentSupported and summarySupported
        properties are not mutually exclusive).
    '''
    
    def __init__(self, currentSupported, entity, refreshRate, summarySupported):
        # MUST define these
        super(PerfProviderSummary, self).__init__()
    
        self.data['currentSupported'] = currentSupported
        self.data['entity'] = entity
        self.data['refreshRate'] = refreshRate
        self.data['summarySupported'] = summarySupported
    
    
    @property
    def currentSupported(self):
        '''True if this entity supports real-time (current) statistics; false if it does not.
        If this property is true for an entity, a client application can set the
        intervalId of the PerfQuerySpec (passed to the QueryPerf operation) to the
        refreshRate to obtain the maximum information possible for the entity.
        '''
        return self.data['currentSupported']

    @property
    def entity(self):
        '''Reference to the performance provider, the managed object that provides real-time
        or historical metrics. The managed objects include but are not limited to
        managed entities, such as host systems, virtual machines, and resource
        pools.
        '''
        return self.data['entity']

    @property
    def refreshRate(self):
        '''Number of seconds between the generation of each counter. This value applies only
        to entities that support real-time (current) statistics.
        '''
        return self.data['refreshRate']

    @property
    def summarySupported(self):
        '''True if this entity supports historical (aggregated) statistics; false if it does
        not. When this property is true for an entity, a client application can
        set the intervalId of QueryPerf to one of the historical intervals to
        obtain historical statistics for this entity.
        '''
        return self.data['summarySupported']

