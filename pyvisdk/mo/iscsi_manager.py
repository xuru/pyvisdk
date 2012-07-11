
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class IscsiManager(BaseEntity):
    '''This managed object provides interfaces for mapping VMkernel NIC to iSCSI Host
    Bus Adapter.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.IscsiManager):
        super(IscsiManager, self).__init__(core, name=name, ref=ref, type=type)

    

    
    
    def BindVnic(self, iScsiHbaName, vnicDevice):
        '''Bind a Virtual NIC to be used for an iSCSI adapter
        
        :param iScsiHbaName: iSCSI adapter name for which the Virtual NIC to be added.
        
        :param vnicDevice: Virtual NIC that is to be bound to the iSCSI HBA
        
        '''
        return self.delegate("BindVnic")(iScsiHbaName, vnicDevice)
    
    def QueryBoundVnics(self, iScsiHbaName):
        '''Query the list of Virtual NICs that are bound to a given iSCSI HBA.
        
        :param iScsiHbaName: iSCSI adapter name for which the method to be applied.
        
        '''
        return self.delegate("QueryBoundVnics")(iScsiHbaName)
    
    def QueryCandidateNics(self, iScsiHbaName):
        '''Query the candidate Virtual NICs and Physical NICs that can be used for Port-
        Binding. For dependent offload adapters, the Virtual NIC should be attached to
        the physical NIC associated with the hardware function.
        
        :param iScsiHbaName: iSCSI Adapter name for which the method to be applied.
        
        '''
        return self.delegate("QueryCandidateNics")(iScsiHbaName)
    
    def QueryMigrationDependencies(self, pnicDevice):
        '''Query the dependency table for a migration operation of a given Physical NIC.
        
        :param pnicDevice: List of Physical NICs to be migrated
        
        '''
        return self.delegate("QueryMigrationDependencies")(pnicDevice)
    
    def QueryPnicStatus(self, pnicDevice):
        '''Query if Physical NIC device is used for iSCSI.
        
        :param pnicDevice: Physical NIC device name to check the status for
        
        '''
        return self.delegate("QueryPnicStatus")(pnicDevice)
    
    def QueryVnicStatus(self, vnicDevice):
        '''Query the status of Virtual NIC association with the iSCSI.
        
        :param vnicDevice: Virtual NIC device to check the status for
        
        '''
        return self.delegate("QueryVnicStatus")(vnicDevice)
    
    def UnbindVnic(self, iScsiHbaName, vnicDevice, force):
        '''Unbind Virtual NIC binding from an iSCSI adapter.
        
        :param iScsiHbaName: iSCSI adapter name for which the Virtual NIC to be removed.
        
        :param vnicDevice: Virtual NIC that is to be removed from the iSCSI HBA
        
        :param force: 
        
        '''
        return self.delegate("UnbindVnic")(iScsiHbaName, vnicDevice, force)