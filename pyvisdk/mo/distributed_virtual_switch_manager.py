
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitchManager(BaseEntity):
    '''The interface to provide relevant information about DistributedVirtualSwitch.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.DistributedVirtualSwitchManager):
        super(DistributedVirtualSwitchManager, self).__init__(core, name=name, ref=ref, type=type)

    

    
    
    def QueryAvailableDvsSpec(self):
        '''This operation returns a list of switch product specifications that are
        supported by the vCenter Server.
        
        '''
        return self.delegate("QueryAvailableDvsSpec")()
    
    def QueryCompatibleHostForExistingDvs(self, container, recursive, dvs):
        '''This operation returns a list of hosts that are compatible with the given
        DistributedVirtualSwitch product specification.
        
        :param container: Where to look for hosts. Supported types of objects for this parameter are Datacenter, ComputeResource and Folder.
        
        :param recursive: Whether to search for hosts in the subfolders, if applicable. In the case when container is a Datacenter, the recursive flag is applied to its HostFolder.
        
        :param dvs: Search the host based on the specification published in the compatibleHostComponentProductInfo of a DistributedVirtualSwitch. If not set, it is assumed to be the specification that a DistributedVirtualSwitch would have if it is created with the default DistributedVirtualSwitchProductSpec.
        
        '''
        return self.delegate("QueryCompatibleHostForExistingDvs")(container, recursive, dvs)
    
    def QueryCompatibleHostForNewDvs(self, container, recursive, switchProductSpec=None):
        '''This operation returns a list of hosts that are compatible with the given
        DistributedVirtualSwitch product specification.
        
        :param container: Where to look for hosts. Supported types of objects for this parameter are Datacenter, ComputeResource and Folder.
        
        :param recursive: Whether to search for hosts in the subfolders, if applicable. In the case when container is a Datacenter, the recursive flag is applied to its HostFolder.
        
        :param switchProductSpec: The productSpec of a DistributedVirtualSwitch. If not set, it is assumed to be the default one used for DistributedVirtualSwitch creation.
        
        '''
        return self.delegate("QueryCompatibleHostForNewDvs")(container, recursive, switchProductSpec)
    
    def QueryDvsByUuid(self, uuid):
        '''This operation returns a DistributedVirtualSwitch given a UUID.
        
        :param uuid: 
        
        '''
        return self.delegate("QueryDvsByUuid")(uuid)
    
    def QueryDvsCheckCompatibility(self, hostContainer, dvsProductSpec=None, hostFilterSpec=None):
        '''This operation returns a list of compatibility results. Each compatibility
        result is an object that has a host property and optionally a fault which would
        be populated only if that host is not compatible with a given dvsProductSpec.
        All filters in hostFilerSpecs are ANDed to derive the intersection of hosts
        against which compatibility is checked. If caller did not have view privileges
        on the host entity in an element of the CompatibilityResult array, then that
        entire element would be removed from the CompatibilityResult array. Typical
        uses:This operation returns a list of compatibility results. Each compatibility
        result is an object that has a host property and optionally a fault which would
        be populated only if that host is not compatible with a given dvsProductSpec.
        All filters in hostFilerSpecs are ANDed to derive the intersection of hosts
        against which compatibility is checked. If caller did not have view privileges
        on the host entity in an element of the CompatibilityResult array, then that
        entire element would be removed from the CompatibilityResult array. Typical
        uses:
        
        :param hostContainer: The container of hosts on which we check the compatibility. This container can be a datacenter, folder, or computeResource. We can also include all the hosts in the hierarchy with container as root of the tree.
        
        :param dvsProductSpec: The productSpec of a DistributedVirtualSwitch. If not set, it is assumed to be the default one used for DistributedVirtualSwitch creation for current version.
        
        :param hostFilterSpec: The hosts against which to check compatibility. This is a filterSpec and users can use this to specify all hosts in a container (datacenter, folder, or computeResource), an array of hosts, or hosts that might or might not be a DVS member.
        
        '''
        return self.delegate("QueryDvsCheckCompatibility")(hostContainer, dvsProductSpec, hostFilterSpec)
    
    def QueryDvsCompatibleHostSpec(self, switchProductSpec=None):
        '''This operation returns a list of host product specifications that are
        compatible with the given DistributedVirtualSwitch product specification.
        
        :param switchProductSpec: The productSpec of a DistributedVirtualSwitch. If not set, it is assumed to be the default one used for DistributedVirtualSwitch creation.
        
        '''
        return self.delegate("QueryDvsCompatibleHostSpec")(switchProductSpec)
    
    def QueryDvsConfigTarget(self, host=None, dvs=None):
        '''This operation returns the DistributedVirtualSwitch or
        DistributedVirtualPortgroup config target on a host.
        
        :param host: The host on which the query is to be made. If called directly on the host this parameter need not be specified.
        
        :param dvs: The distributed virtual switch on which the query is to be made. If unspecified the config target will encompass all the distributed virtual switches available on the host.
        
        '''
        return self.delegate("QueryDvsConfigTarget")(host, dvs)
    
    def QueryDvsFeatureCapability(self, switchProductSpec=None):
        '''This operation indicates which version-specific DVS features are available for
        the given DistributedVirtualSwitch product specification.
        
        :param switchProductSpec: The productSpec of a DistributedVirtualSwitch. If not set, it is assumed to be the default one used for DistributedVirtualSwitch creation.
        
        '''
        return self.delegate("QueryDvsFeatureCapability")(switchProductSpec)
    
    def RectifyDvsOnHost_Task(self, hosts):
        '''Update the Distributed Switch configuration on the hosts to bring them in sync
        with the current configuration in vCenter Server.
        
        :param hosts: The hosts to be rectified.
        
        '''
        return self.delegate("RectifyDvsOnHost_Task")(hosts)