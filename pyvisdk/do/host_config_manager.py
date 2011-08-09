
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostConfigManager(DynamicData):
    '''This data object type describes the configuration of a host across products and
        versions.
    '''
    
    def __init__(self, advancedOption, authenticationManager, autoStartManager, bootDeviceSystem, cpuScheduler, datastoreSystem, dateTimeSystem, diagnosticSystem, firewallSystem, firmwareSystem, healthStatusSystem, kernelModuleSystem, licenseManager, memoryManager, networkSystem, patchManager, pciPassthruSystem, powerSystem, serviceSystem, snmpSystem, storageSystem, virtualNicManager, vmotionSystem):
        # MUST define these
        super(HostConfigManager, self).__init__()
    
        self.data['advancedOption'] = advancedOption
        self.data['authenticationManager'] = authenticationManager
        self.data['autoStartManager'] = autoStartManager
        self.data['bootDeviceSystem'] = bootDeviceSystem
        self.data['cpuScheduler'] = cpuScheduler
        self.data['datastoreSystem'] = datastoreSystem
        self.data['dateTimeSystem'] = dateTimeSystem
        self.data['diagnosticSystem'] = diagnosticSystem
        self.data['firewallSystem'] = firewallSystem
        self.data['firmwareSystem'] = firmwareSystem
        self.data['healthStatusSystem'] = healthStatusSystem
        self.data['kernelModuleSystem'] = kernelModuleSystem
        self.data['licenseManager'] = licenseManager
        self.data['memoryManager'] = memoryManager
        self.data['networkSystem'] = networkSystem
        self.data['patchManager'] = patchManager
        self.data['pciPassthruSystem'] = pciPassthruSystem
        self.data['powerSystem'] = powerSystem
        self.data['serviceSystem'] = serviceSystem
        self.data['snmpSystem'] = snmpSystem
        self.data['storageSystem'] = storageSystem
        self.data['virtualNicManager'] = virtualNicManager
        self.data['vmotionSystem'] = vmotionSystem
    
    
    @property
    def advancedOption(self):
        '''Advanced options.
        '''
        return self.data['advancedOption']

    @property
    def authenticationManager(self):
        '''Authentication method configuration - for example, for Active Directory
        membership.
        '''
        return self.data['authenticationManager']

    @property
    def autoStartManager(self):
        '''Auto-start and auto-stop configuration.
        '''
        return self.data['autoStartManager']

    @property
    def bootDeviceSystem(self):
        '''Boot device order management.
        '''
        return self.data['bootDeviceSystem']

    @property
    def cpuScheduler(self):
        '''The CPU scheduler that determines which threads execute on a CPU at any given
        time.
        '''
        return self.data['cpuScheduler']

    @property
    def datastoreSystem(self):
        '''The datastore manager.
        '''
        return self.data['datastoreSystem']

    @property
    def dateTimeSystem(self):
        '''DateTime configuration
        '''
        return self.data['dateTimeSystem']

    @property
    def diagnosticSystem(self):
        '''The diagnostic for the ESX Server system.
        '''
        return self.data['diagnosticSystem']

    @property
    def firewallSystem(self):
        '''The firewall configuration.
        '''
        return self.data['firewallSystem']

    @property
    def firmwareSystem(self):
        '''Firmware management.
        '''
        return self.data['firmwareSystem']

    @property
    def healthStatusSystem(self):
        '''System health status manager.
        '''
        return self.data['healthStatusSystem']

    @property
    def kernelModuleSystem(self):
        '''Kernel module configuration management.
        '''
        return self.data['kernelModuleSystem']

    @property
    def licenseManager(self):
        '''License manager
        '''
        return self.data['licenseManager']

    @property
    def memoryManager(self):
        '''The memory manager on the host.
        '''
        return self.data['memoryManager']

    @property
    def networkSystem(self):
        '''The network system configuration.
        '''
        return self.data['networkSystem']

    @property
    def patchManager(self):
        '''Host patch management.
        '''
        return self.data['patchManager']

    @property
    def pciPassthruSystem(self):
        '''PciDeviceSystem for passthru.
        '''
        return self.data['pciPassthruSystem']

    @property
    def powerSystem(self):
        '''Power System manager.
        '''
        return self.data['powerSystem']

    @property
    def serviceSystem(self):
        '''The configuration of the host services (for example, SSH, FTP, and Telnet).
        '''
        return self.data['serviceSystem']

    @property
    def snmpSystem(self):
        '''Snmp configuration
        '''
        return self.data['snmpSystem']

    @property
    def storageSystem(self):
        '''The storage configuration.
        '''
        return self.data['storageSystem']

    @property
    def virtualNicManager(self):
        '''The VirtualNic configuration.
        '''
        return self.data['virtualNicManager']

    @property
    def vmotionSystem(self):
        '''The VMotion configuration.
        '''
        return self.data['vmotionSystem']

