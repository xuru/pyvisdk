
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
    Datacenter.* A folder for VirtualMachine, template, and VirtualApp objects. * A
    folder for a ComputeResource hierarchy. * A folder for Network,
    DistributedVirtualSwitch, and DistributedVirtualPortgroup objects. * A folder
    for Datastore objects.For a visual representation of the organization of
    objects in a vCenter hierarchy, see the description of the ServiceInstance
    object.'''

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

    
    
    def PowerOnMultiVM_Task(self, vm, option=None):
        '''Powers on multiple virtual machines in a data center. If the virtual machines
        are suspended, this method resumes execution from the suspend point. The
        virtual machines can belong to different clusters in the data center.Powers on
        multiple virtual machines in a data center. If the virtual machines are
        suspended, this method resumes execution from the suspend point. The virtual
        machines can belong to different clusters in the data center.Powers on multiple
        virtual machines in a data center. If the virtual machines are suspended, this
        method resumes execution from the suspend point. The virtual machines can
        belong to different clusters in the data center.
        
        :param vm: The virtual machines to power on.
        
        :param option: An array of OptionValue options for this power-on session. The names and values of the options are defined in ClusterPowerOnVmOption.vSphere API 4.1
        
        '''
        return self.delegate("PowerOnMultiVM_Task")(vm, option)
    
    def QueryConnectionInfo(self, hostname, port, username, password, sslThumbprint=None):
        '''This method provides a way of getting basic information about a host without
        adding it to a datacenter. Connection wizards typically use this method to show
        information about a host so a user can confirm a set of changes before applying
        them.
        
        :param hostname: The target of the query.
        
        :param port: The port number of the target host. For ESX 2.x this is the authd port (902 by default). For ESX 3.x and above and for VMware Server hosts this is the https port (443 by default). You can specify -1 to have the vCenter Server try the default ports.
        
        :param username: The name of the user.
        
        :param password: The password of the user.
        
        :param sslThumbprint: The expected SSL thumbprint of the host's certificateVI API 2.5
        
        '''
        return self.delegate("QueryConnectionInfo")(hostname, port, username, password, sslThumbprint)