
from pyvisdk.do.vm_clone_event import VmCloneEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmCloneFailedEvent(VmCloneEvent):
    '''This event records a failure to clone a virtual machine.
    '''
    
    def __init__(self, destFolder, destHost, destName, reason):
        # MUST define these
        super(VmCloneFailedEvent, self).__init__()
    
        self.data['destFolder'] = destFolder
        self.data['destHost'] = destHost
        self.data['destName'] = destName
        self.data['reason'] = reason
    
    
    @property
    def destFolder(self):
        '''The destination folder to which the virtual machine is being cloned.
        '''
        return self.data['destFolder']

    @property
    def destHost(self):
        '''The destination host to which the virtual machine was being cloned.
        '''
        return self.data['destHost']

    @property
    def destName(self):
        '''The name of the destination virtual machine.
        '''
        return self.data['destName']

    @property
    def reason(self):
        '''The reason why this clone operation failed.
        '''
        return self.data['reason']

