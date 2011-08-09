
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostConfigInfo(DynamicData):
    '''This data object type encapsulates a typical set of host configuration information
        that is useful for displaying and configuring a host.VirtualCenter can
        retrieve this set of information very efficiently even for a large set of
        hosts.
    '''
    
    def __init__(self, activeDiagnosticPartition, adminDisabled, authenticationManagerInfo, autoStart, capabilities, consoleReservation, datastoreCapabilities, datastorePrincipal, dateTimeInfo, featureVersion, fileSystemVolume, firewall, flags, host, hyperThread, ipmi, localSwapDatastore, multipathState, network, offloadCapabilities, option, optionDef, pciPassthruInfo, powerSystemCapability, powerSystemInfo, product, service, sslThumbprintInfo, storageDevice, systemFile, systemResources, virtualMachineReservation, virtualNicManagerInfo, vmotion):
        # MUST define these
        super(HostConfigInfo, self).__init__()
    
        self.data['activeDiagnosticPartition'] = activeDiagnosticPartition
        self.data['adminDisabled'] = adminDisabled
        self.data['authenticationManagerInfo'] = authenticationManagerInfo
        self.data['autoStart'] = autoStart
        self.data['capabilities'] = capabilities
        self.data['consoleReservation'] = consoleReservation
        self.data['datastoreCapabilities'] = datastoreCapabilities
        self.data['datastorePrincipal'] = datastorePrincipal
        self.data['dateTimeInfo'] = dateTimeInfo
        self.data['featureVersion'] = featureVersion
        self.data['fileSystemVolume'] = fileSystemVolume
        self.data['firewall'] = firewall
        self.data['flags'] = flags
        self.data['host'] = host
        self.data['hyperThread'] = hyperThread
        self.data['ipmi'] = ipmi
        self.data['localSwapDatastore'] = localSwapDatastore
        self.data['multipathState'] = multipathState
        self.data['network'] = network
        self.data['offloadCapabilities'] = offloadCapabilities
        self.data['option'] = option
        self.data['optionDef'] = optionDef
        self.data['pciPassthruInfo'] = pciPassthruInfo
        self.data['powerSystemCapability'] = powerSystemCapability
        self.data['powerSystemInfo'] = powerSystemInfo
        self.data['product'] = product
        self.data['service'] = service
        self.data['sslThumbprintInfo'] = sslThumbprintInfo
        self.data['storageDevice'] = storageDevice
        self.data['systemFile'] = systemFile
        self.data['systemResources'] = systemResources
        self.data['virtualMachineReservation'] = virtualMachineReservation
        self.data['virtualNicManagerInfo'] = virtualNicManagerInfo
        self.data['vmotion'] = vmotion
    
    
    @property
    def activeDiagnosticPartition(self):
        '''The diagnostic partition that will be set as the current diagnostic partition on
        the host.
        '''
        return self.data['activeDiagnosticPartition']

    @property
    def adminDisabled(self):
        '''If the flag is true, the permissions on the host have been modified such that it
        is only accessible through local console or an authorized centralized
        management application. This flag is affected by the EnterLockdownMode and
        ExitLockdownMode operations.
        '''
        return self.data['adminDisabled']

    @property
    def authenticationManagerInfo(self):
        '''Current authentication configuration.
        '''
        return self.data['authenticationManagerInfo']

    @property
    def autoStart(self):
        '''AutoStart configuration.
        '''
        return self.data['autoStart']

    @property
    def capabilities(self):
        '''Capability vector indicating the available network features.
        '''
        return self.data['capabilities']

    @property
    def consoleReservation(self):
        '''Memory configuration.
        '''
        return self.data['consoleReservation']

    @property
    def datastoreCapabilities(self):
        '''Capability vector indicating available datastore features.
        '''
        return self.data['datastoreCapabilities']

    @property
    def datastorePrincipal(self):
        '''Datastore principal user
        '''
        return self.data['datastorePrincipal']

    @property
    def dateTimeInfo(self):
        '''Date/Time related configuration
        '''
        return self.data['dateTimeInfo']

    @property
    def featureVersion(self):
        '''List of feature-specific version information. Each element refers to the version
        information for a specific feature.
        '''
        return self.data['featureVersion']

    @property
    def fileSystemVolume(self):
        '''Storage system file system volume information.
        '''
        return self.data['fileSystemVolume']

    @property
    def firewall(self):
        '''Firewall configuration.
        '''
        return self.data['firewall']

    @property
    def flags(self):
        '''Additional flags for a host.
        '''
        return self.data['flags']

    @property
    def host(self):
        '''A reference to a managed object on a host.
        '''
        return self.data['host']

    @property
    def hyperThread(self):
        '''If hyperthreading is supported, this is the CPU configuration for optimizing
        hyperthreading.
        '''
        return self.data['hyperThread']

    @property
    def ipmi(self):
        '''IPMI (Intelligent Platform Management Interface) info for the host.
        '''
        return self.data['ipmi']

    @property
    def localSwapDatastore(self):
        '''Datastore visible to this host that may be used to store virtual machine
        swapfiles, for virtual machines executing on this host. The value of this
        property is set or unset by invoking UpdateLocalSwapDatastore. The policy
        for using this datastore is determined by the compute resource
        configuration's vmSwapPlacement property in concert with each individual
        virtual machine configuration's swapPlacement property.
        '''
        return self.data['localSwapDatastore']

    @property
    def multipathState(self):
        '''Storage multipath state information.
        '''
        return self.data['multipathState']

    @property
    def network(self):
        '''Network system information.
        '''
        return self.data['network']

    @property
    def offloadCapabilities(self):
        '''capabilities to offload operations either to the host or to physical hardware when
        a virtual machine is transmitting on a network
        '''
        return self.data['offloadCapabilities']

    @property
    def option(self):
        '''Host configuration options as defined by the OptionValue data object type.
        '''
        return self.data['option']

    @property
    def optionDef(self):
        '''A list of supported options.
        '''
        return self.data['optionDef']

    @property
    def pciPassthruInfo(self):
        '''PCI passthrough information.
        '''
        return self.data['pciPassthruInfo']

    @property
    def powerSystemCapability(self):
        '''Host power management capability.
        '''
        return self.data['powerSystemCapability']

    @property
    def powerSystemInfo(self):
        '''Host power management information.
        '''
        return self.data['powerSystemInfo']

    @property
    def product(self):
        '''Information about a product.
        '''
        return self.data['product']

    @property
    def service(self):
        '''Host service configuration.
        '''
        return self.data['service']

    @property
    def sslThumbprintInfo(self):
        '''SSL Thumbprint info for hosts in the same cluster
        '''
        return self.data['sslThumbprintInfo']

    @property
    def storageDevice(self):
        '''Storage system information.
        '''
        return self.data['storageDevice']

    @property
    def systemFile(self):
        '''Datastore paths of files used by the host system on mounted volumes, for instance,
        the COS vmdk file of the host. For information on datastore paths, see
        Datastore.
        '''
        return self.data['systemFile']

    @property
    def systemResources(self):
        '''Reference for the system resource hierarchy, used for configuring the set of
        resources reserved to the system and unavailable to virtual machines.
        '''
        return self.data['systemResources']

    @property
    def virtualMachineReservation(self):
        '''Virtual machine memory configuration.
        '''
        return self.data['virtualMachineReservation']

    @property
    def virtualNicManagerInfo(self):
        '''VirtualNic manager information.
        '''
        return self.data['virtualNicManagerInfo']

    @property
    def vmotion(self):
        '''VMotion system information.
        '''
        return self.data['vmotion']

