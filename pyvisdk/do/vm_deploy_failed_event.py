
from pyvisdk.do.vm_event import VmEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmDeployFailedEvent(VmEvent):
    '''This event records a failure to deploy from a template.
    '''
    
    def __init__(self, destDatastore, reason):
        # MUST define these
        super(VmDeployFailedEvent, self).__init__()
    
        self.data['destDatastore'] = destDatastore
        self.data['reason'] = reason
    
    
    @property
    def destDatastore(self):
        '''The destination datastore the template is being deployed to.
        '''
        return self.data['destDatastore']

    @property
    def reason(self):
        '''The reason for the failure.
        '''
        return self.data['reason']

