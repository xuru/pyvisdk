
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmRenamedEvent(VmEvent):
    '''This event records the renaming of a virtual machine.
    '''
    
    def __init__(self, newName, oldName):
        # MUST define these
        super(VmRenamedEvent, self).__init__()
    
        self.data['newName'] = newName
        self.data['oldName'] = oldName
    
    
    @property
    def newName(self):
        '''The new name of the virtual machine.
        '''
        return self.data['newName']

    @property
    def oldName(self):
        '''The old name of the virtual machine.
        '''
        return self.data['oldName']

