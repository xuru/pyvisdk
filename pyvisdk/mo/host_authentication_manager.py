
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostAuthenticationManager(BaseEntity):
    '''The HostAuthenticationManager managed object provides access to Active
    Directory configuration information for an ESX host. It also provides access to
    methods for adding a host to or removing a host from an Active Directory
    domain.The vSphere API supports Microsoft Active Directory management of
    authentication for ESX hosts. To integrate an ESX host into an Active Directory
    environment, you use an Active Directory account that has the authority to add
    a computer to a domain. The ESX Server locates the Active Directory domain
    controller. When you add a host to a domain, you only need to specify the
    domain and the account user name and password.There are two approaches that you
    can use to add an ESX host to or remove a host from an Active Directory
    domain.* JoinDomain_Task and LeaveCurrentDomain_Task methods - Your vSphere
    client application can call these methods directly to add the host to or remove
    the host from a domain. * Host configuration - Use the HostActiveDirectory data
    object to specify Active Directory configuration, either adding the host to or
    removing the host from a domain. To apply the Active Directory configuration,
    use the HostProfileManager method (ApplyHostConfig_Task) to apply the
    HostConfigSpec. When the ESX Server processes the configuration, it will invoke
    the join or leave method.To take advantage of ESX host membership in an Active
    Directory domain, grant permissions on the ESX host to Active Directory users
    and groups who should have direct access to management of the ESX host. Use the
    UserDirectory.RetrieveUserGroups method to obtain information about Active
    Directory users and groups. After retrieving the Active Directory data, you can
    use the AuthorizationManager.SetEntityPermissions method to set the principal
    property to the appropriate user or group.By default, the ESX host assigns the
    Administrator role to the "ESX Admins" group. If the group does not exist when
    the host joins the domain, the host will not assign the role. In this case, you
    must create the "ESX Admins" group in the Active Directory. The host will
    periodically check the domain controller for the group and will assign the role
    when the group exists.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.HostAuthenticationManager):
        super(HostAuthenticationManager, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def info(self):
        '''Information about Active Directory membership.'''
        return self.update('info')
    @property
    def supportedStore(self):
        '''An array that can contain managed object references to local and Active
        Directory authentication managed objects.'''
        return self.update('supportedStore')

    