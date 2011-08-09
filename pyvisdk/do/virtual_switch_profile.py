
from pyvisdk.do.apply_profile import ApplyProfile
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualSwitchProfile(ApplyProfile):
    '''This data object type represents a profile for a virtual switch.
    '''
    
    def __init__(self, key, link, name, networkPolicy, numPorts):
        # MUST define these
        super(VirtualSwitchProfile, self).__init__()
    
        self.data['key'] = key
        self.data['link'] = link
        self.data['name'] = name
        self.data['networkPolicy'] = networkPolicy
        self.data['numPorts'] = numPorts
    
    
    @property
    def key(self):
        '''The linkable identifier.
        '''
        return self.data['key']

    @property
    def link(self):
        '''The links that are connected to the virtual switch.
        '''
        return self.data['link']

    @property
    def name(self):
        '''The name of the virtual switch.
        '''
        return self.data['name']

    @property
    def networkPolicy(self):
        '''The network policy applicable on the virtual switch.
        '''
        return self.data['networkPolicy']

    @property
    def numPorts(self):
        '''The number of ports on the virtual switch.
        '''
        return self.data['numPorts']

