
from pyvisdk.do.ovf_manager_common_params import OvfManagerCommonParams
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OvfCreateImportSpecParams(OvfManagerCommonParams):
    '''Parameters for deploying an OVF.
    '''
    
    def __init__(self, diskProvisioning, entityName, hostSystem, ipAllocationPolicy, ipProtocol, networkMapping, propertyMapping, resourceMapping):
        # MUST define these
        super(OvfCreateImportSpecParams, self).__init__()
    
        self.data['diskProvisioning'] = diskProvisioning
        self.data['entityName'] = entityName
        self.data['hostSystem'] = hostSystem
        self.data['ipAllocationPolicy'] = ipAllocationPolicy
        self.data['ipProtocol'] = ipProtocol
        self.data['networkMapping'] = networkMapping
        self.data['propertyMapping'] = propertyMapping
        self.data['resourceMapping'] = resourceMapping
    
    
    @property
    def diskProvisioning(self):
        '''An optional disk provisioning. If set, all the disks in the deployed OVF will have
        get the same specified disk type (e.g., thin provisioned). The valide
        values for disk provisioning are: * monolithicSparse * monolithicFlat *
        twoGbMaxExtentSparse * twoGbMaxExtentFlat * thin * thick * sparse * flat
        '''
        return self.data['diskProvisioning']

    @property
    def entityName(self):
        '''The name to set on the entity (more precisely, on the top-level vApp or VM of the
        entity) as it appears in VI. If empty, the product name is obtained from
        the ProductSection of the descriptor. If that name is not specified, the
        ovf:id of the top-level entity is used.
        '''
        return self.data['entityName']

    @property
    def hostSystem(self):
        '''The host to validate the OVF descriptor against, if it cannot be deduced from the
        resource pool.
        '''
        return self.data['hostSystem']

    @property
    def ipAllocationPolicy(self):
        '''The IP allocation policy chosen by the caller.
        '''
        return self.data['ipAllocationPolicy']

    @property
    def ipProtocol(self):
        '''The IP protocol chosen by the caller.
        '''
        return self.data['ipProtocol']

    @property
    def networkMapping(self):
        '''The mapping of network identifiers from the descriptor to networks in the VI
        infrastructure.
        '''
        return self.data['networkMapping']

    @property
    def propertyMapping(self):
        '''The assignment of values to the properties found in the descriptor. If no value is
        specified for an option, the default value from the descriptor is used.
        '''
        return self.data['propertyMapping']

    @property
    def resourceMapping(self):
        '''The resource configuration for the created vApp. This can be used to distribute a
        vApp across multiple resource pools (and create linked children).
        '''
        return self.data['resourceMapping']

