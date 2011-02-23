'''
Created on Feb 17, 2011

@author: eplaster
'''
from pyvisdk import consts
from pyvisdk.consts import ManagedObjectRef, TaskInfoState
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

class VirtualMachine(object):
    def __init__(self, core, name=None, mo=None):
        # Parse the information retrieved from RetrieveProperties and organize it in a usefull way.
        self.core = core
        self.client = core.client
        self.service = core.client.service
        self.props = [ "parent", "capability", "name", "summary.config", "snapshot", "runtime", "config.hardware.device"] 
        
        self.capability = None
        self.parent = None
        self.summary_config = None
        self.config = None
        self.name = name
        self.snapshots = {}
        self.poweredOn = False
        
        self.version = ""
        self.ref = None
        self.devices = {}
        
        self.initialize()
    
    def initialize(self):
        log.debug("Initializing " + self.name)
        objectContent = self.core.getDecendentsByName(_type=consts.VirtualMachine, pathSet=self.props, name=self.name)
        self.ref = ManagedObjectRef(consts.VirtualMachine, objectContent.obj.value)
        self._updateProperties(objectContent.propSet)
            
    def update(self, props=[]):
        if not props:
            props = self.props
            
        propset, self.version = self.core.update(self.ref, self.props, version=self.version)
        self._updateProperties(propset)

    def _updateProperties(self, propset):
        for prop in propset:
            log.debug("[%s] %s %s %s" % (getattr(prop, "op", "  "), prop.name, prop.__class__.__name__, getattr(prop, 'val', "").__class__.__name__))
                      
            self._updateProperty(prop)
            
    def _updateProperty(self, prop):
        try:
            if prop.name == "config.hardware.device":
                for device in prop.val[0]:
                    name = device.__class__.__name__
                    if name == "VirtualDisk":
                        device = VirtualDisk(device)
                        
                    if not self.devices.has_key(name):
                        self.devices[name] = []
                    self.devices[name].append(device)
                
            elif prop.name == "name":
                self.name = prop.val
                
            elif prop.name == "config":
                self.config = prop.val
                
            elif prop.name == "parent":
                self.parent = prop.val
                
            elif prop.name == "capability":
                self.capability = prop.val
                
            elif prop.name == "snapshot":
                if prop.op == 'add':
                    for snap in prop.val.rootSnapshotList:
                        self._appendSnapshot(snap)
                elif prop.op == 'assign':
                    self.snapshots = {}
                    if hasattr(prop, 'val'):
                        for snap in prop.val.rootSnapshotList:
                            self._appendSnapshot(snap)
                elif prop.op in ['remove', 'indirectRemove']:
                    for snap in prop.val.rootSnapshotList:
                        if snap.name in self.snapshots.keys():
                            del self.snapshots[snap.name]
                
            elif prop.name == "summary.config":
                self.summary_config = prop.val
                
            elif prop.name == "runtime":
                self.host = ManagedObjectRef(consts.HostSystem, prop.val.host.value)
                self.poweredOn = (prop.val.powerState == "poweredOn")
                
            else:
                log.debug("unknown vm property: [%s] %s" % (prop.name, prop.val))
        except AttributeError, e:
            log.warning("[WARNING] [%s] %s" %  (prop.__class__.__name__, e))
    
    def createSnapshot(self, name=None, description=None, memory_files=False, quisce_filesystem=True):
        if not name:
            name = self.name + "-" + "".join([string.digits[randrange(10)] for x in range(10)])
        if not description:
            description = "pyvisdk %s" % datetime.now().strftime('%d%b%Y')
        rv = self.service.CreateSnapshot_Task(self.ref, name, description, memory_files, quisce_filesystem)
        self.core.waitForTask(rv)
        self.update()
        return self.snapshots[name]
                
    def getSnapshotByName(self, name):
        if self.snapshots.has_key(name):
            return self.snapshots[name]
        
    def removeSnapshotByName(self, name):
        self.removeSnapshot(self.snapshots[name])
        
    def removeSnapshot(self, obj):
        mo = ManagedObjectRef(consts.VirtualMachineSnapshot, obj.snapshot.value)
        rv = self.service.RemoveSnapshot_Task(mo, False)
        self.core.waitForTask(rv)
        self.update()
        
    def removeAllSnapshots(self):
        rv = self.service.RemoveAllSnapshots_Task(self.ref)
        self.core.waitForTask(rv)
        self.update()
    
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
            self.update(["config"])
        
    def powerOn(self):
        rv = self.service.PowerOnVM_Task(self.ref)
        status = self.core.waitForTask(rv)
        if status == TaskInfoState.error:
            raise VisdkTaskError("Unable to power on the virtual machine: " + self.name)
        log.debug("successfully powered on the virtual machine: " + self.name)
        self.update()
    
    def powerOff(self):
        rv = self.service.PowerOffVM_Task(self.ref)
        status = self.core.waitForTask(rv)
        if status == TaskInfoState.error:
            raise VisdkTaskError("Unable to power off the virtual machine: " + self.name)
        log.debug("successfully powered off the virtual machine: " + self.name)
        self.update()
    
    def reset(self):
        rv = self.service.ResetVM_Task(self.ref)
        status = self.core.waitForTask(rv)
        if status == TaskInfoState.error:
            raise VisdkTaskError("Unable to reset the virtual machine: " + self.name)
        log.debug("successfully reset the virtual machine: " + self.name)
        self.update()
    
    def suspend(self):
        rv = self.service.SuspendVM_Task(self.ref)
        status = self.core.waitForTask(rv)
        if status == TaskInfoState.error:
            raise VisdkTaskError("Unable to suspend the virtual machine: " + self.name)
        log.debug("successfully suspended the virtual machine: " + self.name)
        self.update()
    
    def reboot(self):
        try:
            self.service.RebootGuest(self.ref)
        except WebFault, e:
            raise VisdkTaskError("Unable to reboot the virtual machine: " + self.name, e)
        log.debug("successfully rebooted the virtual machine: " + self.name)
        self.update()
    
    def shutdown(self):
        try:
            self.service.ShutdownGuest(self.ref)
        except WebFault, e:
            raise VisdkTaskError("Unable to shutdown the virtual machine: " + self.name, e)
        log.debug("successfully shutdown the virtual machine: " + self.name)
        self.update()
    
    def standby(self):
        try:
            self.service.StandbyGuest(self.ref)
        except WebFault, e:
            raise VisdkTaskError("Unable to standby the virtual machine: " + self.name, e)
        log.debug("successfully standby the virtual machine: " + self.name)
        self.update()
    
    
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
    def __init__(self, obj):
        self.ref = object
        
        self.name = ""
        self.parse(obj)
    
    def parse(self, obj):
        """ only parse out the information that we need..."""
        self.name = obj.deviceInfo.label
        self.backing = obj.backing.__class__.__name__
        self.thin = obj.backing.thinProvisioned
        self.uuid = obj.backing.uuid
        self.filename = obj.backing.fileName
        self.datastore = obj.backing.datastore
        self.capacity = obj.capacityInKB
        
    def __str__(self):
        capacity = (self.capacity/1024)/1024
        out = "<VirtualDisk> name: %s, %-0.2fGB".format(self.name, capacity)
        return out
