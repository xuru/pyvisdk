
from pyvisdk.do.host_event import HostEvent
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVnicConnectedToCustomizedDVPortEvent(HostEvent):
    '''This event records when some host vnics were reconfigured to use DVPorts with port
        level configuration, which might be different from the DVportgroup.
    '''
    
    def __init__(self, vnic):
        # MUST define these
        super(HostVnicConnectedToCustomizedDVPortEvent, self).__init__()
    
        self.data['vnic'] = vnic
    
    
    @property
    def vnic(self):
        '''Information about the vnic that is using the DVport.
        '''
        return self.data['vnic']

