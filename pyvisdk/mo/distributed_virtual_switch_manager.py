
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
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryAvailableDvsSpec")()
    
    def QueryCompatibleHostForExistingDvs(self):
        '''This operation returns a list of hosts that are compatible with the given
        DistributedVirtualSwitch product specification.
        :rtype: ManagedObjectReference[] to a HostSystem[]
        :returns: 
        '''
        return self.delegate("QueryCompatibleHostForExistingDvs")()
    
    def QueryCompatibleHostForNewDvs(self):
        '''This operation returns a list of hosts that are compatible with the given
        DistributedVirtualSwitch product specification.
        :rtype: ManagedObjectReference[] to a HostSystem[]
        :returns: 
        '''
        return self.delegate("QueryCompatibleHostForNewDvs")()
    
    def QueryDvsByUuid(self):
        '''This operation returns a DistributedVirtualSwitch given a UUID.
        :rtype: ManagedObjectReference to a DistributedVirtualSwitch
        :returns: 
        '''
        return self.delegate("QueryDvsByUuid")()
    
    def QueryDvsCheckCompatibility(self):
        '''This operation returns a list of compatibility results. Each compatibility
        result is an object that has a host property and optionally a fault which would
        be populated only if that host is not compatible with a given dvsProductSpec.
        All filters in hostFilerSpecs are ANDed to derive the intersection of hosts
        against which compatibility is checked. If caller did not have view privileges
        on the host entity in an element of the CompatibilityResult array, then that
        entire element would be removed from the CompatibilityResult array. Typical
        uses:
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryDvsCheckCompatibility")()
    
    def QueryDvsCompatibleHostSpec(self):
        '''This operation returns a list of host product specifications that are
        compatible with the given DistributedVirtualSwitch product specification.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryDvsCompatibleHostSpec")()
    
    def QueryDvsConfigTarget(self):
        '''This operation returns the DistributedVirtualSwitch or
        DistributedVirtualPortgroup config target on a host.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryDvsConfigTarget")()
    
    def QueryDvsFeatureCapability(self):
        '''This operation indicates which version-specific DVS features are available for
        the given DistributedVirtualSwitch product specification.
        :rtype: 
        :returns: 
        '''
        return self.delegate("QueryDvsFeatureCapability")()