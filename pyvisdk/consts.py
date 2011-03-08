'''
Created on Feb 15, 2011

@author: eplaster
'''
import suds
import types

class ManagedObjectReference(suds.sudsobject.Property):
    """Custom class to replace the suds generated class, which lacks _type."""
    def __init__(self, _type, value):
        suds.sudsobject.Property.__init__(self, value)
        self._type = _type
        
# enums
class TaskInfoState(object):
    success = "success"
    running = "running"
    error = "error"
    queued = "queued"

serviceTypes = {
    'alarmManager'              : 'AlarmManager',
    'authorizationManager'      : 'AuthorizationManager',
    'clusterProfileManager'     : 'ClusterProfileManager',
    'complianceManager'         : 'ProfileComplianceManager',
    'customFieldsManager'       : 'CustomFieldsManager',
    'customizationSpecManager'  : 'CustomizationSpecManager',
    'diagnosticManager'         : 'DiagnosticManager',
    'dvSwitchManager'           : 'DistributedVirtualSwitchManager',
    'eventManager'              : 'EventManager',
    'extensionManager'          : 'ExtensionManager',
    'fileManager'               : 'FileManager',
    'hostProfileManager'        : 'HostProfileManager',
    'ipPoolManager'             : 'IpPoolManager',
    'licenseManager'            : 'LicenseManager',
    'localizationManager'       : 'LocalizationManager',
    'ovfManager'                : 'OvfManager',
    'perfManager'               : 'PerformanceManager',
    'propertyCollector'         : 'PropertyCollector',
    'rootFolder'                : 'Folder',
    'scheduledTaskManager'      : 'ScheduledTaskManager',
    'searchIndex'               : 'SearchIndex',
    'sessionManager'            : 'SessionManager',
    'setting'                   : 'OptionManager',
    'snmpSystem'                : 'HostSnmpSystem',
    'storageResourceManager'    : 'StorageResourceManager',
    'taskManager'               : 'TaskManager',
    'userDirectory'             : 'UserDirectory',
    'viewManager'               : 'ViewManager',
    'virtualDiskManager'        : 'VirtualDiskManager',
    'vmCompatibilityChecker'    : 'VirtualMachineCompatibilityChecker',
    'vmProvisioningChecker'     : 'VirtualMachineProvisioningChecker',
}
    
    
# managed entities
ManagedEntities = {
    "ManagedEntity": lambda x: ManagedObjectReference("ManagedEntity", x),
    "ComputeResource": lambda x: ManagedObjectReference("ComputeResource", x),
    "ClusterComputeResource": lambda x: ManagedObjectReference("ClusterComputeResource", x),
    "Datacenter": lambda x: ManagedObjectReference("Datacenter", x),
    "Folder": lambda x: ManagedObjectReference("Folder", x),
    "HostSystem": lambda x: ManagedObjectReference("HostSystem", x),
    "ResourcePool": lambda x: ManagedObjectReference("ResourcePool", x),
    "VirtualMachine": lambda x: ManagedObjectReference("VirtualMachine", x),
    "VirtualMachineSnapshot": lambda x: ManagedObjectReference("VirtualMachineSnapshot", x),
    "Datastore": lambda x: ManagedObjectReference("Datastore", x),
}

ManagedEntity = "ManagedEntity"
ComputeResource = "ComputeResource"
ClusterComputeResource = "ClusterComputeResource"
Datacenter = "Datacenter"
Folder = "Folder"
HostSystem = "HostSystem"
ResourcePool = "ResourcePool"
VirtualMachine = "VirtualMachine"
VirtualMachineSnapshot = "VirtualMachineSnapshot"
Datastore = "Datastore"

# compute resources
ComputeResources = {
    "ComputeResource": lambda x: ManagedObjectReference("ComputeResource", x),
    "ClusterComputeResource": lambda x: ManagedObjectReference("ClusterComputeResource", x),
}

# Collectors
HistoryCollectors = {
    "HistoryCollector": lambda x: ManagedObjectReference("HistoryCollector", x),
    "EventHistoryCollector": lambda x: ManagedObjectReference("EventHistoryCollector", x),
    "TaskHistoryCollector": lambda x: ManagedObjectReference("TaskHistoryCollector", x),
}

ManagedEntityList = ManagedEntities.keys()
ComputeResourceList = ComputeResources.keys()
HistoryCollectorList = HistoryCollectors.keys()
