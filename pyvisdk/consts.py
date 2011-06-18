'''
Created on Feb 15, 2011

@author: eplaster
'''
import collections

class Enum(collections.Mapping):
    """Enum is a subclass of :class:`collections.Mapping`, implementing comparison
    methods adhering to precedence rules."""
    
    def __init__(self, *argv, **kwargs):
        super(Enum, self).__init__(*argv, **kwargs)
        self.data = {}

    def labels(self, *args, **kwargs):
        for item in args:
            self.data[item] = item
        for n,v in kwargs.items():
            self.data[n] = v
        return self
        
    def compare(self, other, fun, default=False):
        return fun(self.precedence(self), self.precedence(other))

    def __gt__(self, other):
        return self.compare(other, lambda a, b: a < b, True)

    def __ge__(self, other):
        return self.compare(other, lambda a, b: a <= b, True)

    def __lt__(self, other):
        return self.compare(other, lambda a, b: a > b, False)

    def __le__(self, other):
        return self.compare(other, lambda a, b: a >= b, False)
    
    def __len__(self):
        return len([x for x in self.data.values() if x[0] != "_"])
    
    def __iter__(self):
        return iter(self.data)
    
    def __getitem__(self, item):
        return self.data[item]
    
    def __getattr__(self, item):
        return self.data[item]
    
    def precedence(self, item):
        """Get the precedence index for item.
    
        Lower index means higher precedence.
    
        """
        try:
            return self.PRECEDENCE.index(item)
        except ValueError:
            return self.PRECEDENCE.index(None)
        
TaskInfoState = Enum().labels("success", "error", "running", "queued")
ManagedEntityTypes = Enum().labels( "ManagedEntity", "ComputeResource", "ClusterComputeResource", "Datacenter", "Folder", 
        "HostSystem", "ResourcePool", "VirtualMachine", "VirtualMachineSnapshot", "Datastore")
ComputeResourcesTypes = Enum().labels("ComputeResource","ClusterComputeResource")
HistoryCollectorTypes = Enum().labels("HistoryCollector", "EventHistoryCollector", "TaskHistoryCollector")

serviceTypes = Enum().labels( **{
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
} )
    
