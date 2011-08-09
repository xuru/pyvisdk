
from pyvisdk.do.virtual_controller_option import VirtualControllerOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualPCIControllerOption(VirtualControllerOption):
    '''This data object type contains the options for a virtual PCI Controller.
    '''
    
    def __init__(self, numEthernetCards, numParaVirtualSCSIControllers, numPCIPassthroughDevices, numSasSCSIControllers, numSCSIControllers, numSoundCards, numVideoCards, numVmciDevices, numVmiRoms, numVmxnet3EthernetCards):
        # MUST define these
        super(VirtualPCIControllerOption, self).__init__()
    
        self.data['numEthernetCards'] = numEthernetCards
        self.data['numParaVirtualSCSIControllers'] = numParaVirtualSCSIControllers
        self.data['numPCIPassthroughDevices'] = numPCIPassthroughDevices
        self.data['numSasSCSIControllers'] = numSasSCSIControllers
        self.data['numSCSIControllers'] = numSCSIControllers
        self.data['numSoundCards'] = numSoundCards
        self.data['numVideoCards'] = numVideoCards
        self.data['numVmciDevices'] = numVmciDevices
        self.data['numVmiRoms'] = numVmiRoms
        self.data['numVmxnet3EthernetCards'] = numVmxnet3EthernetCards
    
    
    @property
    def numEthernetCards(self):
        '''Defines the minimum, maximum, and default number of VirtualEthernetCard instances
        available, at any given time, in the PCI controller. The number of
        VirtualEthernetCard instances is also limited by the number of available
        slots in the PCI controller.
        '''
        return self.data['numEthernetCards']

    @property
    def numParaVirtualSCSIControllers(self):
        '''Defines the minimum, maximum, and default number of ParaVirtualScsiController
        instances available, at any given time, in the PCI controller. This is
        also limited by the number of available PCI Express slots in the PCI
        controller as well as the total number of supported SCSI controllers.
        '''
        return self.data['numParaVirtualSCSIControllers']

    @property
    def numPCIPassthroughDevices(self):
        '''Defines the minimum, maximum, and default number of VirtualPCIPassthrough
        instances available, at any given time, in the PCI controller. This is
        also limited by the number of available PCI Express slots in the PCI
        controller.
        '''
        return self.data['numPCIPassthroughDevices']

    @property
    def numSasSCSIControllers(self):
        '''Defines the minimum, maximum, and default number of VirtualLsiLogicSASController
        instances available, at any given time, in the PCI controller. This is
        also limited by the number of available PCI Express slots in the PCI
        controller as well as the total number of supported SCSI controllers.
        '''
        return self.data['numSasSCSIControllers']

    @property
    def numSCSIControllers(self):
        '''Defines the minimum, maximum, and default number of VirtualSCSIController
        instances available at any given time in the PCI controller. The number of
        VirtualSCSIController instances is also limited by the number of available
        slots in the PCI controller.
        '''
        return self.data['numSCSIControllers']

    @property
    def numSoundCards(self):
        '''Defines the minimum, maximum, and default number of VirtualSoundCard instances
        available, at any given time, in the PCI controller. The number of
        VirtualSoundCard instances is also limited by the number of available
        slots in the PCI controller.
        '''
        return self.data['numSoundCards']

    @property
    def numVideoCards(self):
        '''Defines the minimum, maximum, and default number of VirtualVideoCard instances
        available, at any given time, in the PCI controller. The number of
        VirtualVideoCard instances is also limited by the number of available
        slots in the PCI controller.
        '''
        return self.data['numVideoCards']

    @property
    def numVmciDevices(self):
        '''Defines the minimum, maximum, and default number of VirtualVMCIDevice instances
        available, at any given time, in the PCI controller. This is also limited
        by the number of available slots in the PCI controller.
        '''
        return self.data['numVmciDevices']

    @property
    def numVmiRoms(self):
        '''Defines the minimum, maximum, and default number of VirtualVMIROM instances
        available, at any given time, in the PCI controller. This is also limited
        by the number of available slots in the PCI controller.
        '''
        return self.data['numVmiRoms']

    @property
    def numVmxnet3EthernetCards(self):
        '''Defines the minimum, maximum, and default number of VirtualVmxnet3 ethernet card
        instances available, at any given time, in the PCI controller. This is
        also limited by the number of available PCI Express slots in the PCI
        controller as well as the total number of supported ethernet cards.
        '''
        return self.data['numVmxnet3EthernetCards']

