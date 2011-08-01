
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitchManager(BaseEntity):
    '''The interface to provide relevant information about DistributedVirtualSwitch.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.DistributedVirtualSwitchManager):
        # MUST define these
        super(DistributedVirtualSwitchManager, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def QueryCompatibleHostForExistingDvs(self, recursive):
        '''This operation returns a list of hosts that are compatible with the given
        DistributedVirtualSwitch product specification.

        :param recursive: Whether to search for hosts in the subfolders, if applicable. In the case when container is a Datacenter, the recursive flag is applied to its HostFolder.


        :rtype: ManagedObjectReference[] to a HostSystem[] 

        '''
        
        return self.delegate("QueryCompatibleHostForExistingDvs")(recursive)
        

    def QueryDvsCheckCompatibility(self, hostContainer):
        '''This operation returns a list of compatibility results. Each compatibility result
        is an object that has a host property and optionally a fault which would
        be populated only if that host is not compatible with a given
        dvsProductSpec. All filters in hostFilerSpecs are ANDed to derive the
        intersection of hosts against which compatibility is checked. If caller
        did not have view privileges on the host entity in an element of the
        CompatibilityResult array, then that entire element would be removed from
        the CompatibilityResult array. Typical uses:

        :param hostContainer: The container of hosts on which we check the compatibility. This container can be a datacenter, folder, or computeResource. We can also include all the hosts in the hierarchy with container as root of the tree.


        :rtype: DistributedVirtualSwitchManagerCompatibilityResult[] 

        '''
        
        return self.delegate("QueryDvsCheckCompatibility")(hostContainer)
        

    def QueryDvsByUuid(self, uuid):
        '''This operation returns a DistributedVirtualSwitch given a UUID.

        :param uuid: 


        :rtype: ManagedObjectReference to a DistributedVirtualSwitch 

        '''
        
        return self.delegate("QueryDvsByUuid")(uuid)
        

    def QueryDvsConfigTarget(self):
        '''This operation returns the DistributedVirtualSwitch or DistributedVirtualPortgroup
        config target on a host.

        :rtype: DVSManagerDvsConfigTarget 

        '''
        
        return self.delegate("QueryDvsConfigTarget")()
        

    def QueryAvailableDvsSpec(self):
        '''This operation returns a list of switch product specifications that are supported
        by the vCenter Server.

        :rtype: DistributedVirtualSwitchProductSpec[] 

        '''
        
        return self.delegate("QueryAvailableDvsSpec")()
        

    def QueryCompatibleHostForNewDvs(self, recursive):
        '''This operation returns a list of hosts that are compatible with the given
        DistributedVirtualSwitch product specification.

        :param recursive: Whether to search for hosts in the subfolders, if applicable. In the case when container is a Datacenter, the recursive flag is applied to its HostFolder.


        :rtype: ManagedObjectReference[] to a HostSystem[] 

        '''
        
        return self.delegate("QueryCompatibleHostForNewDvs")(recursive)
        

    def QueryDvsFeatureCapability(self):
        '''This operation indicates which version-specific DVS features are available for the
        given DistributedVirtualSwitch product specification.

        :rtype: DVSFeatureCapability 

        '''
        
        return self.delegate("QueryDvsFeatureCapability")()
        

    def QueryDvsCompatibleHostSpec(self):
        '''This operation returns a list of host product specifications that are compatible
        with the given DistributedVirtualSwitch product specification.

        :rtype: DistributedVirtualSwitchHostProductSpec[] 

        '''
        
        return self.delegate("QueryDvsCompatibleHostSpec")()
        
