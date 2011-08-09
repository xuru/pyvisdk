
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmAutoRenameEvent(VmEvent):
    '''This event records that a virtual machine was automatically renamed because of a
        name conflict.
    '''
    
    def __init__(self, newName, oldName):
        # MUST define these
        super(VmAutoRenameEvent, self).__init__()
    
        self.data['newName'] = newName
        self.data['oldName'] = oldName
    
    
    @property
    def newName(self):
        '''The name of the virtual machine after renaming.
        '''
        return self.data['newName']

    @property
    def oldName(self):
        '''The name of the virtual machine before renaming.
        '''
        return self.data['oldName']

