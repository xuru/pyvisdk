'''
Created on Feb 17, 2011

@author: eplaster
'''
from pyvisdk import consts
from pyvisdk.consts import ManagedObjectReference, TaskInfoState
from pyvisdk.core import VisdkInvalidState
from random import randrange
from suds import WebFault
from datetime import datetime
import logging
import string

log = logging.getLogger(__name__)
log.setLevel(logging.DEBUG)

class VisdkTaskError(Exception):
    pass

class VisdkError(Exception):
    pass

class ManagedEntity(object):
    def __init__(self, core, props, name=None, ref=None):
        self.core = core
        self.client = core.client
        self.service = core.client.service
        self.type = consts.ManagedEntity
        self.props = ["configIssue", "configStatus", "name", "parent"] + props
        if ref:
            self.ref = ManagedObjectReference(consts.ManagedEntity, ref.value)
        self.name = name
        
        self.parent = None
        self.issues = None
        self.status = None
        
    def parse(self):
        for prop in self.props:
            data = self.core.getDynamicProperty(self.ref, prop)
            self.update(data)
        
    def update(self, propset):
        log.debug("*********** base update **************")
        for name, value in propset.items():
            try:
                if name == "name":
                    log.debug("[%s] %s" % (name, value.__class__.__name__))
                    self.name = value
            
                elif name == "parent":
                    log.debug("[%s] %s" % (name, value.__class__.__name__))
                    self.parent = value
            
                elif name == "configIssue":
                    log.debug("[%s] %s" % (name, value.__class__.__name__))
                    self.issues = value
            
                elif name == "configStatus":
                    log.debug("[%s] %s" % (name, value.__class__.__name__))
                    self.status = value
            except AttributeError, e:
                log.warning("[WARNING] [%s] %s" %  (name, e))
       
            
class VirtualMachine(ManagedEntity):
    def __init__(self, core, name=None, ref=None):
        props = [ "parent","capability", "summary.config", "snapshot", "runtime", "config.hardware.device"] 
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
    
    def parse(self):
        for prop in self.props:
            changeData = self.core.getDynamicProperty(self.ref, prop)
            self.update(changeData)

    def update(self, prop):
        super(VirtualMachine, self).update(prop)
        
        log.debug("*********** %s update **************" % self.__class__.__name__)
        for name, value in prop.items():
            if name == "config.hardware.device":
                for device in value:
                    name = device.__class__.__name__
                    if name == "VirtualDisk":
                        self.disks.append(VirtualDisk(self.core, device))
                        continue
                        
                    if not self.devices.has_key(name):
                        self.devices[name] = []
                    self.devices[name].append(device)
                
            elif name == "config":
                self.config = value
                
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
        self.sync(['snapshot'])
        return self.snapshots[name]
                
    def hasSnapshots(self):
        return len(self.snapshots.keys()) > 0
    
    def getSnapshotByName(self, name):
        if self.snapshots.has_key(name):
            return self.snapshots[name]
    
    def getSnapshots(self):
        return self.snapshots.values()
        
    def removeSnapshotByName(self, name):
        self.removeSnapshot(self.snapshots[name])
        
    def removeSnapshot(self, obj):
        ref = ManagedObjectReference(consts.VirtualMachineSnapshot, obj.snapshot.value)
        rv = self.service.RemoveSnapshot_Task(ref, False)
        self.core.waitForTask(rv)
        self.sync(['snapshot'])
        
    def removeAllSnapshots(self):
        rv = self.service.RemoveAllSnapshots_Task(self.ref)
        self.core.waitForTask(rv)
        self.sync(['snapshot'])
    
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
            self.sync(["config"])
        
    def powerOn(self):
        rv = self.service.PowerOnVM_Task(self.ref)
        status = self.core.waitForTask(rv)
        if status == TaskInfoState.error:
            raise VisdkTaskError("Unable to power on the virtual machine: " + self.name)
        log.debug("successfully powered on the virtual machine: " + self.name)
        self.sync(['runtime'])
    
    def powerOff(self):
        rv = self.service.PowerOffVM_Task(self.ref)
        status = self.core.waitForTask(rv)
        if status == TaskInfoState.error:
            raise VisdkTaskError("Unable to power off the virtual machine: " + self.name)
        log.debug("successfully powered off the virtual machine: " + self.name)
        self.sync(['runtime'])
    
    def reset(self):
        rv = self.service.ResetVM_Task(self.ref)
        status = self.core.waitForTask(rv)
        if status == TaskInfoState.error:
            raise VisdkTaskError("Unable to reset the virtual machine: " + self.name)
        log.debug("successfully reset the virtual machine: " + self.name)
        self.sync(['runtime'])
    
    def suspend(self):
        rv = self.service.SuspendVM_Task(self.ref)
        status = self.core.waitForTask(rv)
        if status == TaskInfoState.error:
            raise VisdkTaskError("Unable to suspend the virtual machine: " + self.name)
        log.debug("successfully suspended the virtual machine: " + self.name)
        self.sync(['runtime'])
    
    def reboot(self):
        try:
            self.service.RebootGuest(self.ref)
        except WebFault, e:
            raise VisdkTaskError("Unable to reboot the virtual machine: " + self.name, e)
        log.debug("successfully rebooted the virtual machine: " + self.name)
        self.sync(['runtime'])
    
    def shutdown(self):
        try:
            self.service.ShutdownGuest(self.ref)
        except WebFault, e:
            raise VisdkTaskError("Unable to shutdown the virtual machine: " + self.name, e)
        log.debug("successfully shutdown the virtual machine: " + self.name)
        self.sync(['runtime'])
    
    def standby(self):
        try:
            self.service.StandbyGuest(self.ref)
        except WebFault, e:
            raise VisdkTaskError("Unable to standby the virtual machine: " + self.name, e)
        log.debug("successfully standby the virtual machine: " + self.name)
        self.sync(['runtime'])
    
    
    """ Factory Objects """
    def VirtualMachineConfigSpec(self):
        spec = self.client.factory.create('ns0:VirtualMachineConfigSpec')
        return spec

    def _appendSnapshot(self, snap):
        """ Internal: recursive method to add a snapshot MO ref from a VirtualMachineSnapshotTree """
        self.snapshots[snap.name] = snap
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
    def __init__(self, core, data):
        self.core = core
        self.update(data)
        
    def update(self, device):
        log.debug("*********** %s update **************" % self.__class__.__name__)
        """ only parse out the information that we need..."""
        self.name = device.deviceInfo.label
        self.backing = device.backing.__class__.__name__
        self.thin = device.backing.thinProvisioned
        self.uuid = device.backing.uuid
        self.filename = device.backing.fileName
        self.datastore = device.backing.datastore
        self.capacity = device.capacityInKB
            
    def __str__(self):
        capacity = (self.capacity/1024)/1024
        out = "<VirtualDisk> name: %s, %-0.2fGB filename: %s" % (self.name, capacity, self.filename)
        return out

