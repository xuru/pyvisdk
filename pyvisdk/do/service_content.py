
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ServiceContent(DynamicData):
    '''The ServiceContent data object defines properties for the ServiceInstance managed
        object. The ServiceInstance itself does not have directly-accessible
        properties because reading the properties of a managed object requires the
        use of a property collector, and the property collector itself is a
        property of the ServiceInstance. For this reason, use the method
        RetrieveServiceContent to retrieve the ServiceContent object.
    '''
    
    def __init__(self, about, accountManager, alarmManager, authorizationManager, clusterProfileManager, complianceManager, customFieldsManager, customizationSpecManager, diagnosticManager, dvSwitchManager, eventManager, extensionManager, fileManager, hostProfileManager, ipPoolManager, licenseManager, localizationManager, ovfManager, perfManager, propertyCollector, rootFolder, scheduledTaskManager, searchIndex, sessionManager, setting, snmpSystem, storageResourceManager, taskManager, userDirectory, viewManager, virtualDiskManager, virtualizationManager, vmCompatibilityChecker, vmProvisioningChecker):
        # MUST define these
        super(ServiceContent, self).__init__()
    
        self.data['about'] = about
        self.data['accountManager'] = accountManager
        self.data['alarmManager'] = alarmManager
        self.data['authorizationManager'] = authorizationManager
        self.data['clusterProfileManager'] = clusterProfileManager
        self.data['complianceManager'] = complianceManager
        self.data['customFieldsManager'] = customFieldsManager
        self.data['customizationSpecManager'] = customizationSpecManager
        self.data['diagnosticManager'] = diagnosticManager
        self.data['dvSwitchManager'] = dvSwitchManager
        self.data['eventManager'] = eventManager
        self.data['extensionManager'] = extensionManager
        self.data['fileManager'] = fileManager
        self.data['hostProfileManager'] = hostProfileManager
        self.data['ipPoolManager'] = ipPoolManager
        self.data['licenseManager'] = licenseManager
        self.data['localizationManager'] = localizationManager
        self.data['ovfManager'] = ovfManager
        self.data['perfManager'] = perfManager
        self.data['propertyCollector'] = propertyCollector
        self.data['rootFolder'] = rootFolder
        self.data['scheduledTaskManager'] = scheduledTaskManager
        self.data['searchIndex'] = searchIndex
        self.data['sessionManager'] = sessionManager
        self.data['setting'] = setting
        self.data['snmpSystem'] = snmpSystem
        self.data['storageResourceManager'] = storageResourceManager
        self.data['taskManager'] = taskManager
        self.data['userDirectory'] = userDirectory
        self.data['viewManager'] = viewManager
        self.data['virtualDiskManager'] = virtualDiskManager
        self.data['virtualizationManager'] = virtualizationManager
        self.data['vmCompatibilityChecker'] = vmCompatibilityChecker
        self.data['vmProvisioningChecker'] = vmProvisioningChecker
    
    
    @property
    def about(self):
        '''Information about the service, such as the software version.
        '''
        return self.data['about']

    @property
    def accountManager(self):
        '''A singleton managed object that manages host local user and group accounts.
        '''
        return self.data['accountManager']

    @property
    def alarmManager(self):
        '''A singleton managed object that manages alarms.
        '''
        return self.data['alarmManager']

    @property
    def authorizationManager(self):
        '''Manages permissions for managed entities in the service.
        '''
        return self.data['authorizationManager']

    @property
    def clusterProfileManager(self):
        '''A singleton managed object that manages the cluster profiles.
        '''
        return self.data['clusterProfileManager']

    @property
    def complianceManager(self):
        '''A singleton managed object that manages compliance aspects of entities.
        '''
        return self.data['complianceManager']

    @property
    def customFieldsManager(self):
        '''A singleton managed object that managed custom fields.
        '''
        return self.data['customFieldsManager']

    @property
    def customizationSpecManager(self):
        '''A singleton managed object that manages saved guest customization specifications.
        '''
        return self.data['customizationSpecManager']

    @property
    def diagnosticManager(self):
        '''A singleton managed object that provides access to low-level log files.
        '''
        return self.data['diagnosticManager']

    @property
    def dvSwitchManager(self):
        '''A singleton managed object that provides relevant information of
        DistributedVirtualSwitch.
        '''
        return self.data['dvSwitchManager']

    @property
    def eventManager(self):
        '''A singleton managed object that manages events.
        '''
        return self.data['eventManager']

    @property
    def extensionManager(self):
        '''A singleton managed object that manages extensions.
        '''
        return self.data['extensionManager']

    @property
    def fileManager(self):
        '''A singleton managed object that allows management of files present on datastores.
        '''
        return self.data['fileManager']

    @property
    def hostProfileManager(self):
        '''A singleton managed object that manages the host profiles.
        '''
        return self.data['hostProfileManager']

    @property
    def ipPoolManager(self):
        '''A singleton managed object that supports management of IpPool objects. IP pools
        are used when allocating IPv4 and IPv6 addresses to vApps.
        '''
        return self.data['ipPoolManager']

    @property
    def licenseManager(self):
        '''A singleton managed object that manages licensing
        '''
        return self.data['licenseManager']

    @property
    def localizationManager(self):
        '''A singleton managed object that provides methods for retrieving message catalogs
        for client-side localization support.
        '''
        return self.data['localizationManager']

    @property
    def ovfManager(self):
        '''A singleton managed object that can generate OVF descriptors (export) and create
        vApps (single-VM or vApp container-based) from OVF descriptors (import).
        '''
        return self.data['ovfManager']

    @property
    def perfManager(self):
        '''A singleton managed object that manages the collection and reporting of
        performance statistics.
        '''
        return self.data['perfManager']

    @property
    def propertyCollector(self):
        '''Reference to a per-session object for retrieving properties and updates.
        '''
        return self.data['propertyCollector']

    @property
    def rootFolder(self):
        '''Reference to the top of the inventory managed by this service.
        '''
        return self.data['rootFolder']

    @property
    def scheduledTaskManager(self):
        '''A singleton managed object that manages scheduled tasks.
        '''
        return self.data['scheduledTaskManager']

    @property
    def searchIndex(self):
        '''A singleton managed object that allows search of the inventory
        '''
        return self.data['searchIndex']

    @property
    def sessionManager(self):
        '''Managed object for logging in and managing sessions.
        '''
        return self.data['sessionManager']

    @property
    def setting(self):
        '''Generic configuration for a management server. This is for example by vCenter to
        store the vCenter Settings. This is not used for a stand-alone host,
        instead the vim.host.ConfigManager.advancedOption is used.
        '''
        return self.data['setting']

    @property
    def snmpSystem(self):
        '''A singleton managed object that allows SNMP configuration. Not set if not
        supported on a particular platform.
        '''
        return self.data['snmpSystem']

    @property
    def storageResourceManager(self):
        '''A singleton managed object that provides methods for storage resource management.
        '''
        return self.data['storageResourceManager']

    @property
    def taskManager(self):
        '''A singleton managed object that manages tasks.
        '''
        return self.data['taskManager']

    @property
    def userDirectory(self):
        '''A user directory managed object.
        '''
        return self.data['userDirectory']

    @property
    def viewManager(self):
        '''A singleton managed object for tracking custom sets of objects.
        '''
        return self.data['viewManager']

    @property
    def virtualDiskManager(self):
        '''A singleton managed object that allows management of virtual disks on datastores.
        '''
        return self.data['virtualDiskManager']

    @property
    def virtualizationManager(self):
        '''A singleton managed object that manages the discovery, analysis, recommendation
        and virtualization of physical machines
        '''
        return self.data['virtualizationManager']

    @property
    def vmCompatibilityChecker(self):
        '''A singleton managed object that can answer questions about compatibility of a
        virtual machine with a host.
        '''
        return self.data['vmCompatibilityChecker']

    @property
    def vmProvisioningChecker(self):
        '''A singleton managed object that can answer questions about the feasibility of
        certain provisioning operations.
        '''
        return self.data['vmProvisioningChecker']

