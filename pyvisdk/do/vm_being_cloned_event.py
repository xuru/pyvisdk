
from pyvisdk.do.vm_clone_event import VmCloneEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmBeingClonedEvent(VmCloneEvent):
    '''This event records a virtual machine being cloned.
    '''
    
    def __init__(self, destFolder, destHost, destName):
        # MUST define these
        super(VmBeingClonedEvent, self).__init__()
    
        self.data['destFolder'] = destFolder
        self.data['destHost'] = destHost
        self.data['destName'] = destName
    
    
    @property
    def destFolder(self):
        '''The destination folder to which the virtual machine is being cloned.
        '''
        return self.data['destFolder']

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

