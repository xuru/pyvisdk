
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineConfigSummary(DynamicData):
    '''A subset of virtual machine configuration.
    '''
    
    def __init__(self, annotation, cpuReservation, ftInfo, guestFullName, guestId, installBootRequired, instanceUuid, memoryReservation, memorySizeMB, name, numCpu, numEthernetCards, numVirtualDisks, product, template, uuid, vmPathName):
        # MUST define these
        super(VirtualMachineConfigSummary, self).__init__()
    
        self.data['annotation'] = annotation
        self.data['cpuReservation'] = cpuReservation
        self.data['ftInfo'] = ftInfo
        self.data['guestFullName'] = guestFullName
        self.data['guestId'] = guestId
        self.data['installBootRequired'] = installBootRequired
        self.data['instanceUuid'] = instanceUuid
        self.data['memoryReservation'] = memoryReservation
        self.data['memorySizeMB'] = memorySizeMB
        self.data['name'] = name
        self.data['numCpu'] = numCpu
        self.data['numEthernetCards'] = numEthernetCards
        self.data['numVirtualDisks'] = numVirtualDisks
        self.data['product'] = product
        self.data['template'] = template
        self.data['uuid'] = uuid
        self.data['vmPathName'] = vmPathName
    
    
    @property
    def annotation(self):
        '''Description for the virtual machine.
        '''
        return self.data['annotation']

    @property
    def cpuReservation(self):
        '''Configured CPU reservation in MHz
        '''
        return self.data['cpuReservation']

    @property
    def ftInfo(self):
        '''Fault Tolerance settings for this virtual machine. This property will be populated
        only for fault tolerance virtual machines and will be left unset for all
        other virtual machines. See FaultToleranceConfigInfo for a description.
        '''
        return self.data['ftInfo']

    @property
    def guestFullName(self):
        '''Guest operating system name configured on the virtual machine.
        '''
        return self.data['guestFullName']

    @property
    def guestId(self):
        '''Guest operating system identifier (short name).
        '''
        return self.data['guestId']

    @property
    def installBootRequired(self):
        '''Whether the VM requires a reboot to finish installation. False if no vApp meta-
        data is configured.
        '''
        return self.data['installBootRequired']

    @property
    def instanceUuid(self):
        '''VC-specific identifier of the virtual machine
        '''
        return self.data['instanceUuid']

    @property
    def memoryReservation(self):
        '''Configured Memory reservation in MB
        '''
        return self.data['memoryReservation']

    @property
    def memorySizeMB(self):
        '''Memory size of the virtual machine, in megabytes.
        '''
        return self.data['memorySizeMB']

    @property
    def name(self):
        '''Name of the virtual machine.
        '''
        return self.data['name']

    @property
    def numCpu(self):
        '''Number of processors in the virtual machine.
        '''
        return self.data['numCpu']

    @property
    def numEthernetCards(self):
        '''Number of virtual network adapters.
        '''
        return self.data['numEthernetCards']

    @property
    def numVirtualDisks(self):
        '''Number of virtual disks attached to the virtual machine.
        '''
        return self.data['numVirtualDisks']

    @property
    def product(self):
        '''Product information. References to properties in the URLs are expanded.
        '''
        return self.data['product']

    @property
    def template(self):
        '''Flag to determine whether or not this virtual machine is a template.
        '''
        return self.data['template']

    @property
    def uuid(self):
        '''Virtual machine BIOS identification.
        '''
        return self.data['uuid']

    @property
    def vmPathName(self):
        '''Path name to the configuration file for the virtual machine
        '''
        return self.data['vmPathName']

