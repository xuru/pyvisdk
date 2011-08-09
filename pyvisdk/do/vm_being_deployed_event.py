
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmBeingDeployedEvent(VmEvent):
    '''This event records a virtual machine being deployed from a template.
    '''
    
    def __init__(self, srcTemplate):
        # MUST define these
        super(VmBeingDeployedEvent, self).__init__()
    
        self.data['srcTemplate'] = srcTemplate
    
    
    @property
    def srcTemplate(self):
        '''The template object from which the virtual machine is being deployed.
        '''
        return self.data['srcTemplate']

