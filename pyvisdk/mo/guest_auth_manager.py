
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class GuestAuthManager(BaseEntity):
    '''AuthManager is the managed object that provides APIs to manipulate the guest
    operating authentication.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.GuestAuthManager):
        super(GuestAuthManager, self).__init__(core, name=name, ref=ref, type=type)

    

    
    
    def AcquireCredentialsInGuest(self, vm, requestedAuth, sessionID=None):
        '''Authenticates in the guest and returns a GuestAuthentication object with the
        acquired credentials for use in subsequent guest operation calls.Authenticates
        in the guest and returns a GuestAuthentication object with the acquired
        credentials for use in subsequent guest operation calls.
        
        :param vm: MoRef of the VM to perform the operation on.
        
        :param requestedAuth: The guest authentication data used to acquire credentials. See GuestAuthentication.
        
        :param sessionID: The sessionID number should be provided only when responding to a server challenge. The sessionID number to be used with the challenge is found in the GuestAuthenticationChallenge object.
        
        '''
        return self.delegate("AcquireCredentialsInGuest")(vm, requestedAuth, sessionID)
    
    def ReleaseCredentialsInGuest(self, vm, auth):
        '''Releases session data and resources associated with a GuestAuthentication
        object returned by AcquireCredentialsInGuest.Releases session data and
        resources associated with a GuestAuthentication object returned by
        AcquireCredentialsInGuest.
        
        :param vm: MoRef of the VM to perform the operation on.
        
        :param auth: The guest authentication data. See GuestAuthentication.
        
        '''
        return self.delegate("ReleaseCredentialsInGuest")(vm, auth)
    
    def ValidateCredentialsInGuest(self, vm, auth):
        '''Validates the GuestAuthentication credentials.Validates the GuestAuthentication
        credentials.
        
        :param vm: MoRef of the VM to perform the operation on.
        
        :param auth: The guest authentication data. See GuestAuthentication.
        
        '''
        return self.delegate("ValidateCredentialsInGuest")(vm, auth)