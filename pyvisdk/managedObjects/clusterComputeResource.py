'''
Created on Mar 8, 2011

@author: eplaster
'''
from pyvisdk.consts import ManagedEntityTypes
from pyvisdk.managedObjects.managedentity import ManagedEntity
import logging

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

class ClusterComputeResource(ManagedEntity):
    def __init__(self, core, name=None, ref=None):
        # MUST define these first
        # -- start --
        self.type = ManagedEntityTypes.ClusterComputeResource
        
        # properties for this managed object
        props = [ "configuration"]
        
        # methods for this managed object
        methods = ["AddHost_Task", "ApplyRecommendation", "CancelRecommendation", "MoveHostInto_Task", \
                   "MoveInto_Task", "RecommendHostsForVm", "ReconfigureCluster_Task", \
                   "RefreshRecommendation", "RetrieveDasAdvancedRuntimeInfo"]
        # -- end --
        
        super(ClusterComputeResource, self).__init__(core, methods, props, name, ref)
        
