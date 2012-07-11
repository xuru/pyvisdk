
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDiskManager(BaseEntity):
    '''This managed object type provides a way to manage and manipulate virtual disks
    on datastores. The source and the destination names are in the form of a URL or
    a datastore path.A URL has the formwhere* is or . * specifies the hostname or
    IP address of the VirtualCenter or ESX server and optionally the port. * is the
    inventory path to the Datacenter containing the Datastore. * is the name of the
    Datastore. * is a slash-delimited path from the root of the datastore.A
    datastore path has the formwhere* is the datastore name. * is a slash-delimited
    path from the root of the datastore.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.VirtualDiskManager):
        super(VirtualDiskManager, self).__init__(core, name=name, ref=ref, type=type)

    

    
    
    def CopyVirtualDisk_Task(self, sourceName, destName, sourceDatacenter=None, destDatacenter=None, destSpec=None, force=None):
        '''Copy a virtual disk, performing conversions as specified in the spec.Copy a
        virtual disk, performing conversions as specified in the spec.Copy a virtual
        disk, performing conversions as specified in the spec.Copy a virtual disk,
        performing conversions as specified in the spec.
        
        :param sourceName: The name of the source, either a datastore path or a URL referring to the virtual disk to be copied.
        
        :param sourceDatacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,must be a URL.
        
        :param destName: The name of the destination, either a datastore path or a URL referring to the virtual disk to be created.
        
        :param destDatacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter, it is assumed that the destination path belongs to the source datacenter.
        
        :param destSpec: The specification of the virtual disk to be created. If not specified, a preallocated format and busLogic adapter type is assumed.
        
        :param force: The force flag is currently ignored. The FileAlreadyExists fault is thrown if the destination file already exists.
        
        '''
        return self.delegate("CopyVirtualDisk_Task")(sourceName, sourceDatacenter, destName, destDatacenter, destSpec, force)
    
    def CreateVirtualDisk_Task(self, name, spec, datacenter=None):
        '''Create a virtual disk.Create a virtual disk.Create a virtual disk.
        
        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk to be created.
        
        :param datacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,must be a URL.
        
        :param spec: The specification of the virtual disk to be created.
        
        '''
        return self.delegate("CreateVirtualDisk_Task")(name, datacenter, spec)
    
    def DefragmentVirtualDisk_Task(self, name, datacenter=None):
        '''Defragment a sparse virtual disk. This is defragmentation of the virtual disk
        file(s) in the host operating system, not defragmentation of the guest
        operating system filesystem inside the virtual disk.Defragment a sparse virtual
        disk. This is defragmentation of the virtual disk file(s) in the host operating
        system, not defragmentation of the guest operating system filesystem inside the
        virtual disk.Defragment a sparse virtual disk. This is defragmentation of the
        virtual disk file(s) in the host operating system, not defragmentation of the
        guest operating system filesystem inside the virtual disk.
        
        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk that should be defragmented.
        
        :param datacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,must be a URL.
        
        '''
        return self.delegate("DefragmentVirtualDisk_Task")(name, datacenter)
    
    def DeleteVirtualDisk_Task(self, name, datacenter=None):
        '''Delete a virtual disk. All files relating to the disk will be deleted.Delete a
        virtual disk. All files relating to the disk will be deleted.Delete a virtual
        disk. All files relating to the disk will be deleted.
        
        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk to be deleted.
        
        :param datacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,must be a URL.
        
        '''
        return self.delegate("DeleteVirtualDisk_Task")(name, datacenter)
    
    def EagerZeroVirtualDisk_Task(self, name, datacenter=None):
        '''Explicitly zero out unaccessed parts zeroedthick disk. Effectively a no-op if
        the disk is already eagerZeroedThick. Unlike zeroFillVirtualDisk, which wipes
        the entire disk, this operation only affects previously unaccessed parts of the
        disk.Explicitly zero out unaccessed parts zeroedthick disk. Effectively a no-op
        if the disk is already eagerZeroedThick. Unlike zeroFillVirtualDisk, which
        wipes the entire disk, this operation only affects previously unaccessed parts
        of the disk.Explicitly zero out unaccessed parts zeroedthick disk. Effectively
        a no-op if the disk is already eagerZeroedThick. Unlike zeroFillVirtualDisk,
        which wipes the entire disk, this operation only affects previously unaccessed
        parts of the disk.
        
        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk that should be inflated.
        
        :param datacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,must be a URL.
        
        '''
        return self.delegate("EagerZeroVirtualDisk_Task")(name, datacenter)
    
    def ExtendVirtualDisk_Task(self, name, newCapacityKb, datacenter=None, eagerZero=None):
        '''Expand the capacity of a virtual disk to the new capacity. If the eagerZero
        flag is not specified, - the extended disk region of a zerothick disk will be
        zeroedthick - the extended disk region of a eagerzerothick disk will be
        eagerzeroedthick - a thin-provisioned disk will always be extended as a thin-
        provisioned disk. If the eagerZero flag TRUE, the extended region of the disk
        will always be eagerly zeroed. If the eagerZero flag FALSE, the extended region
        of a zeroedthick or eagerzeroedthick the disk will not be eagerly zeroed. This
        condition has no effect on a thin source disk.Expand the capacity of a virtual
        disk to the new capacity. If the eagerZero flag is not specified, - the
        extended disk region of a zerothick disk will be zeroedthick - the extended
        disk region of a eagerzerothick disk will be eagerzeroedthick - a thin-
        provisioned disk will always be extended as a thin-provisioned disk. If the
        eagerZero flag TRUE, the extended region of the disk will always be eagerly
        zeroed. If the eagerZero flag FALSE, the extended region of a zeroedthick or
        eagerzeroedthick the disk will not be eagerly zeroed. This condition has no
        effect on a thin source disk.Expand the capacity of a virtual disk to the new
        capacity. If the eagerZero flag is not specified, - the extended disk region of
        a zerothick disk will be zeroedthick - the extended disk region of a
        eagerzerothick disk will be eagerzeroedthick - a thin-provisioned disk will
        always be extended as a thin-provisioned disk. If the eagerZero flag TRUE, the
        extended region of the disk will always be eagerly zeroed. If the eagerZero
        flag FALSE, the extended region of a zeroedthick or eagerzeroedthick the disk
        will not be eagerly zeroed. This condition has no effect on a thin source disk.
        
        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk whose capacity should be expanded.
        
        :param datacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,must be a URL.
        
        :param newCapacityKb: The new capacty of the virtual disk in Kb.
        
        :param eagerZero: If true, the extended part of the disk will be explicitly filled with zeroes.vSphere API 4.0
        
        '''
        return self.delegate("ExtendVirtualDisk_Task")(name, datacenter, newCapacityKb, eagerZero)
    
    def InflateVirtualDisk_Task(self, name, datacenter=None):
        '''Inflate a sparse or thin-provisioned virtual disk up to the full size.
        Additional space allocated to the disk as a result of this operation will be
        filled with zeroes.Inflate a sparse or thin-provisioned virtual disk up to the
        full size. Additional space allocated to the disk as a result of this operation
        will be filled with zeroes.Inflate a sparse or thin-provisioned virtual disk up
        to the full size. Additional space allocated to the disk as a result of this
        operation will be filled with zeroes.
        
        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk that should be inflated.
        
        :param datacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,must be a URL.
        
        '''
        return self.delegate("InflateVirtualDisk_Task")(name, datacenter)
    
    def MoveVirtualDisk_Task(self, sourceName, destName, sourceDatacenter=None, destDatacenter=None, force=None):
        '''Move a virtual disk and all related files from the source location specified by
        <code>sourceName</code> and <code>sourceDatacenter</code> to the destination
        location specified by <code>destName</code> and <code>destDatacenter</code>.
        
        :param sourceName: The name of the source, either a datastore path or a URL referring to the virtual disk to be moved.
        
        :param sourceDatacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,must be a URL.
        
        :param destName: The name of the destination, either a datastore path or a URL referring to the destination virtual disk.
        
        :param destDatacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter, it is assumed that the destination path belongs to the source datacenter.
        
        :param force: If true, overwrite any indentically named disk at the destination. If not specified, it is assumed to be false
        
        '''
        return self.delegate("MoveVirtualDisk_Task")(sourceName, sourceDatacenter, destName, destDatacenter, force)
    
    def QueryVirtualDiskFragmentation(self, name, datacenter=None):
        '''Return the percentage of fragmentation of the sparse virtual disk. This is the
        fragmentation of virtual disk file(s) in the host operating system, not the
        fragmentation of the guest operating systemS filesystem inside the virtual
        disk.Return the percentage of fragmentation of the sparse virtual disk. This is
        the fragmentation of virtual disk file(s) in the host operating system, not the
        fragmentation of the guest operating systemS filesystem inside the virtual
        disk.Return the percentage of fragmentation of the sparse virtual disk. This is
        the fragmentation of virtual disk file(s) in the host operating system, not the
        fragmentation of the guest operating systemS filesystem inside the virtual
        disk.
        
        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk for which to return the percentage of fragmentation.
        
        :param datacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,must be a URL.
        
        '''
        return self.delegate("QueryVirtualDiskFragmentation")(name, datacenter)
    
    def QueryVirtualDiskGeometry(self, name, datacenter=None):
        '''Get the disk geometry information for the virtual disk.Get the disk geometry
        information for the virtual disk.Get the disk geometry information for the
        virtual disk.
        
        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk from which to get geometry information.
        
        :param datacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,must be a URL.
        
        '''
        return self.delegate("QueryVirtualDiskGeometry")(name, datacenter)
    
    def QueryVirtualDiskUuid(self, name, datacenter=None):
        '''Get the virtual disk SCSI inquiry page 0x83 data.Get the virtual disk SCSI
        inquiry page 0x83 data.Get the virtual disk SCSI inquiry page 0x83 data.
        
        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk from which to get SCSI inquiry page 0x83 data.
        
        :param datacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,must be a URL.
        
        '''
        return self.delegate("QueryVirtualDiskUuid")(name, datacenter)
    
    def SetVirtualDiskUuid(self, name, uuid, datacenter=None):
        '''Set the virtual disk SCSI inquiry page 0x83 data.Set the virtual disk SCSI
        inquiry page 0x83 data.Set the virtual disk SCSI inquiry page 0x83 data.
        
        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk whose SCSI inquiry page 0x83 data should be set.
        
        :param datacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,must be a URL.
        
        :param uuid: The hex representation of the unique ID for this virtual disk.
        
        '''
        return self.delegate("SetVirtualDiskUuid")(name, datacenter, uuid)
    
    def ShrinkVirtualDisk_Task(self, name, datacenter=None, copy=None):
        '''Shrink a sparse virtual disk.Shrink a sparse virtual disk.Shrink a sparse
        virtual disk.
        
        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk that should be shrink.
        
        :param datacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,must be a URL.
        
        :param copy: If true or omitted, performs shrink in copy-shrink mode, otherwise shrink in in-place mode.
        
        '''
        return self.delegate("ShrinkVirtualDisk_Task")(name, datacenter, copy)
    
    def ZeroFillVirtualDisk_Task(self, name, datacenter=None):
        '''Overwrite all blocks of the virtual disk with zeros. All data will be
        lost.Overwrite all blocks of the virtual disk with zeros. All data will be
        lost.Overwrite all blocks of the virtual disk with zeros. All data will be
        lost.
        
        :param name: The name of the disk, either a datastore path or a URL referring to the virtual disk whose blocks should be overwritten with zeroes.
        
        :param datacenter: Ifis a datastore path, the datacenter for that datastore path. Not needed when invoked directly on ESX. If not specified on a call to VirtualCenter,must be a URL.
        
        '''
        return self.delegate("ZeroFillVirtualDisk_Task")(name, datacenter)