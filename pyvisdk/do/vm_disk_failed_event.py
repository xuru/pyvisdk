
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmDiskFailedEvent(VmEvent):
    '''This event records a failure to create a virtual disk in a virtual machine.
    '''
    
    def __init__(self, disk, reason):
        # MUST define these
        super(VmDiskFailedEvent, self).__init__()
    
        self.data['disk'] = disk
        self.data['reason'] = reason
    
    
    @property
    def disk(self):
        '''The name of the virtual disk.
        '''
        return self.data['disk']

    @property
    def reason(self):
        '''The reason for the failure.
        '''
        return self.data['reason']

