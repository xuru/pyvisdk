
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDiagnosticSystem(BaseEntity):
    '''The DiagnosticSystem managed object is used to configure the diagnostic
    mechanisms specific to the host. The DiagnosticSystem interface supports the
    following concepts:* Notion of an active diagnostic partition that is selected
    from a set of available partitions. * Ability to create a diagnostic partition
    that gets added to the list of available partitions and could be made active.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostDiagnosticSystem):
        super(HostDiagnosticSystem, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def activePartition(self):
        '''The currently active diagnostic partition.'''
        return self.update('activePartition')

    
    
    def CreateDiagnosticPartition(self, spec):
        '''Creates a diagnostic partition according to the provided create specification.
        On success, this method will create the partition and make the partition the
        active diagnostic partition if specified. On failure, the diagnostic partition
        may exist but may not be active if the partition was supposed to be made
        active.
        
        :param spec: 
        
        '''
        return self.delegate("CreateDiagnosticPartition")(spec)
    
    def QueryAvailablePartition(self):
        '''Retrieves a list of available diagnostic partitions. The server will provide
        the list in order of preference. In general, local diagnostic partitions are
        better than shared diagnostic partitions because of the impossibility of
        multiple servers sharing the same partition. The most preferred diagnostic
        partition will be first in the array.
        
        '''
        return self.delegate("QueryAvailablePartition")()
    
    def QueryPartitionCreateDesc(self, diskUuid, diagnosticType):
        '''For a disk, query for the diagnostic partition creation description. The
        description details how the diagnostic partition will be created on the disk
        and provides a creation specification that is needed to invoke the create
        operation.See HostScsiDiskSee uuid
        
        :param diskUuid: See HostScsiDiskSee uuid
        
        :param diagnosticType: See HostScsiDiskSee uuid
        
        '''
        return self.delegate("QueryPartitionCreateDesc")(diskUuid, diagnosticType)
    
    def QueryPartitionCreateOptions(self, storageType, diagnosticType):
        '''Retrieves a list of disks that can be used to contain a diagnostic partition.
        This list will contain disks that have sufficient space to contain a diagnostic
        partition of the specific type.Retrieves a list of disks that can be used to
        contain a diagnostic partition. This list will contain disks that have
        sufficient space to contain a diagnostic partition of the specific type.
        
        :param storageType: 
        
        :param diagnosticType: 
        
        '''
        return self.delegate("QueryPartitionCreateOptions")(storageType, diagnosticType)
    
    def SelectActivePartition(self, partition=None):
        '''Changes the active diagnostic partition to a different partition. Setting a
        NULL partition will result in unsetting the diagnostic partition.
        
        :param partition: 
        
        '''
        return self.delegate("SelectActivePartition")(partition)