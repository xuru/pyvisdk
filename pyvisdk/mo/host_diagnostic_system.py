
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostDiagnosticSystem(BaseEntity):
    '''The DiagnosticSystem managed object is used to configure the diagnostic mechanisms
        specific to the host. The DiagnosticSystem interface supports the
        following concepts:
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostDiagnosticSystem):
        # MUST define these
        super(HostDiagnosticSystem, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def activePartition(self):
        '''The currently active diagnostic partition.
        '''
        return self.update('activePartition')


    def CreateDiagnosticPartition(self):
        '''Creates a diagnostic partition according to the provided create specification. On
        success, this method will create the partition and make the partition the
        active diagnostic partition if specified. On failure, the diagnostic
        partition may exist but may not be active if the partition was supposed to
        be made active.
        '''
        
        return self.delegate("CreateDiagnosticPartition")()
        

    def QueryAvailablePartition(self):
        '''Retrieves a list of available diagnostic partitions. The server will provide the
        list in order of preference. In general, local diagnostic partitions are
        better than shared diagnostic partitions because of the impossibility of
        multiple servers sharing the same partition. The most preferred diagnostic
        partition will be first in the array.
        '''
        
        return self.delegate("QueryAvailablePartition")()
        

    def QueryPartitionCreateDesc(self):
        '''For a disk, query for the diagnostic partition creation description. The
        description details how the diagnostic partition will be created on the
        disk and provides a creation specification that is needed to invoke the
        create operation. See HostScsiDisk See uuid
        '''
        
        return self.delegate("QueryPartitionCreateDesc")()
        

    def QueryPartitionCreateOptions(self):
        '''Retrieves a list of disks that can be used to contain a diagnostic partition. This
        list will contain disks that have sufficient space to contain a diagnostic
        partition of the specific type.The choices will be returned in the order
        that is most preferable as determined by the system.
        '''
        
        return self.delegate("QueryPartitionCreateOptions")()
        

    def SelectActivePartition(self):
        '''Changes the active diagnostic partition to a different partition. Setting a NULL
        partition will result in unsetting the diagnostic partition.
        '''
        
        return self.delegate("SelectActivePartition")()
        
