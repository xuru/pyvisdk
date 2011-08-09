
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineRelocateSpec(DynamicData):
    '''Specification for moving or copying a virtual machine to a different datastore or
        host.
    '''
    
    def __init__(self, datastore, disk, diskMoveType, host, pool, transform):
        # MUST define these
        super(VirtualMachineRelocateSpec, self).__init__()
    
        self.data['datastore'] = datastore
        self.data['disk'] = disk
        self.data['diskMoveType'] = diskMoveType
        self.data['host'] = host
        self.data['pool'] = pool
        self.data['transform'] = transform
    
    
    @property
    def datastore(self):
        '''The datastore where the virtual machine should be located. If not specified, the
        current datastore is used.
        '''
        return self.data['datastore']

    @property
    def disk(self):
        '''An optional list that allows specifying the datastore location for each virtual
        disk.
        '''
        return self.data['disk']

    @property
    def diskMoveType(self):
        '''Manner in which to move the virtual disk to the target datastore. The set of
        possible values is described in VirtualMachineRelocateDiskMoveOptions.
        '''
        return self.data['diskMoveType']

    @property
    def host(self):
        '''The target host for the virtual machine. If not specified, * if resource pool is
        not specified, current host is used. * if resource pool is specified, and
        the target pool represents a stand-alone host, the host is used. * if
        resource pool is specified, and the target pool represents a DRS-enabled
        cluster, a host selected by DRS is used. * if resource pool is specified
        and the target pool represents a cluster without DRS enabled, an
        InvalidArgument exception be thrown.
        '''
        return self.data['host']

    @property
    def pool(self):
        '''The resource pool to which this virtual machine should be attached. For a relocate
        or clone operation to a virtual machine, if the argument is not supplied,
        the current resource pool of virtual machine is used. For a clone
        operation to a template, this argument is ignored. For a clone operation
        from a template to a virtual machine, this argument is required.
        '''
        return self.data['pool']

    @property
    def transform(self):
        '''Transformation to perform on the disks. The backend is free to ignore this hint if
        it is not valid for the current operation. This can be used by clients,
        for example, to create sparse disks for templates.
        '''
        return self.data['transform']

