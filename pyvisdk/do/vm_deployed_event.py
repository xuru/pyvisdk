
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmDeployedEvent(VmEvent):
    '''This event records the completion of a virtual machine deployment operation.
    '''
    
    def __init__(self, srcTemplate):
        # MUST define these
        super(VmDeployedEvent, self).__init__()
    
        self.data['srcTemplate'] = srcTemplate
    
    
    @property
    def srcTemplate(self):
        '''The template object from which the virtual machine has been deployed.
        '''
        return self.data['srcTemplate']

