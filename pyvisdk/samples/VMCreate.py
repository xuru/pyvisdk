'''
Created on Aug 14, 2011

@author: eplaster
'''
import logging
import os.path
from pyvisdk.app import PyvisdkApp
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.do.description import Description
from pyvisdk.do.virtual_cdrom import VirtualCdrom
from pyvisdk.do.virtual_cdrom_iso_backing_info import VirtualCdromIsoBackingInfo
from pyvisdk.do.virtual_cdrom_remote_passthrough_backing_info import \
    VirtualCdromRemotePassthroughBackingInfo
from pyvisdk.do.virtual_device_config_spec import VirtualDeviceConfigSpec
from pyvisdk.do.virtual_device_connect_info import VirtualDeviceConnectInfo
from pyvisdk.do.virtual_disk import VirtualDisk
from pyvisdk.do.virtual_disk_flat_ver2_backing_info import \
    VirtualDiskFlatVer2BackingInfo
from pyvisdk.do.virtual_ethernet_card_network_backing_info import \
    VirtualEthernetCardNetworkBackingInfo
from pyvisdk.do.virtual_ethernet_card_distributed_virtual_port_backing_info import \
    VirtualEthernetCardDistributedVirtualPortBackingInfo
from pyvisdk.do.virtual_ide_controller import VirtualIDEController
from pyvisdk.do.virtual_lsi_logic_controller import VirtualLsiLogicController
from pyvisdk.do.virtual_machine_config_spec import VirtualMachineConfigSpec
from pyvisdk.do.virtual_machine_file_info import VirtualMachineFileInfo
from pyvisdk.do.virtual_vmxnet3 import VirtualVmxnet3
from pyvisdk.do.tools_config_info import ToolsConfigInfo
from pyvisdk.do.virtual_machine_flag_info import VirtualMachineFlagInfo
from pyvisdk.do.distributed_virtual_switch_port_connection import DistributedVirtualSwitchPortConnection
from pyvisdk.do.virtual_machine_default_power_op_info import VirtualMachineDefaultPowerOpInfo
from pyvisdk.enums.virtual_device_config_spec_file_operation import \
    VirtualDeviceConfigSpecFileOperation
from pyvisdk.enums.virtual_device_config_spec_operation import \
    VirtualDeviceConfigSpecOperation
from pyvisdk.enums.virtual_scsi_sharing import VirtualSCSISharing
from pyvisdk.mo.datacenter import Datacenter
from pyvisdk.mo.host_system import HostSystem

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)


