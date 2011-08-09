
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PerfCompositeMetric(DynamicData):
    '''PerfCompositeMetric includes an optional aggregated entity performance statistics
        and a list of composite entities performance statistics. The aggregated
        entity statistics are optional because some entities, such as folders, do
        not have their own statistics.
    '''
    
    def __init__(self, childEntity, entity):
        # MUST define these
        super(PerfCompositeMetric, self).__init__()
    
        self.data['childEntity'] = childEntity
        self.data['entity'] = entity
    
    
    @property
    def childEntity(self):
        '''A list of metrics of performance providers that comprise the aggregated entity.
        For example, Host is an aggregated entity for virtual machines and virtual
        machine Folders. ResourcePools are aggregate entities for virtual
        machines. Host, Folder, and Cluster are aggregate entities for hosts in
        the cluster or folder.
        '''
        return self.data['childEntity']

    @property
    def entity(self):
        '''The aggregated entity performance metrics. If it exists, the PerfSampleInfo list
        of the aggregate entity is a complete list of PerfSampleInfo that could be
        contained in PerfSampleInfo lists of child entities.
        '''
        return self.data['entity']

