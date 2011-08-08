
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
    
    

    def QueryAvailableDvsSpec(self, switchProductSpec):
        '''This operation returns a list of switch product specifications that are supported
        by the vCenter Server.

        :param switchProductSpec: The productSpec of a DistributedVirtualSwitch. If not set, it is assumed to be the
        default one used for DistributedVirtualSwitch creation.


        :rtype: DVSFeatureCapability 

        '''
        
        return self.delegate("QueryAvailableDvsSpec")(switchProductSpec)
        

    def QueryCompatibleHostForExistingDvs(self, switchProductSpec):
        '''This operation returns a list of hosts that are compatible with the given
        DistributedVirtualSwitch product specification.

        :param switchProductSpec: The productSpec of a DistributedVirtualSwitch. If not set, it is assumed to be the
        default one used for DistributedVirtualSwitch creation.


        :rtype: DVSFeatureCapability 

        '''
        
        return self.delegate("QueryCompatibleHostForExistingDvs")(switchProductSpec)
        

    def QueryCompatibleHostForNewDvs(self, switchProductSpec):
        '''This operation returns a list of hosts that are compatible with the given
        DistributedVirtualSwitch product specification.

        :param switchProductSpec: The productSpec of a DistributedVirtualSwitch. If not set, it is assumed to be the
        default one used for DistributedVirtualSwitch creation.


        :rtype: DVSFeatureCapability 

        '''
        
        return self.delegate("QueryCompatibleHostForNewDvs")(switchProductSpec)
        

    def QueryDvsByUuid(self, switchProductSpec):
        '''This operation returns a DistributedVirtualSwitch given a UUID.

        :param switchProductSpec: The productSpec of a DistributedVirtualSwitch. If not set, it is assumed to be the
        default one used for DistributedVirtualSwitch creation.


        :rtype: DVSFeatureCapability 

        '''
        
        return self.delegate("QueryDvsByUuid")(switchProductSpec)
        

    def QueryDvsCheckCompatibility(self, switchProductSpec):
        '''This operation returns a list of compatibility results. Each compatibility result
        is an object that has a host property and optionally a fault which would
        be populated only if that host is not compatible with a given
        dvsProductSpec. All filters in hostFilerSpecs are ANDed to derive the
        intersection of hosts against which compatibility is checked. If caller
        did not have view privileges on the host entity in an element of the
        CompatibilityResult array, then that entire element would be removed from
        the CompatibilityResult array. Typical uses:

        :param switchProductSpec: The productSpec of a DistributedVirtualSwitch. If not set, it is assumed to be the
        default one used for DistributedVirtualSwitch creation.


        :rtype: DVSFeatureCapability 

        '''
        
        return self.delegate("QueryDvsCheckCompatibility")(switchProductSpec)
        

    def QueryDvsCompatibleHostSpec(self, switchProductSpec):
        '''This operation returns a list of host product specifications that are compatible
        with the given DistributedVirtualSwitch product specification.

        :param switchProductSpec: The productSpec of a DistributedVirtualSwitch. If not set, it is assumed to be the
        default one used for DistributedVirtualSwitch creation.


        :rtype: DVSFeatureCapability 

        '''
        
        return self.delegate("QueryDvsCompatibleHostSpec")(switchProductSpec)
        

    def QueryDvsConfigTarget(self, switchProductSpec):
        '''This operation returns the DistributedVirtualSwitch or DistributedVirtualPortgroup
        config target on a host.

        :param switchProductSpec: The productSpec of a DistributedVirtualSwitch. If not set, it is assumed to be the
        default one used for DistributedVirtualSwitch creation.


        :rtype: DVSFeatureCapability 

        '''
        
        return self.delegate("QueryDvsConfigTarget")(switchProductSpec)
        

    def QueryDvsFeatureCapability(self, switchProductSpec):
        '''This operation indicates which version-specific DVS features are available for the
        given DistributedVirtualSwitch product specification.

        :param switchProductSpec: The productSpec of a DistributedVirtualSwitch. If not set, it is assumed to be the
        default one used for DistributedVirtualSwitch creation.


        :rtype: DVSFeatureCapability 

        '''
        
        return self.delegate("QueryDvsFeatureCapability")(switchProductSpec)
        
