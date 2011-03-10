'''
Created on Feb 17, 2011

@author: eplaster
'''
from datetime import datetime
from pyvisdk import consts
from pyvisdk.consts import ManagedObjectReference, TaskInfoState
from pyvisdk.core import VisdkInvalidState
from pyvisdk.mangagedObjects.managedentity import ManagedEntity
from pyvisdk.mangagedObjects.snapshot import VirtualMachineSnapshot
from random import randrange
from suds import WebFault
import logging
import string
import types

log = logging.getLogger(__name__)
log.setLevel(logging.INFO)

class VisdkTaskError(Exception):
    pass

class VisdkError(Exception):
    pass

class VisdkAttributes(object):
    pass
            
class VirtualMachine(ManagedEntity):
    def __init__(self, core, name=None, ref=None):
        props = [ "parent","capability", "config", "summary.config", "snapshot", "runtime"] 
        super(VirtualMachine, self).__init__(core, props, name, ref)
        
        # MUST define these
        self.type = consts.VirtualMachine
        
        # properties to get updated
        self.capability = None
        self.summary_config = None
        self.config = None
        self.snapshots = {}
        self.poweredOn = False
        
        self.version = ""
        self.devices = {}
        self.disks = []
        
        self.ref = ref
        if ref == None and name != None:
            ref = self.core.getDecendentsByName(consts.VirtualMachine, name=self.name).obj
            
        if ref:
            self.ref = ManagedObjectReference(consts.VirtualMachine, ref.value)
        else:
            raise VisdkError("Unable to get managed object reference for: [%s] %s" % (name, ref))
        self.parse()
    
    def parse(self, prop=None):
        if prop:
            changeData = self.core.getDynamicProperty(self.ref, prop)
            self.update(changeData)
        else:
            for prop in self.props:
                self.parse(prop)
        
    def update(self, prop):
        super(VirtualMachine, self).update(prop)
        
        for name, value in prop.items():
            log.debug("[%-20s] %s" % (name, value.__class__.__name__))
                
            if name == "config":
                self.config = value
                self.disks = []
                
                # setup the devices...
                for device in value.hardware.device:
                    log.debug("[%-20s] %s" % (name, device.__class__.__name__))
                    name = device.__class__.__name__
                    if name == "VirtualDisk":
                        self.disks.append(VirtualDisk(self, device))
                        continue
                        
                    if not self.devices.has_key(name):
                        self.devices[name] = []
                    self.devices[name].append(device)
               
            elif name == "capability":
                self.capability = value
                
            elif name == "snapshot":
                for snap in value.rootSnapshotList:
                    self._appendSnapshot(snap)
                
            elif name == "summary.config":
                self.summary_config = value
                
            elif name == "runtime":
                self.host = ManagedObjectReference(consts.HostSystem, value.host.value)
                self.poweredOn = (value.powerState == "poweredOn")

    def createSnapshot(self, name=None, description=None, memory_files=False, quisce_filesystem=True):
        if not name:
            name = self.name + "-" + "".join([string.digits[randrange(10)] for x in range(10)])
        if not description:
            description = "pyvisdk %s" % datetime.now().strftime('%d%b%Y')
            
        rv = self.service.CreateSnapshot_Task(self.ref, name, description, memory_files, quisce_filesystem)
        self.core.waitForTask(rv)
        
        # signal an update
        self.parse('snapshot')
                
    def hasSnapshots(self):
        return len(self.snapshots.keys()) > 0
    
    def getSnapshotByName(self, name):
        if self.snapshots.has_key(name):
            return self.snapshots[name]
    
    def getSnapshots(self):
        return self.snapshots.values()
        
    def removeSnapshotByName(self, name):
        self.removeSnapshot(self.snapshots[name])
        
    def removeSnapshot(self, snapshot):
        rv = self.service.RemoveSnapshot_Task(snapshot.ref, False)
        self.core.waitForTask(rv)
        self.parse('snapshot')
        
    def removeAllSnapshots(self):
        rv = self.service.RemoveAllSnapshots_Task(self.ref)
        self.core.waitForTask(rv)
        self.parse('snapshot')
    
    def enableChangedBlockTracking(self, truth=True):
        if self.capability.changeTrackingSupported:
            if self.config.changeTrackingEnabled:
                # log message
                return
            
            if self.poweredOn:
                raise VisdkInvalidState("Virtual machine must be powered off in order to enable CBT")
            
            spec = self.VirtualMachineConfigSpec()
            spec.changeTrackingEnabled = truth
            rv = self.service.ReconfigVM_Task(self.ref, spec)
            self.core.waitForTask(rv)
            self.parse("config")
            
            if self.config.changeTrackingEnabled != truth:
                self.enableChangedBlockTracking(truth)
        
    def powerOn(self):
        rv = self.service.PowerOnVM_Task(self.ref)
        status = self.core.waitForTask(rv)
        if status == TaskInfoState.error:
            raise VisdkTaskError("Unable to power on the virtual machine: " + self.name)
        log.debug("successfully powered on the virtual machine: " + self.name)
        self.parse('runtime')
    
    def powerOff(self):
        rv = self.service.PowerOffVM_Task(self.ref)
        status = self.core.waitForTask(rv)
        if status == TaskInfoState.error:
            raise VisdkTaskError("Unable to power off the virtual machine: " + self.name)
        log.debug("successfully powered off the virtual machine: " + self.name)
        self.parse('runtime')
    
    def reset(self):
        rv = self.service.ResetVM_Task(self.ref)
        status = self.core.waitForTask(rv)
        if status == TaskInfoState.error:
            raise VisdkTaskError("Unable to reset the virtual machine: " + self.name)
        log.debug("successfully reset the virtual machine: " + self.name)
        self.parse('runtime')
    
    def suspend(self):
        rv = self.service.SuspendVM_Task(self.ref)
        status = self.core.waitForTask(rv)
        if status == TaskInfoState.error:
            raise VisdkTaskError("Unable to suspend the virtual machine: " + self.name)
        log.debug("successfully suspended the virtual machine: " + self.name)
        self.parse('runtime')
    
    def reboot(self):
        try:
            self.service.RebootGuest(self.ref)
        except WebFault, e:
            raise VisdkTaskError("Unable to reboot the virtual machine: " + self.name, e)
        log.debug("successfully rebooted the virtual machine: " + self.name)
        self.parse('runtime')
    
    def shutdown(self):
        try:
            self.service.ShutdownGuest(self.ref)
        except WebFault, e:
            raise VisdkTaskError("Unable to shutdown the virtual machine: " + self.name, e)
        log.debug("successfully shutdown the virtual machine: " + self.name)
        self.parse('runtime')
    
    def standby(self):
        try:
            self.service.StandbyGuest(self.ref)
        except WebFault, e:
            raise VisdkTaskError("Unable to standby the virtual machine: " + self.name, e)
        log.debug("successfully standby the virtual machine: " + self.name)
        self.parse('runtime')
    
    
    """ Factory Objects """
    def VirtualMachineConfigSpec(self):
        spec = self.client.factory.create('ns0:VirtualMachineConfigSpec')
        return spec

    def _appendSnapshot(self, snap):
        """ Internal: recursive method to add a snapshot MO ref from a VirtualMachineSnapshotTree """
        self.snapshots[snap.name] = VirtualMachineSnapshot(self, ref=snap)
        if hasattr(snap, "childSnapshotList"):
            for x in snap.childSnapshotList:
                self._appendSnapshot(x)
        
    def __str__(self):
        out = "<%s> %d snapshots" % (self.name, len(self.snapshots.keys()))
        return out
    