class HostSystem(ManagedEntity):
    def __init__(self, core, name=None, ref=None):
            # MUST define these
        props = [ "name", "datastore"]
        super(HostSystem, self).__init__(core, props, name, ref)
        
        self.datastores = {}
        self.type = consts.HostSystem
        self.name = name
        if ref:
            self.ref = ManagedObjectReference(consts.HostSystem, ref.value)
        self.parse()
    
    def update(self, prop):
        super(HostSystem, self).update(prop)
        
        log.debug("*********** %s update **************" % self.__class__.__name__)
        for name, value in prop.items():
            if name == 'datastore':
                for dsmor in value:
                    ds = Datastore(self.core, ref=dsmor)
                    self.datastores[ds.name] = ds
        
    def parse(self):
        for prop in self.props:
            info = self.core.getDynamicProperty(self.ref, prop)
            self.update(info)
    
    def __str__(self):
        return "<%s> %s" % (self.type, self.name)

class Datastore(ManagedEntity):
    def __init__(self, core, name=None, ref=None):
        # MUST define these
        props = [ "browser", "info", "summary", "capability"]
        super(Datastore, self).__init__(core, props, name, ref)
        
        self.type = consts.Datastore # type used to get to the virtual disks
        
        self.name = name
        self.ref = ref
        if ref:
            self.ref = ManagedObjectReference(consts.Datastore, ref.value)
        self.parse()
        
    def update(self, prop):
        super(Datastore, self).update(prop)
        
        log.debug("*********** %s update **************" % self.__class__.__name__)
        for name, value in prop.items():
            if name == 'info':
                log.debug("[%s] %s" % (name, value.__class__.__name__))
                # VmfsDatastoreInfo
                self.info = value
            
            elif name == 'summary':
                log.debug("[%s] %s" % (name, value.__class__.__name__))
                self.summary = value
            
            elif name == 'capability':
                log.debug("[%s] %s" % (name, value.__class__.__name__))
                self.capability = value
            
            elif name == 'browser':
                log.debug("[%s] %s" % (name, value.__class__.__name__))
                self.browser = value
            
    def parse(self):
        info = self.core.getDynamicProperty(self.ref, self.props)
        self.update(info)
        
    def __str__(self):
        return "<%s> %s" % (self.type, self.name)
