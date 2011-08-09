
from pyvisdk.do.event import Event
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VmEvent(Event):
    '''These are virtual machine events.
    '''
    
    def __init__(self, template):
        # MUST define these
        super(VmEvent, self).__init__()
    
        self.data['template'] = template
    
    
    @property
    def template(self):
        '''Indicates whether or not the virtual machine is marked as a template.
        '''
        return self.data['template']

