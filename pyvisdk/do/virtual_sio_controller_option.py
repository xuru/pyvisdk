
from pyvisdk.do.virtual_controller_option import VirtualControllerOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualSIOControllerOption(VirtualControllerOption):
    '''The VirtualSIOControllerOption data object type contains the options for a virtual
        Super IO Controller.
    '''
    
    def __init__(self, numFloppyDrives, numParallelPorts, numSerialPorts):
        # MUST define these
        super(VirtualSIOControllerOption, self).__init__()
    
        self.data['numFloppyDrives'] = numFloppyDrives
        self.data['numParallelPorts'] = numParallelPorts
        self.data['numSerialPorts'] = numSerialPorts
    
    
    @property
    def numFloppyDrives(self):
        '''Three properties (numFloppyDrives.min, numFloppyDrives.max, and
        numFloppyDrives.defaultValue) define the minimum, maximum, and default
        number of floppy drives you can have at any given time in the Super IO
        Controller. This is further constrained by the number of available slots
        in the Super IO Controller.
        '''
        return self.data['numFloppyDrives']

    @property
    def numParallelPorts(self):
        '''Three properties (numParallelPorts.min, numParallelPorts.max, and
        numParallelPorts.defaultValue) define the minimum, maximum, and default
        number of parallel ports you can have at any given time in the Super IO
        controller. This is further constrained by the number of available slots
        in the Super IO Controller.
        '''
        return self.data['numParallelPorts']

    @property
    def numSerialPorts(self):
        '''Three properties (numSerialPorts.min, numSerialPorts.max, and
        numSerialPorts.defaultValue) define the minimum, maximum, and default
        number of serial ports you can have at any given time in the Super IO
        Controller. This is further constrained by the number of available slots
        in the Super IO Controller.
        '''
        return self.data['numSerialPorts']

