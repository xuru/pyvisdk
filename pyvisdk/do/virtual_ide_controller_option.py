
from pyvisdk.do.virtual_controller_option import VirtualControllerOption
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualIDEControllerOption(VirtualControllerOption):
    '''The VirtualIDEControllerOption data object type contains the options for a virtual
        IDE controller.
    '''
    
    def __init__(self, numIDECdroms, numIDEDisks):
        # MUST define these
        super(VirtualIDEControllerOption, self).__init__()
    
        self.data['numIDECdroms'] = numIDECdroms
        self.data['numIDEDisks'] = numIDEDisks
    
    
    @property
    def numIDECdroms(self):
        '''The minimum, maximum, and default number of IDE VirtualCdrom instances you can
        have, at any given time, in the IDE controller. The number is further
        constrained by the number of available slots in the virtual IDE
        controller.
        '''
        return self.data['numIDECdroms']

    @property
    def numIDEDisks(self):
        '''The minimum, maximum, and default number of IDE VirtualDisk instances you can
        have, at any given time, in the IDE controller. The number is further
        constrained by the number of available slots in the virtual IDE
        controller.
        '''
        return self.data['numIDEDisks']

