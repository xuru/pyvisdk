
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.profile import Profile
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostProfile(Profile):
    '''This data object type represents a profile for configuring the host.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.HostProfile):
        # MUST define these
        super(HostProfile, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def referenceHost(self):
        '''Reference host in use for this HostProfile
        '''
        return self.update('referenceHost')


    def ExecuteHostProfile(self, host):
        '''Execute the Profile Engine to calculate the list of configuration changes needed
        for the host.

        :param host: to a HostSystemReference host to use. If Unset, referenceHost is cleared.

        '''
        
        return self.delegate("ExecuteHostProfile")(host)
        

    def UpdateHostProfile(self, host):
        '''Update the HostProfile with the specified config.

        :param host: to a HostSystemReference host to use. If Unset, referenceHost is cleared.

        '''
        
        return self.delegate("UpdateHostProfile")(host)
        

    def UpdateReferenceHost(self, host):
        '''Update the reference host in use by the HostProfile.

        :param host: to a HostSystemReference host to use. If Unset, referenceHost is cleared.

        '''
        
        return self.delegate("UpdateReferenceHost")(host)
        
