
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ConfigTarget(DynamicData):
    '''The ConfigTarget class contains information about "physical" devices that can be
        used to back virtual devices.
    '''
    
    def __init__(self, autoVmotion, cdRom, datastore, distributedVirtualPortgroup, distributedVirtualSwitch, floppy, ideDisk, legacyNetworkInfo, maxMemMBOptimalPerf, network, numCpuCores, numCpus, numNumaNodes, parallel, pciPassthrough, resourcePool, scsiDisk, scsiPassthrough, serial, sound, usb):
        # MUST define these
        super(ConfigTarget, self).__init__()
    
        self.data['autoVmotion'] = autoVmotion
        self.data['cdRom'] = cdRom
        self.data['datastore'] = datastore
        self.data['distributedVirtualPortgroup'] = distributedVirtualPortgroup
        self.data['distributedVirtualSwitch'] = distributedVirtualSwitch
        self.data['floppy'] = floppy
        self.data['ideDisk'] = ideDisk
        self.data['legacyNetworkInfo'] = legacyNetworkInfo
        self.data['maxMemMBOptimalPerf'] = maxMemMBOptimalPerf
        self.data['network'] = network
        self.data['numCpuCores'] = numCpuCores
        self.data['numCpus'] = numCpus
        self.data['numNumaNodes'] = numNumaNodes
        self.data['parallel'] = parallel
        self.data['pciPassthrough'] = pciPassthrough
        self.data['resourcePool'] = resourcePool
        self.data['scsiDisk'] = scsiDisk
        self.data['scsiPassthrough'] = scsiPassthrough
        self.data['serial'] = serial
        self.data['sound'] = sound
        self.data['usb'] = usb
    
    
    @property
    def autoVmotion(self):
        '''Information whether a virtual machine with this ConfigTarget can auto vmotion.
        This field is only populated from an Environment browser obtained from a
        virtual machine.
        '''
        return self.data['autoVmotion']

    @property
    def cdRom(self):
        '''List of CD-ROM devices available for use by virtual CD-ROMs. Used for
        VirtualCdromAtapiBackingInfo.
        '''
        return self.data['cdRom']

    @property
    def datastore(self):
        '''List of datastores available for virtual disks and associated storage.
        '''
        return self.data['datastore']

    @property
    def distributedVirtualPortgroup(self):
        '''List of networks available from DistributedVirtualSwitch for virtual network
        adapters.
        '''
        return self.data['distributedVirtualPortgroup']

    @property
    def distributedVirtualSwitch(self):
        '''List of distributed virtual switch available for virtual network adapters.
        '''
        return self.data['distributedVirtualSwitch']

    @property
    def floppy(self):
        '''List of floppy devices available for use by virtual floppies. Used for
        VirtualFloppyDeviceBackingInfo.
        '''
        return self.data['floppy']

    @property
    def ideDisk(self):
        '''List of physical IDE disks that can be used as targets for raw disk backings.
        '''
        return self.data['ideDisk']

    @property
    def legacyNetworkInfo(self):
        '''Legacy switch names when using the LegacyNetworkBacking types.
        '''
        return self.data['legacyNetworkInfo']

    @property
    def maxMemMBOptimalPerf(self):
        '''Maximum recommended memory size, in MB, for creating a new virtual machine.
        '''
        return self.data['maxMemMBOptimalPerf']

    @property
    def network(self):
        '''List of networks available for virtual network adapters.
        '''
        return self.data['network']

    @property
    def numCpuCores(self):
        '''Number of physical CPU cores that are available to run virtual machines.
        '''
        return self.data['numCpuCores']

    @property
    def numCpus(self):
        '''Number of logical CPUs that can be used to run virtual machines.
        '''
        return self.data['numCpus']

    @property
    def numNumaNodes(self):
        '''Number of NUMA nodes.
        '''
        return self.data['numNumaNodes']

    @property
    def parallel(self):
        '''List of parallel devices available to support virtualization. Used for
        VirtualParallelPortDeviceBackingInfo.
        '''
        return self.data['parallel']

    @property
    def pciPassthrough(self):
        '''List of generic PCI devices.
        '''
        return self.data['pciPassthrough']

    @property
    def resourcePool(self):
        '''Information about the current available resources on the current resource pool for
        a virtual machine. This field is only populated from an Environment
        browser obtained from a virtual machine.
        '''
        return self.data['resourcePool']

    @property
    def scsiDisk(self):
        '''List of physical SCSI disks that can be used as targets for raw disk mapping
        backings.
        '''
        return self.data['scsiDisk']

    @property
    def scsiPassthrough(self):
        '''List of generic SCSI devices.
        '''
        return self.data['scsiPassthrough']

    @property
    def serial(self):
        '''List of serial devices available to support virtualization. Used for
        VirtualSerialPortDeviceBackingInfo.
        '''
        return self.data['serial']

    @property
    def sound(self):
        '''List of sound devices available to support virtualization. Used for
        VirtualSoundCardDeviceBackingInfo.
        '''
        return self.data['sound']

    @property
    def usb(self):
        '''List of USB devices on the host that are available to support virtualization. Used
        for VirtualUSBUSBBackingInfo.
        '''
        return self.data['usb']

