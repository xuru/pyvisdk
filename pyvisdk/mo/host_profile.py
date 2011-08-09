
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.profile import Profile
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostProfile(Profile):
    '''This data object type represents a profile for configuring the host.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostProfile):
        # MUST define these
        super(HostProfile, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def referenceHost(self):
        '''Reference host in use for this HostProfile
        '''
        return self.update('referenceHost')


    def ExecuteHostProfile(self, host, deferredParam):
        '''Execute the Profile Engine to calculate the list of configuration changes needed
        for the host.

        :param host: to a HostSystemThe host on which to execute the profile. The host needn't be
        associated with the Profile.

        :param deferredParam: The inputs that the user has given till now. This should include all the inputs
        the user has given till now including the inputs from the previous round
        of the call.


        :rtype: ProfileExecuteResult 

        '''
        
        return self.delegate("ExecuteHostProfile")(host,deferredParam)
        

    def UpdateHostProfile(self, config):
        '''Update the HostProfile with the specified config.

        :param config: Specification which describes the changes.

        '''
        
        return self.delegate("UpdateHostProfile")(config)
        

    def UpdateReferenceHost(self, host):
        '''Update the reference host in use by the HostProfile.

        :param host: to a HostSystemReference host to use. If Unset, referenceHost is cleared.

        '''
        
        return self.delegate("UpdateReferenceHost")(host)
        
