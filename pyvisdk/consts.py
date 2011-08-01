'''
Created on Feb 15, 2011

@author: eplaster
'''
from pyvisdk.utils import Enum        

TaskInfoState = Enum("success", "error", "running", "queued")
ComputeResourcesTypes = Enum("ComputeResource","ClusterComputeResource")
HistoryCollectorTypes = Enum("HistoryCollector", "EventHistoryCollector", "TaskHistoryCollector")

serviceTypes = Enum( **{
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
    
