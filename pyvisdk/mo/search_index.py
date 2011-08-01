
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class SearchIndex(BaseEntity):
    '''The SearchIndex service allows a client to efficiently query the inventory for a
        specific managed entity by attributes such as UUID, IP address, DNS name,
        or datastore path. Such searches typically return a VirtualMachine or a
        HostSystem. While searching, only objects for which the user has
        sufficient privileges are considered. The findByInventoryPath and
        findChild operations only search on entities for which the user has view
        privileges; all other SearchIndex find operations only search virtual
        machines and hosts for which the user has read privileges. If the user
        does not have sufficient privileges for an object that matches the search
        criteria, that object is not returned.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.SearchIndex):
        # MUST define these
        super(SearchIndex, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def FindAllByIp(self, ip, vmSearch):
        '''Finds all virtual machines or hosts by IP address, where the IP address is in dot-
        decimal notation. For example, 10.17.12.12. The IP address for a virtual
        machine is the one returned from VMware tools, ipAddress.

        :param ip: The dot-decimal notation formatted IP address to find.

        :param vmSearch: If true, search for virtual machines, otherwise search for hosts.


        :rtype: ManagedObjectReference[] to a ManagedEntity[] 

        '''
        
        return self.delegate("FindAllByIp")(ip,vmSearch)
        

    def FindByInventoryPath(self, inventoryPath):
        '''Finds a managed entity based on its location in the inventory. The path is
        separated by slashes ('/'). For example, a path should be of the form "My
        Folder/My Datacenter/vm/Discovered VM/VM1". A leading slash or trailing
        slash is ignored. Thus, the following paths all represents the same
        object: "a/b", "/a/b", "a/b/", and '/a/b/'. Slashes in names must be
        represented using %2f, following the standard URL syntax. Any object in
        the inventory can be retrieved using this method, including resource pools
        and hosts.

        :param inventoryPath: The path to the entity.


        :rtype: ManagedObjectReference to a ManagedEntity 

        '''
        
        return self.delegate("FindByInventoryPath")(inventoryPath)
        

    def FindByUuid(self, vmSearch, uuid):
        '''Finds a virtual machine or host by BIOS or instance UUID.

        :param vmSearch: If true, search for virtual machines, otherwise search for hosts.

        :param uuid: The UUID to find. If vmSearch is true, the uuid can be either BIOS or instance UUID.


        :rtype: ManagedObjectReference to a ManagedEntity 

        '''
        
        return self.delegate("FindByUuid")(vmSearch,uuid)
        

    def FindAllByDnsName(self, dnsName, vmSearch):
        '''Finds all virtual machines or hosts by DNS name. The DNS name for a virtual
        machine is the one returned from VMware tools, hostName.

        :param dnsName: The fully qualified domain name to find.

        :param vmSearch: If true, search for virtual machines, otherwise search for hosts.


        :rtype: ManagedObjectReference[] to a ManagedEntity[] 

        '''
        
        return self.delegate("FindAllByDnsName")(dnsName,vmSearch)
        

    def FindByDnsName(self, dnsName, vmSearch):
        '''Finds a virtual machine or host by DNS name. The DNS name for a virtual machine is
        the one returned from VMware tools, hostName.

        :param dnsName: The fully qualified domain name to find.

        :param vmSearch: if true, search for virtual machines, otherwise search for hosts.


        :rtype: ManagedObjectReference to a ManagedEntity 

        '''
        
        return self.delegate("FindByDnsName")(dnsName,vmSearch)
        

    def FindByIp(self, ip, vmSearch):
        '''Finds a virtual machine or host by IP address, where the IP address is in dot-
        decimal notation. For example, 10.17.12.12. The IP address for a virtual
        machine is the one returned from VMware tools, ipAddress.

        :param ip: The dot-decimal notation formatted IP address to find.

        :param vmSearch: if true, search for virtual machines, otherwise search for hosts.


        :rtype: ManagedObjectReference to a ManagedEntity 

        '''
        
        return self.delegate("FindByIp")(ip,vmSearch)
        

    def FindByDatastorePath(self, path):
        '''Finds a virtual machine by its location on a datastore.

        :param path: A datastore path to the .vmx file for the virtual machine.


        :rtype: ManagedObjectReference to a VirtualMachine 

        '''
        
        return self.delegate("FindByDatastorePath")(path)
        

    def FindChild(self, name):
        '''Finds a particular child based on a managed entity name. This only searches the
        immediate children of a managed entity. For a Datacenter, the host and vm
        folders are considered children. For a ComputeResource, the hosts and root
        ResourcePool are considered children.

        :param name: The name of the child object.


        :rtype: ManagedObjectReference to a ManagedEntity 

        '''
        
        return self.delegate("FindChild")(name)
        

    def FindAllByUuid(self, vmSearch, uuid):
        '''Finds all virtual machines or hosts by UUID.

        :param vmSearch: If true, search for virtual machines, otherwise search for hosts.

        :param uuid: The UUID to find. If vmSearch is true, the UUID can be either BIOS or instance UUID.


        :rtype: ManagedObjectReference[] to a ManagedEntity[] 

        '''
        
        return self.delegate("FindAllByUuid")(vmSearch,uuid)
        
