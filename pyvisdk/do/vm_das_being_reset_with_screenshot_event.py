
from pyvisdk.do.vm_das_being_reset_event import VmDasBeingResetEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmDasBeingResetWithScreenshotEvent(VmDasBeingResetEvent):
    '''This event records when a virtual machine is reset by HA VM Health Monitoring on
        hosts that support the create screenshot api
    '''
    
    def __init__(self, screenshotFilePath):
        # MUST define these
        super(VmDasBeingResetWithScreenshotEvent, self).__init__()
    
        self.data['screenshotFilePath'] = screenshotFilePath
    
    
    @property
    def screenshotFilePath(self):
        '''The datastore path of the screenshot taken before resetting.
        '''
        return self.data['screenshotFilePath']

