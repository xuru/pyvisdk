
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostConfigSpec(DynamicData):
    '''The HostConfigSpec data object provides access to data objects that specify
        configuration changes to be applied to an ESX host.
    '''
    
    def __init__(self, activeDirectory, datastorePrincipal, datastorePrincipalPasswd, datetime, firewall, license, memory, nasDatastore, network, nicTypeSelection, option, security, service, storageDevice, userAccount, usergroupAccount):
        # MUST define these
        super(HostConfigSpec, self).__init__()
    
        self.data['activeDirectory'] = activeDirectory
        self.data['datastorePrincipal'] = datastorePrincipal
        self.data['datastorePrincipalPasswd'] = datastorePrincipalPasswd
        self.data['datetime'] = datetime
        self.data['firewall'] = firewall
        self.data['license'] = license
        self.data['memory'] = memory
        self.data['nasDatastore'] = nasDatastore
        self.data['network'] = network
        self.data['nicTypeSelection'] = nicTypeSelection
        self.data['option'] = option
        self.data['security'] = security
        self.data['service'] = service
        self.data['storageDevice'] = storageDevice
        self.data['userAccount'] = userAccount
        self.data['usergroupAccount'] = usergroupAccount
    
    
    @property
    def activeDirectory(self):
        '''Active Directory configuration change.
        '''
        return self.data['activeDirectory']

    @property
    def datastorePrincipal(self):
        '''Datastore principal user.
        '''
        return self.data['datastorePrincipal']

    @property
    def datastorePrincipalPasswd(self):
        '''Password for the datastore principal.
        '''
        return self.data['datastorePrincipalPasswd']

    @property
    def datetime(self):
        '''DateTime Configuration.
        '''
        return self.data['datetime']

    @property
    def firewall(self):
        '''Firewall configuration.
        '''
        return self.data['firewall']

    @property
    def license(self):
        '''License configuration for the host.
        '''
        return self.data['license']

    @property
    def memory(self):
        '''Memory configuration for the host.
        '''
        return self.data['memory']

    @property
    def nasDatastore(self):
        '''Configurations to create NAS datastores.
        '''
        return self.data['nasDatastore']

    @property
    def network(self):
        '''Network system information.
        '''
        return self.data['network']

    @property
    def nicTypeSelection(self):
        '''Type selection for different VirtualNics.
        '''
        return self.data['nicTypeSelection']

    @property
    def option(self):
        '''Host configuration options as defined by the OptionValue data object type.
        '''
        return self.data['option']

    @property
    def security(self):
        '''Security specification.
        '''
        return self.data['security']

    @property
    def service(self):
        '''Host service configuration.
        '''
        return self.data['service']

    @property
    def storageDevice(self):
        '''Storage system information.
        '''
        return self.data['storageDevice']

    @property
    def userAccount(self):
        '''List of users to create/update with new password.
        '''
        return self.data['userAccount']

    @property
    def usergroupAccount(self):
        '''List of users to create/update with new password.
        '''
        return self.data['usergroupAccount']

