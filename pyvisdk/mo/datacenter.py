
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.managed_entity import ManagedEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class Datacenter(ManagedEntity):
    '''The Datacenter managed object provides the interface to the common container
    object for hosts, virtual machines, networks, and datastores. These entities
    must be under a distinct datacenter in the inventory, and datacenters may not
    be nested under other datacenters.Every Datacenter has the following set of
    dedicated folders. These folders are empty until you create entities for the
    Datacenter.For a visual representation of the organization of objects in a
    vCenter hierarchy, see the description of the ServiceInstance object.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.Datacenter):
        super(Datacenter, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def datastore(self):
        '''A collection of references to the datastore objects available in this
    datacenter.'''
        return self.update('datastore')
    @property
    def datastoreFolder(self):
        '''A reference to the folder hierarchy that contains the datastores for this
    datacenter.'''
        return self.update('datastoreFolder')
    @property
    def hostFolder(self):
        '''A reference to the folder hierarchy that contains the compute resources,
    including hosts and clusters, for this datacenter.'''
        return self.update('hostFolder')
    @property
    def network(self):
        '''A collection of references to the network objects available in this datacenter.'''
        return self.update('network')
    @property
    def networkFolder(self):
        '''A reference to the folder hierarchy that contains the network entities for this
    datacenter. The folder can include Network, DistributedVirtualSwitch, and
    DistributedVirtualPortgroup objects.'''
        return self.update('networkFolder')
    @property
    def vmFolder(self):
        '''A reference to the folder hierarchy that contains VirtualMachine virtual
    machine templates (identified by the template property, and VirtualApp objects
    for this datacenter.'''
        return self.update('vmFolder')
    
    
    
    def PowerOnMultiVM_Task(self):
        '''Powers on multiple virtual machines in a data center. If the virtual machines
        are suspended, this method resumes execution from the suspend point. The
        virtual machines can belong to different clusters in the data center.If any
        virtual machine in the list is manually managed by DRS, or DRS has to migrate
        any manually managed virtual machine or power on any manually managed host in
        order to power on these virtual machines, a DRS recommendation will be
        generated, and the users need to manually apply the recommendation for actually
        powering on these virtual machines. Otherwise, all the virtual machine will be
        automatically powered on. The virtual machines on stand alone hosts or DRS
        disabled will be powered-on on the current host. The DRS automatically managed
        virtual machines will be powered-on on the recommended hosts.When powering on a
        virtual machine in a cluster, the system might do an implicit relocation of the
        virtual machine to another host.
        :rtype: ManagedObjectReference to a Task
        :returns: 
        '''
        return self.delegate("PowerOnMultiVM_Task")()
    
    def QueryConnectionInfo(self):
        '''This method provides a way of getting basic information about a host without
        adding it to a datacenter. Connection wizards typically use this method to show
        information about a host so a user can confirm a set of changes before applying
        them.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryConnectionInfo")()