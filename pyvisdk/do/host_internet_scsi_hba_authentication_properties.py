
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostInternetScsiHbaAuthenticationProperties(DynamicData):
    '''The authentication settings for this host bus adapter or target.
    '''
    
    def __init__(self, chapAuthEnabled, chapAuthenticationType, chapInherited, chapName, chapSecret, mutualChapAuthenticationType, mutualChapInherited, mutualChapName, mutualChapSecret):
        # MUST define these
        super(HostInternetScsiHbaAuthenticationProperties, self).__init__()
    
        self.data['chapAuthEnabled'] = chapAuthEnabled
        self.data['chapAuthenticationType'] = chapAuthenticationType
        self.data['chapInherited'] = chapInherited
        self.data['chapName'] = chapName
        self.data['chapSecret'] = chapSecret
        self.data['mutualChapAuthenticationType'] = mutualChapAuthenticationType
        self.data['mutualChapInherited'] = mutualChapInherited
        self.data['mutualChapName'] = mutualChapName
        self.data['mutualChapSecret'] = mutualChapSecret
    
    
    @property
    def chapAuthEnabled(self):
        '''True if CHAP is currently enabled
        '''
        return self.data['chapAuthEnabled']

    @property
    def chapAuthenticationType(self):
        '''The preference for CHAP or non-CHAP protocol if CHAP is enabled
        '''
        return self.data['chapAuthenticationType']

    @property
    def chapInherited(self):
        '''CHAP settings are inherited
        '''
        return self.data['chapInherited']

    @property
    def chapName(self):
        '''The CHAP user name if enabled
        '''
        return self.data['chapName']

    @property
    def chapSecret(self):
        '''The CHAP secret if enabled
        '''
        return self.data['chapSecret']

    @property
    def mutualChapAuthenticationType(self):
        '''The preference for CHAP or non-CHAP protocol if CHAP is enabled
        '''
        return self.data['mutualChapAuthenticationType']

    @property
    def mutualChapInherited(self):
        '''Mutual-CHAP settings are inherited
        '''
        return self.data['mutualChapInherited']

    @property
    def mutualChapName(self):
        '''When Mutual-CHAP is enabled, the user name that target needs to use to
        authenticate with the initiator
        '''
        return self.data['mutualChapName']

    @property
    def mutualChapSecret(self):
        '''When Mutual-CHAP is enabled, the secret that target needs to use to authenticate
        with the initiator
        '''
        return self.data['mutualChapSecret']

