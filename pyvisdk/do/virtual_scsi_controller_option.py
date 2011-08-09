
from pyvisdk.do.virtual_controller_option import VirtualControllerOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualSCSIControllerOption(VirtualControllerOption):
    '''The VirtualSCSIControllerOption data object type contains the options for a
        virtual SCSI controller defined by the VirtualSCSIController data object
        type.
    '''
    
    def __init__(self, defaultSharedIndex, hotAddRemove, numSCSICdroms, numSCSIDisks, numSCSIPassthrough, scsiCtlrUnitNumber, sharing):
        # MUST define these
        super(VirtualSCSIControllerOption, self).__init__()
    
        self.data['defaultSharedIndex'] = defaultSharedIndex
        self.data['hotAddRemove'] = hotAddRemove
        self.data['numSCSICdroms'] = numSCSICdroms
        self.data['numSCSIDisks'] = numSCSIDisks
        self.data['numSCSIPassthrough'] = numSCSIPassthrough
        self.data['scsiCtlrUnitNumber'] = scsiCtlrUnitNumber
        self.data['sharing'] = sharing
    
    
    @property
    def defaultSharedIndex(self):
        '''Index into sharing array specifying the default value.
        '''
        return self.data['defaultSharedIndex']

    @property
    def hotAddRemove(self):
        '''This object determines if hot adding and removing of devices is supported. Hot
        adding and removing of devices enables users to add or remove a SCSI disk
        without having to shut down the virtual machine. If the feature is
        supported, you can designate a default value. Two properties accomplish
        this: *
        '''
        return self.data['hotAddRemove']

    @property
    def numSCSICdroms(self):
        '''Three properties (numSCSICdroms.min, numSCSICdroms.max, and
        numSCSICdroms.defaultValue) define the minimum, maximum, and default
        number of SCSI VirtualCdrom instances available in the SCSI controller.
        The number of SCSI VirtualCdrom instances is also limited by the number of
        available slots in the SCSI controller.
        '''
        return self.data['numSCSICdroms']

    @property
    def numSCSIDisks(self):
        '''Three properties (numSCSIDisks.min, numSCSIDisks.max, and
        numSCSIDisks.defaultValue) define the minimum, maximum, and default number
        of SCSI VirtualDisk instances available at any given time in the SCSI
        controller. The number of SCSI VirtualDisk instances is also limited by
        the number of available slots in the SCSI controller.
        '''
        return self.data['numSCSIDisks']

    @property
    def numSCSIPassthrough(self):
        '''Three properties (numSCSIPassthrough.min, numSCSIPassthrough.max, and
        numSCSIPassthrough.defaultValue) define the minimum, maximum, and default
        number of VirtualSCSIPassthrough instances available have at any given
        time in the SCSI controller. The number of VirtualSCSIPassthrough
        instances is also limited by the number of available slots in the SCSI
        controller.
        '''
        return self.data['numSCSIPassthrough']

    @property
    def scsiCtlrUnitNumber(self):
        '''The unit number of the SCSI controller. The SCSI controller sits on its own bus,
        so that this field defines which slot the controller will use.
        '''
        return self.data['scsiCtlrUnitNumber']

    @property
    def sharing(self):
        '''Supported shared bus modes.
        '''
        return self.data['sharing']

