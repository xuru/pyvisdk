
from pyvisdk.do.apply_profile import ApplyProfile
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostApplyProfile(ApplyProfile):
    '''This DataObject has information about how a host should be configured.
    '''
    
    def __init__(self, authentication, datetime, firewall, memory, network, option, security, service, storage, userAccount, usergroupAccount):
        # MUST define these
        super(HostApplyProfile, self).__init__()
    
        self.data['authentication'] = authentication
        self.data['datetime'] = datetime
        self.data['firewall'] = firewall
        self.data['memory'] = memory
        self.data['network'] = network
        self.data['option'] = option
        self.data['security'] = security
        self.data['service'] = service
        self.data['storage'] = storage
        self.data['userAccount'] = userAccount
        self.data['usergroupAccount'] = usergroupAccount
    
    
    @property
    def authentication(self):
        '''Authentication Configuration
        '''
        return self.data['authentication']

    @property
    def datetime(self):
        '''Date and time configuration
        '''
        return self.data['datetime']

    @property
    def firewall(self):
        '''Firewall configuration
        '''
        return self.data['firewall']

    @property
    def memory(self):
        '''Memory configuration for the host. This may not be valid all versions of the host.
        '''
        return self.data['memory']

    @property
    def network(self):
        '''The network profile. If set, the network configuration on the host is overwritten
        with that specified in the networkProfile
        '''
        return self.data['network']

    @property
    def option(self):
        '''Set of profiles representing advanced config options.
        '''
        return self.data['option']

    @property
    def security(self):
        '''Security Configuration of the host. It can include configurations like
        administrator passwords and so on.
        '''
        return self.data['security']

    @property
    def service(self):
        '''Host configuration part which specifies the services
        '''
        return self.data['service']

    @property
    def storage(self):
        '''Storage part of the configuration.
        '''
        return self.data['storage']

    @property
    def userAccount(self):
        '''Set of userAccounts that need to be configured on the host
        '''
        return self.data['userAccount']

    @property
    def usergroupAccount(self):
        '''Set of UserGroups that need to be configured on the host
        '''
        return self.data['usergroupAccount']

