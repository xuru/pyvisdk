'''
Created on Feb 17, 2011

@author: eplaster
'''
from pyvisdk import consts
from pyvisdk.consts import ManagedObjectRef
from random import randrange
from types import StringType
import string
import types

class VisdkTaskError(Exception):
    pass

class VirtualMachine(object):
    def __init__(self, core, name=None, mo=None):
        # Parse the information retrieved from RetrieveProperties and organize it in a usefull way.
        self.core = core
        self.client = core.client
        self.service = core.client.service
        self.pathSet = [ "capability", "parent", "name", "summary.config", "snapshot", "config" ] 
        
        self.capability = None
        self.parent = None
        self.summary_config = None
        self.config = None
        self.name = name
        self.snapshots = {}
        
        self.version = ""
        self.ref = None
        self.devices = {}
        
        if mo:
            self.ref = mo
            self.update()
        else:
            self.initialize()
    
    def initialize(self):
        objectContent = self.core.getDecendentsByName(_type=consts.VirtualMachine, pathSet=self.pathSet, name=self.name)
        self.ref = ManagedObjectRef(consts.VirtualMachine, objectContent.obj.value)
            
        for prop in objectContent.propSet:
            self.updateProperty(prop)
            
    def update(self):
        propset, self.version = self.core.update(self.ref, self.pathSet, version=self.version)
        for prop in propset:
            print
            print "[%s] %s %s %s" % (prop.op, prop.name, prop.__class__.__name__, getattr(prop, 'val', "").__class__.__name__)
            print "="*80
            self.updateProperty(prop)

    def updateProperty(self, prop):
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
                print prop.val
                
            elif prop.name == "parent":
                self.parent = prop.val
                
            elif prop.name == "capability":
                print prop.val
                self.capability = prop.val
                
            elif prop.name == "snapshot":
                if prop.op == 'add':
                    print " -> Adding snapshot"
                    for snap in prop.val.rootSnapshotList:
                        self._appendSnapshot(snap)
                elif prop.op == 'assign':
                    print " -> Assigning snapshot"
                    self.snapshots = {}
                    if hasattr(prop, 'val'):
                        for snap in prop.val.rootSnapshotList:
                            self._appendSnapshot(snap)
                elif prop.op in ['remove', 'indirectRemove']:
                    print " -> Removing snapshot"
                    for snap in prop.val.rootSnapshotList:
                        if snap.name in self.snapshots.keys():
                            del self.snapshots[snap.name]
                
            elif prop.name == "summary.config":
                print prop.val
                self.summary_config = prop.val
        except AttributeError, e:
            print "[WARNING] %s" % e, prop.__class__.__name__
    
    def createSnapshot(self, name=None, description=None, memory_files=False, quisce_filesystem=True):
        if not name:
            name = self.name + "-" + "".join([string.digits[randrange(10)] for x in range(10)])
        rv = self.service.CreateSnapshot_Task(self.ref, name, description, memory_files, quisce_filesystem)
        self.core.waitForTask(rv)
        self.update()
                
    def removeSnapshotByName(self, name):
        self.removeSnapshot(self.snapshots[name])
        
    def removeSnapshot(self, obj):
        print obj
        mo = ManagedObjectRef(consts.VirtualMachineSnapshot, obj.snapshot.value)
        rv = self.service.RemoveSnapshot_Task(mo, False)
        self.core.waitForTask(rv)
        self.update()
        
    def removeAllSnapshots(self):
        rv = self.service.RemoveAllSnapshots_Task(self.ref)
        self.core.waitForTask(rv)
        self.update()
    
    def enableChangedBlockTracking(self, truth=True):
        spec = self.VirtualMachineConfigSpec()
        spec.changeTrackingEnabled = truth
        rv = self.service.ReconfigVM_Task(self.ref, spec)
        self.core.waitForTask(rv)
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
