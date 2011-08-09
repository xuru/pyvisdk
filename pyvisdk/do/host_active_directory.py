
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostActiveDirectory(DynamicData):
    '''The HostActiveDirectory data object contains Active Directory configuration
        information for an ESX host.The vSphere API supports Microsoft Active
        Directory management of authentication for ESX hosts. To integrate an ESX
        host into an Active Directory environment, you use an Active Directory
        account that has the authority to add a computer to a domain. The ESX
        Server locates the Active Directory domain controller. When you use the
        host profile to configure authentication for an ESX host, you specify the
        configuration operation (add or remove). To add the host to a domain,
        specify the domain, and the authorized Active Directory account user name
        and password. You do not need to specify these parameters to remove the
        host from a domain because the host has the information it needs to
        perform the operation. When you call ApplyHostConfig_Task to apply the
        configuration, the ESX Server will call the appropriate method
        (JoinDomain_Task or LeaveCurrentDomain_Task) on your behalf.Before you
        call the method to apply the host profile, check to see that the
        HostAuthenticationManager.supportedStore array contains a
        HostActiveDirectoryAuthentication object. The presence of the Active
        Directory authentication object indicates that a host is capable of
        joining a domain. However, if you try to add a host to a domain when the
        HostAuthenticationStoreInfo.enabled property is , the join method will
        throw a fault.As an alternative to using the host profile to configure
        Active Directory authentication for an ESX host, your vSphere client
        application can call the HostActiveDirectoryAuthentication join and leave
        methods directly to add the host to or remove the host from a domain.To
        take advantage of ESX host membership in an Active Directory domain, grant
        permissions on the ESX host to users and groups in Active Directory who
        should have direct access to management of the ESX host. Use the
        UserDirectory.RetrieveUserGroups method to obtain information about Active
        Directory users and groups. After retrieving the Active Directory data,
        you can use the AuthorizationManager.SetEntityPermissions method to set
        the principal property to the appropriate user or group.By default, the
        ESX host assigns the Administrator role to the "ESX Admins" group. If the
        group does not exist when the host joins the domain, the host will not
        assign the role. In this case, you must create the "ESX Admins" group in
        the Active Directory. The host will periodically check the domain
        controller for the group and will assign the role when the group exists.
    '''
    
    def __init__(self, changeOperation, spec):
        # MUST define these
        super(HostActiveDirectory, self).__init__()
    
        self.data['changeOperation'] = changeOperation
        self.data['spec'] = spec
    
    
    @property
    def changeOperation(self):
        '''Configuration change operation to apply to the host. You can specify the following
        values: * add: Add the host to the domain. The ESX Server will use the
        HostActiveDirectorySpec information (domain, account user name and
        password) to call JoinDomain_Task. * remove: Remove the host from its
        current domain. The ESX Server will call LeaveCurrentDomain_Task,
        specifying
        '''
        return self.data['changeOperation']

    @property
    def spec(self):
        '''Active Directory domain access information (domain and account user name and
        password).
        '''
        return self.data['spec']