class VMCreate(PyvisdkApp):
    '''
    This sample creates a VM.
    
    Parameters:
    vmname :       [required]: Name of the virtual machine
    datacentername [required]: Name of the datacenter
    hostname :     [optional]: Name fo the host
    guestosid:     [optional]: Type of Guest OS
    cpucount:      [optional]: Total cpu count
    disksize       [optional]: Size of the Disk
    memorysize     [optional]: Size of the Memory in the blocks of 1024 MB
    datastorename  [optional]: Name of datastore
    
    '''

    def __init__(self):
        super(VMCreate, self).__init__()
        
        self.parser.add_option("", "--vmname", dest="vmname", help="Name of the virtual machine")
        self.parser.add_option("", "--datacenter", dest="datacenter", help="Name of the datacenter")
        self.parser.add_option("", "--hostname", dest="hostname", help="Name of the host")
        self.parser.add_option("", "--guestosid", dest="guestosid", help="Type of Guest OS")
        self.parser.add_option("", "--datastore", dest="datastore", help="Name of datastore")
        self.parser.add_option("", "--cpucount", dest="cpucount", default=1, type="int", help="Total cpu count")
        self.parser.add_option("", "--disksize", dest="disksize", default=1048576, type="int", help="Size of the disk in KB")
        self.parser.add_option("", "--memory", dest="memory", default=1024, type="long", help="Size of the memory in blocks of MB")
        self.parse()
        
        # connect and login to the vcenter or ESX server
        self.connect()
        
    def setup(self):
        disk_ctlr_key = 1
        self.datacenter         = self.vim.getDatacenter(self.options.datacenter)
        self.host_folder        = self.datacenter.hostFolder
        self.vm_folder          = self.datacenter.vmFolder
        self.host_system        = self._get_host_system()
        self.compute_resource   = self._get_compute_resource(self.host_folder)
        self.resource_pool      = self.compute_resource.resourcePool
        
        self.default_devs       = self._getDefaultDevices(self.compute_resource, self.host_system)
        self.config_target      = self._getConfigTargetForHost(self.compute_resource, self.host_system)
        self.datastore          = self._get_datastore(self.config_target)
        self.datastore_volume   = self._getVolumeName(self.datastore.name)
        
        # new parts...
        self.scsi_controller    = self._process_scsi_controller(disk_ctlr_key)
        self.ide_controller     = self._process_ide_controller()
        self.cdrom              = self._process_cdrom(disk_ctlr_key)
        self.disk               = self._process_virtual_disk(disk_ctlr_key)
        self.nic                = self._process_nic()
        
    def create(self):
        self.setup()
        
        device_config_spec = [ self.scsi_controller, self.disk ]
        if self.ide_controller:
            device_config_spec += [self.cdrom, self.nic]
        
        vmfi = VirtualMachineFileInfo(self.vim, vmPathName=self.datastore_volume)
        
        tools = ToolsConfigInfo(self.vim, afterPowerOn = True, afterResume = True, beforeGuestStandby = True, 
                                beforeGuestShutdown = True, beforeGuestReboot = True)
            
        flags = VirtualMachineFlagInfo(self.vim, snapshotPowerOffBehavior="powerOff")

        power_info = VirtualMachineDefaultPowerOpInfo(self.vim, powerOffType="preset", suspendType="preset", resetType="preset", standbyAction="powerOnSuspend")
        
        print "name: ", self.options.vmname, type(self.options.vmname)
        print "memory: ", self.options.memory, type(self.options.memory)
        print "cpus: ", self.options.cpucount, type(self.options.cpucount)
        print "Creating %s with %dMB of memory and %d CPUs." % (self.options.vmname, self.options.memory, self.options.cpucount)
        
        vmspec = VirtualMachineConfigSpec(self.vim, 
            name = self.options.vmname,
            guestId = self.options.guestosid,
            annotation = "VMCreate made this...",
            files=vmfi, 
            numCPUs = int(self.options.cpucount),
            memoryMB = int(self.options.memory),
            tools=tools,
            flags = flags,
            powerOpInfo = power_info,
            
            deviceChange=device_config_spec,
            changeTrackingEnabled = True,
            version='vmx-07'
            )
        
        self.vm_folder.CreateVM_Task(vmspec, self.resource_pool, self.host_system)
        self.disconnect()
        

    def _get_host_system(self):
        log.info("Getting host system...")
        if self.options.hostname:
            host_system = self.vim.getHostSystem(self.options.hostname)
        else:
            host_system = self.vim.getHostSystems()[0]
        return host_system
            
    def _get_compute_resource(self, host_folder):
        log.info("Getting compute resource...")
        compute_resource = None
        for rc in host_folder.getDecendants(ManagedObjectTypes.ComputeResource):
            for hr in rc.host:
                if hr.name == self.host_system.name:
                    compute_resource = rc
                    break
        return compute_resource
    
    def _getVolumeName(self, volName):
        log.info("Getting volume name...")
        volume_name = None
        if volName and (len(volName) > 0):
            volume_name = "[" + volName + "]"
        else:
            volume_name = "[Local]"
        return volume_name
    
    def _process_scsi_controller(self, disk_ctlr_key):
        log.info("Processing scsi controller info...")
        
        scsi_ctrl = VirtualLsiLogicController(self.vim, 
                busNumber=0, key = 1, sharedBus = VirtualSCSISharing.noSharing)
        scsi_ctrl.deviceInfo = Description(self.vim, 
                label="SCSI controller 0", summary="LSI Logic")
        
        scsi_ctrl_spec = VirtualDeviceConfigSpec(self.vim,
                operation = VirtualDeviceConfigSpecOperation.add,
                device = scsi_ctrl )
        delattr(scsi_ctrl_spec, 'fileOperation')
        return scsi_ctrl_spec
    
    def _process_ide_controller(self):
        log.info("Processing IDE controller info...")
        ide_controller = None
        for dev in self.default_devs:
            if dev.__class__.__name__ == 'VirtualIDEController':
                ide_controller = dev
                break
            
        return ide_controller
    
    def _process_floppy(self):
        log.info("Processing Floppy info...")
    
    def _get_datastore(self, config_target):
        log.info("Getting datastore info...")
        datastore = None
        for vds_info in config_target.datastore:
            ds_summary = vds_info.datastore
            
            # if we didn't specify what datastore, return the first one in our config target
            if not self.options.datastore:
                return ds_summary.datastore
            
            if ds_summary.name == self.options.datastore:
                datastore = ds_summary.datastore
                break
        return datastore
            
    def _process_cdrom(self, disk_ctlr_key):
        log.info("Processing cdrom info...")
        
        backing = VirtualCdromRemotePassthroughBackingInfo(self.vim, exclusive=False, deviceName="cdrom0")
        
        cdrom   = VirtualCdrom(self.vim, 
                        controllerKey=self.ide_controller.key, 
                        key=20, 
                        backing=backing, 
                        unitNumber=0)
        
        # let's connect it on boot...
        vdci = VirtualDeviceConnectInfo(self.vim, allowGuestControl=False, connected=True, startConnected=True)
        cdrom.connectable = vdci
        
        # Add some info
        desc = Description(self.vim,
            label = "CD-ROM Device cdrom0",
            summary = "The CD-ROM device for this virtual machine.")
        cdrom.deviceInfo = desc
        
        cdrom_spec = VirtualDeviceConfigSpec(self.vim,
                operation = VirtualDeviceConfigSpecOperation.add,
                device = cdrom)
        
        delattr(cdrom_spec, 'fileOperation')
        return cdrom_spec
    
    def _process_virtual_disk(self, disk_ctlr_key, unit_number=0):
        log.info("Processing virtual disk info...")
        size = self.options.disksize
        
        desc = Description(self.vim,
            label = "Hard Disk 1",
            summary = "%d KB" % int(size))
        
        disk_spec = VirtualDeviceConfigSpec(self.vim, 
                fileOperation = VirtualDeviceConfigSpecFileOperation.create,
                operation = VirtualDeviceConfigSpecOperation.add )
        
        backing = VirtualDiskFlatVer2BackingInfo(self.vim, 
                diskMode = "persistent",
                fileName = self.datastore_volume
                )
        delattr(backing, "datastore")
        
        disk = VirtualDisk(self.vim, 
                key=0, 
                unitNumber=unit_number, 
                controllerKey=1, 
                capacityInKB=int(size),
                backing=backing)
        
        disk_spec.device = disk
        return disk_spec
        
    def _process_nic(self):
        log.info("Processing NIC info...")
        networkname = "VLAN-2"
        network = None
        
        if self.config_target.network:
            for netinfo in self.config_target.network:
                summary = netinfo.network
                
                if summary.name == networkname:
                    if summary.isAccessible:
                        network = summary.network
                    else:
                        raise AssertionError("Network is not accessible: %s" % summary.name)
                    break
            backing = VirtualEthernetCardNetworkBackingInfo(self.vim, network=network.ref, deviceName=network.name)
                    
        elif self.config_target.distributedVirtualPortgroup:
            for pgi in self.config_target.distributedVirtualPortgroup:
                if networkname in pgi.portgroupName:
                    port_group = pgi
                    break
            
            connection =  DistributedVirtualSwitchPortConnection(self.vim, switchUuid=port_group.switchUuid)
            backing = VirtualEthernetCardDistributedVirtualPortBackingInfo(self.vim, port=connection)
        
        
        nic = VirtualVmxnet3(self.vim,
            addressType = "generated",
            backing = backing,
            key = -48)
        
        # let's connect it on boot...
        vdci = VirtualDeviceConnectInfo(self.vim, allowGuestControl=True, connected=True, startConnected=True)
        nic.connectable = vdci
        
        nicSpec = VirtualDeviceConfigSpec(self.vim,
            operation = VirtualDeviceConfigSpecOperation.add,
            device = nic)
        delattr(nicSpec, 'fileOperation')
            
        return nicSpec
        
        
    def _getDefaultDevices(self, compute_resource, host):
        log.info("Getting default devices...")
        browser = compute_resource.environmentBrowser

        conf_opt = browser.QueryConfigOption(key=None, host=host)
        default_devs = conf_opt.defaultDevice
        return default_devs

    def _getConfigTargetForHost(self, compute_resource, host):
        log.info("Getting target for host...")
        browser = compute_resource.environmentBrowser
        configTarget = browser.QueryConfigTarget(host)
        return configTarget

if __name__ == '__main__':
    app = VMCreate()
    app.create()
    
    
    
    
    
    
    
    