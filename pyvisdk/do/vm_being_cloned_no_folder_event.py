
from pyvisdk.do.vm_clone_event import VmCloneEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmBeingClonedNoFolderEvent(VmCloneEvent):
    '''This event records a virtual machine being cloned.
    '''
    
    def __init__(self, destHost, destName):
        # MUST define these
        super(VmBeingClonedNoFolderEvent, self).__init__()
    
        self.data['destHost'] = destHost
        self.data['destName'] = destName
    
    
    @property
    def destHost(self):
        '''The destination host to which the virtual machine is being cloned.
        '''
        return self.data['destHost']

    @property
    def destName(self):
        '''The name of the destination virtual machine.
        '''
        return self.data['destName']

