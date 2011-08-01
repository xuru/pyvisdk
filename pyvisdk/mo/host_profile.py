
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
    
    

    def UpdateReferenceHost(self):
        '''Update the reference host in use by the HostProfile.
        '''
        
        return self.delegate("UpdateReferenceHost")()
        

    def ExecuteHostProfile(self):
        '''Execute the Profile Engine to calculate the list of configuration changes needed
        for the host.

        :rtype: ProfileExecuteResult 

        '''
        
        return self.delegate("ExecuteHostProfile")()
        

    def UpdateHostProfile(self, config):
        '''Update the HostProfile with the specified config.

        :param config: Specification which describes the changes.

        '''
        
        return self.delegate("UpdateHostProfile")(config)
        
