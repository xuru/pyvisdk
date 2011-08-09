
from pyvisdk.do.virtual_controller import VirtualController
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualSCSIController(VirtualController):
    '''The VirtualSCSIController data object type represents a SCSI controller in a
        virtual machine.
    '''
    
    def __init__(self, hotAddRemove, scsiCtlrUnitNumber, sharedBus):
        # MUST define these
        super(VirtualSCSIController, self).__init__()
    
        self.data['hotAddRemove'] = hotAddRemove
        self.data['scsiCtlrUnitNumber'] = scsiCtlrUnitNumber
        self.data['sharedBus'] = sharedBus
    
    
    @property
    def hotAddRemove(self):
        '''Setting this flag is optional. Setting this flag to true enables hot adding
        devices; setting this flag to false disables hot adding. This property
        determines if a SCSI disk may be added without shutting down the virtual
        machine. Using this flag depends on if this feature is supported, as
        designated by the setting of the boolean hotAddRemove.supported property
        in the VirtualSCSIControllerOption data object type. *
        '''
        return self.data['hotAddRemove']

    @property
    def scsiCtlrUnitNumber(self):
        '''The unit number of the SCSI controller. The SCSI controller sits on its own bus,
        so this field defines which slot the controller is using.
        '''
        return self.data['scsiCtlrUnitNumber']

    @property
    def sharedBus(self):
        '''Mode for sharing the SCSI bus. The modes are physicalSharing, virtualSharing, and
        noSharing. See the Sharing data object type for an explanation of these
        modes.
        '''
        return self.data['sharedBus']

