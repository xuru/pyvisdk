
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.managed_entity import ManagedEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ComputeResource(ManagedEntity):
    '''Represents a set of physical compute resources for a set of virtual
    machines.The base type ComputeResource, when instantiated by calling
    AddStandaloneHost_Task, represents a single host. The subclass
    ClusterComputeResource represents a cluster of hosts and adds distributed
    management features such as availability and resource scheduling.A
    ComputeResource always has a root ResourcePool associated with it. Certain
    types of clusters such as those with VMware DRS enabled and standalone hosts
    (ESX Server 3) support the creation of ResourcePool hierarchies.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.ComputeResource):
        super(ComputeResource, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def configurationEx(self):
        '''Configuration of the compute resource; applies to both standalone hosts and
        clusters. For a cluster this property will return a ClusterConfigInfoEx object.'''
        return self.update('configurationEx')
    @property
    def datastore(self):
        '''The datastore property is the subset of datastore objects in the datacenter
        available in this ComputeResource.'''
        return self.update('datastore')
    @property
    def environmentBrowser(self):
        '''The environment browser object that identifies the environments that are
        supported on this compute resource.'''
        return self.update('environmentBrowser')
    @property
    def host(self):
        '''List of hosts that are part of this compute resource. If the compute resource
        is a standalone type, then this list contains just one element.'''
        return self.update('host')
    @property
    def network(self):
        '''The subset of network objects available in the datacenter that is available in
        this ComputeResource.'''
        return self.update('network')
    @property
    def resourcePool(self):
        '''Reference to root resource pool.'''
        return self.update('resourcePool')
    @property
    def summary(self):
        '''Basic runtime information about a compute resource. This information is used on
        summary screens and in list views.'''
        return self.update('summary')

    
    
    def ReconfigureComputeResource_Task(self, spec, modify):
        '''Change the compute resource configuration.
        
        :param spec: A set of configuration changes to apply to the compute resource. The specification can be a complete set of changes or a partial set of changes, applied incrementally. When invoking reconfigureEx on a cluster, this argument may be a ClusterConfigSpecEx object.
        
        :param modify: Flag to specify whether the specification ("spec") should be applied incrementally. If "modify" is false and the operation succeeds, then the configuration of the cluster matches the specification exactly; in this case any unset portions of the specification will result in unset or default portions of the configuration.
        
        '''
        return self.delegate("ReconfigureComputeResource_Task")(spec, modify)