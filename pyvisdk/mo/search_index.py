
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class SearchIndex(BaseEntity):
    '''The SearchIndex service allows a client to efficiently query the inventory for
    a specific managed entity by attributes such as UUID, IP address, DNS name, or
    datastore path. Such searches typically return a VirtualMachine or a
    HostSystem. While searching, only objects for which the user has sufficient
    privileges are considered. The findByInventoryPath and findChild operations
    only search on entities for which the user has view privileges; all other
    SearchIndex find operations only search virtual machines and hosts for which
    the user has read privileges. If the user does not have sufficient privileges
    for an object that matches the search criteria, that object is not returned.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.SearchIndex):
        super(SearchIndex, self).__init__(core, name=name, ref=ref, type=type)

    

    
    
    def FindAllByDnsName(self, dnsName, vmSearch, datacenter=None):
        '''Finds all virtual machines or hosts by DNS name. The DNS name for a virtual
        machine is the one returned from VMware tools, hostName.
        
        :param datacenter: If specified, restricts the query to entities in a particular datacenter. If not specified, the entire inventory is searched.
        
        :param dnsName: The fully qualified domain name to find.
        
        :param vmSearch: If true, search for virtual machines, otherwise search for hosts.
        
        '''
        return self.delegate("FindAllByDnsName")(datacenter, dnsName, vmSearch)
    
    def FindAllByIp(self, ip, vmSearch, datacenter=None):
        '''Finds all virtual machines or hosts by IP address, where the IP address is in
        dot-decimal notation. For example, 10.17.12.12. The IP address for a virtual
        machine is the one returned from VMware tools, ipAddress.
        
        :param datacenter: If specified, restricts the query to entities in a particular datacenter. If not specified, the entire inventory is searched.
        
        :param ip: The dot-decimal notation formatted IP address to find.
        
        :param vmSearch: If true, search for virtual machines, otherwise search for hosts.
        
        '''
        return self.delegate("FindAllByIp")(datacenter, ip, vmSearch)
    
    def FindAllByUuid(self, uuid, vmSearch, datacenter=None, instanceUuid=None):
        '''Finds all virtual machines or hosts by UUID.
        
        :param datacenter: If specified, restricts the query to entities in a particular datacenter. If not specified, the entire inventory is searched.
        
        :param uuid: The UUID to find. If vmSearch is true, the UUID can be either BIOS or instance UUID.
        
        :param vmSearch: If true, search for virtual machines, otherwise search for hosts.
        
        :param instanceUuid: Should only be set when vmSearch is true. If specified, search for virtual machines whose instance UUID matches the given uuid. Otherwise, search for virtual machines whose BIOS UUID matches the given uuid.
        
        '''
        return self.delegate("FindAllByUuid")(datacenter, uuid, vmSearch, instanceUuid)
    
    def FindByDatastorePath(self, datacenter, path):
        '''Finds a virtual machine by its location on a datastore.
        
        :param datacenter: Specifies the datacenter to which the datastore path belongs.
        
        :param path: A datastore path to the .vmx file for the virtual machine.
        
        '''
        return self.delegate("FindByDatastorePath")(datacenter, path)
    
    def FindByDnsName(self, dnsName, vmSearch, datacenter=None):
        '''Finds a virtual machine or host by DNS name. The DNS name for a virtual machine
        is the one returned from VMware tools, hostName.
        
        :param datacenter: If specified, restricts the query to entities in a particular datacenter. If not specified, the entire inventory is searched.
        
        :param dnsName: The fully qualified domain name to find.
        
        :param vmSearch: if true, search for virtual machines, otherwise search for hosts.
        
        '''
        return self.delegate("FindByDnsName")(datacenter, dnsName, vmSearch)
    
    def FindByInventoryPath(self, inventoryPath):
        '''Finds a managed entity based on its location in the inventory. The path is
        separated by slashes ('/'). For example, a path should be of the form "My
        Folder/My Datacenter/vm/Discovered VM/VM1". A leading slash or trailing slash
        is ignored. Thus, the following paths all represents the same object: "a/b",
        "/a/b", "a/b/", and '/a/b/'. Slashes in names must be represented using %2f,
        following the standard URL syntax. Any object in the inventory can be retrieved
        using this method, including resource pools and hosts.
        
        :param inventoryPath: The path to the entity.
        
        '''
        return self.delegate("FindByInventoryPath")(inventoryPath)
    
    def FindByIp(self, ip, vmSearch, datacenter=None):
        '''Finds a virtual machine or host by IP address, where the IP address is in dot-
        decimal notation. For example, 10.17.12.12. The IP address for a virtual
        machine is the one returned from VMware tools, ipAddress.
        
        :param datacenter: If specified, restricts the query to entities in a particular datacenter. If not specified, the entire inventory is searched.
        
        :param ip: The dot-decimal notation formatted IP address to find.
        
        :param vmSearch: if true, search for virtual machines, otherwise search for hosts.
        
        '''
        return self.delegate("FindByIp")(datacenter, ip, vmSearch)
    
    def FindByUuid(self, uuid, vmSearch, datacenter=None, instanceUuid=None):
        '''Finds a virtual machine or host by BIOS or instance UUID.
        
        :param datacenter: If specified, restricts the query to entities in a particular datacenter. If not specified, the entire inventory is searched.
        
        :param uuid: The UUID to find. If vmSearch is true, the uuid can be either BIOS or instance UUID.
        
        :param vmSearch: If true, search for virtual machines, otherwise search for hosts.
        
        :param instanceUuid: Should only be set when vmSearch is true. If specified, search for virtual machines whose instance UUID matches the given uuid. Otherwise, search for virtual machines whose BIOS UUID matches the given uuid.vSphere API 4.0
        
        '''
        return self.delegate("FindByUuid")(datacenter, uuid, vmSearch, instanceUuid)
    
    def FindChild(self, entity, name):
        '''Finds a particular child based on a managed entity name. This only searches the
        immediate children of a managed entity. For a Datacenter, the host and vm
        folders are considered children. For a ComputeResource, the hosts and root
        ResourcePool are considered children.
        
        :param entity: A reference to a managed entity.
        
        :param name: The name of the child object.
        
        '''
        return self.delegate("FindChild")(entity, name)