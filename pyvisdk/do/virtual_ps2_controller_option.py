
from pyvisdk.do.virtual_controller_option import VirtualControllerOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualPS2ControllerOption(VirtualControllerOption):
    '''The VirtualPS2ControllerOption data object type contains the options for a virtual
        PS/2 controller for keyboards and mice. In addition to the options defined
        in the VirtualControllerOption data object type, these options include the
        number of keyboards and mice.
    '''
    
    def __init__(self, numKeyboards, numPointingDevices):
        # MUST define these
        super(VirtualPS2ControllerOption, self).__init__()
    
        self.data['numKeyboards'] = numKeyboards
        self.data['numPointingDevices'] = numPointingDevices
    
    
    @property
    def numKeyboards(self):
        '''The minimum, maximum, and default number of keyboards you can have at any given
        time. This is further constrained by the number of available slots in the
        PS/2 controller. The minimum, maximum, and default are integers defined by
        three properties: *
        '''
        return self.data['numKeyboards']

    @property
    def numPointingDevices(self):
        '''The minimum, maximum, and default number of mice you can have at any given time.
        The number of mice is also limited by the number of available slots in the
        PS/2 controller. The minimum, maximum, and default are integers defined by
        three properties: *
        '''
        return self.data['numPointingDevices']

