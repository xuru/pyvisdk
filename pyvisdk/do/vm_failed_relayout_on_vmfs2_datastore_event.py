
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmFailedRelayoutOnVmfs2DatastoreEvent(VmEvent):
    '''This event records a failure to relay out a virtual machine when the virtual
        machine still has disks on a VMFS2 volume.
    '''
    
    def __init__(self, ):
        # MUST define these
        super(VmFailedRelayoutOnVmfs2DatastoreEvent, self).__init__()
    

    
    
