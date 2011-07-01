'''
Created on Feb 17, 2011

@author: eplaster
'''
from datetime import datetime
from pyvisdk.consts import ManagedEntityTypes
from pyvisdk.core import VisdkInvalidState
from pyvisdk.managedObjects.managedentity import ManagedEntity
from pyvisdk.managedObjects.snapshot import VirtualMachineSnapshot
from random import randrange
import logging
import string

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
        # MUST define these first
        self.type = ManagedEntityTypes.VirtualMachine
       
        props = [ "capability", "config", "datastore", "environmentBrowser", "guest", 
                 "guestHeartbeatStatus", "layout", "layoutEx", "network", "parentVApp", 
                 "resourceConfig", "resourcePool", "rootSnapshot", "runtime",
                 "snapshot", "storage", "summary"]
        
        methods = [
            "AcquireMksTicket", "AcquireTicket", "AnswerVM", "CheckCustomizationSpec", "CloneVM_Task", 
            "CreateScreenshot_Task", "CreateSecondaryVM_Task", "CreateSnapshot_Task", "CustomizeVM_Task", 
            "DefragmentAllDisks", "DisableSecondaryVM_Task", "EnableSecondaryVM_Task", "ExportVm", "ExtractOvfEnvironment", 
            "MakePrimaryVM_Task", "MarkAsTemplate", "MarkAsVirtualMachine", "MigrateVM_Task", "MountToolsInstaller", 
            "PowerOffVM_Task", "PowerOnVM_Task", "PromoteDisks_Task", "QueryChangedDiskAreas", "QueryFaultToleranceCompatibility", 
            "QueryUnownedFiles", "RebootGuest", "ReconfigVM_Task", "RefreshStorageInfo", "reloadVirtualMachineFromPath_Task", 
            "RelocateVM_Task", "RemoveAllSnapshots_Task", "ResetGuestInformation", "ResetVM_Task", "RevertToCurrentSnapshot_Task", 
            "SetDisplayTopology", "SetScreenResolution", "ShutdownGuest", "StandbyGuest", "StartRecording_Task", 
            "StartReplaying_Task", "StopRecording_Task", "StopReplaying_Task", "SuspendVM_Task", "TerminateFaultTolerantVM_Task", 
            "TurnOffFaultToleranceForVM_Task", "UnmountToolsInstaller", "UnregisterVM", "UpgradeTools_Task", "UpgradeVM_Task" ]
        
        super(VirtualMachine, self).__init__(core, methods, props, name, ref)
        self.snapshots = {}
        self._updateSnapshots()
        
        
    def createSnapshot(self, name=None, description=None, memory_files=False, quisce_filesystem=True):
        if not name:
            name = self.name + "-" + "".join([string.digits[randrange(10)] for _ in range(10)])
        if not description:
            description = "pyvisdk %s" % datetime.now().strftime('%d%b%Y')
            
        rv = self.service.CreateSnapshot_Task(self.ref, name, description, memory_files, quisce_filesystem)
        self.core.waitForTask(rv)
        
        self._updateSnapshots()
                
    def hasSnapshots(self):
        self._updateSnapshots()
        return self.snapshots != []
    
    def getSnapshotByName(self, name):
        self._updateSnapshots()
        if self.snapshots.has_key(name):
            return self.snapshots[name]
    
    def getSnapshots(self):
        self._updateSnapshots()
        return self.snapshots.values()
        
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
            self.update("config")
            
            if self.config.changeTrackingEnabled != truth:
                self.enableChangedBlockTracking(truth)
        
    
    # Factory Objects
    def VirtualMachineConfigSpec(self):
        spec = self.client.factory.create('ns0:VirtualMachineConfigSpec')
        return spec

    def _updateSnapshots(self):
        self.update('snapshot')
        if self.snapshot:
            for x in self.snapshot.rootSnapshotList:
                self._appendSnapshot(x)

    def _appendSnapshot(self, tree):
        """ Internal: recursive method to add a snapshot MO ref from a VirtualMachineSnapshotTree """
        self.snapshots[tree.name] = VirtualMachineSnapshot(self, ref=tree.snapshot)
        if hasattr(tree, "childSnapshotList"):
            for x in tree.childSnapshotList:
                self._appendSnapshot(x)
        
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

