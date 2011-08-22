
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.profile import Profile
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostProfile(Profile):
    '''This data object type represents a profile for configuring the host.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostProfile):
        super(HostProfile, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def referenceHost(self):
        '''Reference host in use for this HostProfile'''
        return self.update('referenceHost')
    
    
    
    def ExecuteHostProfile(self):
        '''Execute the Profile Engine to calculate the list of configuration changes
        needed for the host.
        :rtype: 
        :returns: 
        '''
        return self.delegate("ExecuteHostProfile")()
    
    def UpdateHostProfile(self):
        '''Update the HostProfile with the specified config.
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdateHostProfile")()
    
    def UpdateReferenceHost(self):
        '''Update the reference host in use by the HostProfile.
        :rtype: None
        :returns: 
        '''
        return self.delegate("UpdateReferenceHost")()