
from pyvisdk.do.apply_profile import ApplyProfile
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PortGroupProfile(ApplyProfile):
    '''This data object type is a base class for the different kinds of port group
        profiles.
    '''
    
    def __init__(self, key, name, networkPolicy, vlan, vswitch):
        # MUST define these
        super(PortGroupProfile, self).__init__()
    
        self.data['key'] = key
        self.data['name'] = name
        self.data['networkPolicy'] = networkPolicy
        self.data['vlan'] = vlan
        self.data['vswitch'] = vswitch
    
    
    @property
    def key(self):
        '''The linkable identifier.
        '''
        return self.data['key']

    @property
    def name(self):
        '''The name of the portgroup.
        '''
        return self.data['name']

    @property
    def networkPolicy(self):
        '''The network policy applicable on the port group.
        '''
        return self.data['networkPolicy']

    @property
    def vlan(self):
        '''The vlan Id of the portGroup.
        '''
        return self.data['vlan']

    @property
    def vswitch(self):
        '''The virtual switch that the protgroup is connected to.
        '''
        return self.data['vswitch']

