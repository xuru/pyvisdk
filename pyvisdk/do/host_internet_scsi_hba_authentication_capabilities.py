
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostInternetScsiHbaAuthenticationCapabilities(DynamicData):
    '''The authentication capabilities for this host bus adapter.
    '''
    
    def __init__(self, chapAuthSettable, krb5AuthSettable, mutualChapSettable, spkmAuthSettable, srpAuthSettable, targetChapSettable, targetMutualChapSettable):
        # MUST define these
        super(HostInternetScsiHbaAuthenticationCapabilities, self).__init__()
    
        self.data['chapAuthSettable'] = chapAuthSettable
        self.data['krb5AuthSettable'] = krb5AuthSettable
        self.data['mutualChapSettable'] = mutualChapSettable
        self.data['spkmAuthSettable'] = spkmAuthSettable
        self.data['srpAuthSettable'] = srpAuthSettable
        self.data['targetChapSettable'] = targetChapSettable
        self.data['targetMutualChapSettable'] = targetMutualChapSettable
    
    
    @property
    def chapAuthSettable(self):
        '''True if this host bus adapter supports changing the configuration state of CHAP
        authentication. CHAP is mandatory, however some adapter may not allow
        disabling this authentication method.
        '''
        return self.data['chapAuthSettable']

    @property
    def krb5AuthSettable(self):
        '''Always false in this version of the API.
        '''
        return self.data['krb5AuthSettable']

    @property
    def mutualChapSettable(self):
        '''When chapAuthSettable is TRUE, this describes if Mutual CHAP configuration is
        allowed as well.
        '''
        return self.data['mutualChapSettable']

    @property
    def spkmAuthSettable(self):
        '''Always false in this version of the API.
        '''
        return self.data['spkmAuthSettable']

    @property
    def srpAuthSettable(self):
        '''Always false in this version of the API.
        '''
        return self.data['srpAuthSettable']

    @property
    def targetChapSettable(self):
        '''When targetChapSettable is TRUE, this describes if CHAP configuration is allowed
        on targets associated with the adapter.
        '''
        return self.data['targetChapSettable']

    @property
    def targetMutualChapSettable(self):
        '''When targetMutualChapSettable is TRUE, this describes if Mutual CHAP configuration
        is allowed on targets associated with the adapter.
        '''
        return self.data['targetMutualChapSettable']

