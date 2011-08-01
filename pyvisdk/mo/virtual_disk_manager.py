
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDiskManager(BaseEntity):
    '''NOTE: This managed object type and all of its methods are experimental and subject
        to change in future releases.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.VirtualDiskManager):
        # MUST define these
        super(VirtualDiskManager, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def MoveVirtualDisk_Task(self, sourceName, destName):
        '''Move a virtual disk and all related files from the source location specified by
        sourceName and sourceDatacenter to the destination location specified by
        destName and destDatacenter.

        :param sourceName: The name of the source, either a datastore path or a URL referring to the virtual disk to be moved.

        :param destName: The name of the destination, either a datastore path or a URL referring to the destination virtual disk.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("MoveVirtualDisk_Task")(sourceName,destName)
        

    def CopyVirtualDisk_Task(self, sourceName, destName):
        '''Copy a virtual disk, performing conversions as specified in the spec.If source (or
        destination) name is specified as a URL, then the corresponding datacenter
        parameter may be omitted.Requires Datastore.FileManagement privilege on
        both source and destination datastores.Experimental. Subject to change

        :param sourceName: The name of the source, either a datastore path or a URL referring to the virtual disk to be copied.

        :param destName: The name of the destination, either a datastore path or a URL referring to the virtual disk to be created.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CopyVirtualDisk_Task")(sourceName,destName)
        

    def DeleteVirtualDisk_Task(self, name):
        '''Delete a virtual disk. All files relating to the disk will be deleted.The
        datacenter parameter may be omitted if a URL is used to name the
        disk.Requires Datastore.FileManagement privilege on the datastore where
        the virtual disk is removed.Experimental. Subject to change

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk to be deleted.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("DeleteVirtualDisk_Task")(name)
        

    def EagerZeroVirtualDisk_Task(self, name):
        '''Explicitly zero out unaccessed parts zeroedthick disk. Effectively a no-op if the
        disk is already eagerZeroedThick. Unlike zeroFillVirtualDisk, which wipes
        the entire disk, this operation only affects previously unaccessed parts
        of the disk.The datacenter parameter may be omitted if a URL is used to
        name the disk.Requires Datastore.FileManagement privilege on the datastore
        where the virtual disk resides.Experimental. Subject to change

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk that should be inflated.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("EagerZeroVirtualDisk_Task")(name)
        

    def CreateVirtualDisk_Task(self, name, spec):
        '''Create a virtual disk.The datacenter parameter may be omitted if a URL is used to
        name the disk.Requires Datastore.FileManagement privilege on the datastore
        where the virtual disk is created.Experimental. Subject to change

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk to be created.

        :param spec: The specification of the virtual disk to be created.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CreateVirtualDisk_Task")(name,spec)
        

    def QueryVirtualDiskUuid(self, name):
        '''Get the virtual disk SCSI inquiry page 0x83 data.The datacenter parameter may be
        omitted if a URL is used to name the disk.Requires
        Datastore.FileManagement privilege on the datastore where the virtual disk
        resides.Experimental. Subject to change

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk from which to get SCSI inquiry page 0x83 data.


        :rtype: xsd:string 

        '''
        
        return self.delegate("QueryVirtualDiskUuid")(name)
        

    def ExtendVirtualDisk_Task(self, newCapacityKb, name):
        '''Expand the capacity of a virtual disk to the new capacity. If the eagerZero flag
        is not specified, - the extended disk region of a zerothick disk will be
        zeroedthick - the extended disk region of a eagerzerothick disk will be
        eagerzeroedthick - a thin-provisioned disk will always be extended as a
        thin-provisioned disk. If the eagerZero flag TRUE, the extended region of
        the disk will always be eagerly zeroed. If the eagerZero flag FALSE, the
        extended region of a zeroedthick or eagerzeroedthick the disk will not be
        eagerly zeroed. This condition has no effect on a thin source disk.The
        datacenter parameter may be omitted if a URL is used to name the
        disk.Requires Datastore.FileManagement privilege on the datastore where
        the virtual disk resides.Experimental. Subject to change

        :param newCapacityKb: The new capacty of the virtual disk in Kb.

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk whose capacity should be expanded.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("ExtendVirtualDisk_Task")(newCapacityKb,name)
        

    def SetVirtualDiskUuid(self, name, uuid):
        '''Set the virtual disk SCSI inquiry page 0x83 data.The datacenter parameter may be
        omitted if a URL is used to name the disk.Requires
        Datastore.FileManagement privilege on the datastore where the virtual disk
        resides.Experimental. Subject to change

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk whose SCSI inquiry page 0x83 data should be set.

        :param uuid: The hex representation of the unique ID for this virtual disk.

        '''
        
        return self.delegate("SetVirtualDiskUuid")(name,uuid)
        

    def QueryVirtualDiskFragmentation(self, name):
        '''Return the percentage of fragmentation of the sparse virtual disk. This is the
        fragmentation of virtual disk file(s) in the host operating system, not
        the fragmentation of the guest operating systemS filesystem inside the
        virtual disk.The datacenter parameter may be omitted if a URL is used to
        name the disk.Requires Datastore.FileManagement privilege on the datastore
        where the virtual disk resides.Experimental. Subject to change

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk for which to return the percentage of fragmentation.


        :rtype: xsd:int 

        '''
        
        return self.delegate("QueryVirtualDiskFragmentation")(name)
        

    def InflateVirtualDisk_Task(self, name):
        '''Inflate a sparse or thin-provisioned virtual disk up to the full size. Additional
        space allocated to the disk as a result of this operation will be filled
        with zeroes.The datacenter parameter may be omitted if a URL is used to
        name the disk.Requires Datastore.FileManagement privilege on the datastore
        where the virtual disk resides.Experimental. Subject to change

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk that should be inflated.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("InflateVirtualDisk_Task")(name)
        

    def QueryVirtualDiskGeometry(self, name):
        '''Get the disk geometry information for the virtual disk.The datacenter parameter
        may be omitted if a URL is used to name the disk.Requires
        Datastore.FileManagement privilege on the datastore where the virtual disk
        resides.Experimental. Subject to change

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk from which to get geometry information.


        :rtype: HostDiskDimensionsChs 

        '''
        
        return self.delegate("QueryVirtualDiskGeometry")(name)
        

    def DefragmentVirtualDisk_Task(self, name):
        '''Defragment a sparse virtual disk. This is defragmentation of the virtual disk
        file(s) in the host operating system, not defragmentation of the guest
        operating system filesystem inside the virtual disk.The datacenter
        parameter may be omitted if a URL is used to name the disk.Requires
        Datastore.FileManagement privilege on the datastore where the virtual disk
        resides.Experimental. Subject to change

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk that should be defragmented.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("DefragmentVirtualDisk_Task")(name)
        

    def ShrinkVirtualDisk_Task(self, name):
        '''Shrink a sparse virtual disk.The datacenter parameter may be omitted if a URL is
        used to name the disk.The optional parameter copy specifies whether to
        shrink the disk in copy-shrink mode or in-place mode. In copy-shrink mode,
        additional space is required, but will result in a shrunk disk that is
        also defragmented. In-place shrink does not require additional space, but
        will increase fragmentation. The default behavior is to perform copy-
        shrink if the parameter is not specified.

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk that should be shrink.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("ShrinkVirtualDisk_Task")(name)
        

    def ZeroFillVirtualDisk_Task(self, name):
        '''Overwrite all blocks of the virtual disk with zeros. All data will be lost.The
        datacenter parameter may be omitted if a URL is used to name the
        disk.Requires Datastore.FileManagement privilege on the datastore where
        the virtual disk resides.Experimental. Subject to change

        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk whose blocks should be overwritten with zeroes.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("ZeroFillVirtualDisk_Task")(name)
        