class VirtualDisk(object):
    """
    VirtualDisk
    
    NOTE: This class is special in that it's not an managed object, but part of the VirtualMachine MOR
    """
    def __init__(self, vm, data):
        self.vm = vm
        self.core = vm.core
        self.update(data)
        
    def update(self, device):
        """ only parse out the information that we need..."""
        self.key = device.key
        self.name = device.deviceInfo.label
        self.backingType = device.backing.__class__.__name__
        self.backing = device.backing
        self.thin = device.backing.thinProvisioned
        self.uuid = device.backing.uuid
        self.filename = device.backing.fileName
        self.datastore = device.backing.datastore
        self.capacity = device.capacityInKB
        self.changeId = getattr(device.backing, 'changeId', '*')
            
    def queryChangedDiskAreas(self, snapshot, offset, changeID):
        if self.vm.config.changeTrackingEnabled:
            return self.core.client.QueryChangedDiskAreas(self.vm.ref, snapshot.ref, self.key, offset, changeID)
        else:
            raise VisdkError("Unable to query ChangedDiskArea when CBT is unsupported.  Please enable CBT to call this method.")

    def __str__(self):
        capacity = (self.capacity/1024)/1024
        out = "<VirtualDisk> name: %s, %-0.2fGB filename: %s" % (self.name, capacity, self.filename)
        return out

