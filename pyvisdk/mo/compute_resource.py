
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.managed_entity import ManagedEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ComputeResource(ManagedEntity):
    '''The base type ComputeResource, when instantiated by calling
        AddStandaloneHost_Task, represents a single host. The subclass
        ClusterComputeResource represents a cluster of hosts and adds distributed
        management features such as availability and resource scheduling.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.ComputeResource):
        # MUST define these
        super(ComputeResource, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def configurationEx(self):
        '''Configuration of the compute resource; applies to both standalone hosts and
        clusters. For a cluster this property will return a ClusterConfigInfoEx
        object.
        '''
        return self.update('configurationEx')

    @property
    def datastore(self):
        '''The datastore property is the subset of datastore objects in the datacenter
        available in this ComputeResource.
        '''
        return self.update('datastore')

    @property
    def environmentBrowser(self):
        '''The environment browser object that identifies the environments that are supported
        on this compute resource.
        '''
        return self.update('environmentBrowser')

    @property
    def host(self):
        '''List of hosts that are part of this compute resource. If the compute resource is a
        standalone type, then this list contains just one element.
        '''
        return self.update('host')

    @property
    def network(self):
        '''The subset of network objects available in the datacenter that is available in
        this ComputeResource.
        '''
        return self.update('network')

    @property
    def resourcePool(self):
        '''Reference to root resource pool.
        '''
        return self.update('resourcePool')

    @property
    def summary(self):
        '''Basic runtime information about a compute resource. This information is used on
        summary screens and in list views.
        '''
        return self.update('summary')

