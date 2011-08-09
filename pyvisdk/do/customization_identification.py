
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class CustomizationIdentification(DynamicData):
    '''The Identification data object type provides information needed to join a
        workgroup or domain.The Identification data object type maps to the
        Identification key in the answer file. These values are transferred into
        the file that VirtualCenter stores on the target virtual disk. For more
        detailed information, see the document .
    '''
    
    def __init__(self, domainAdmin, domainAdminPassword, joinDomain, joinWorkgroup):
        # MUST define these
        super(CustomizationIdentification, self).__init__()
    
        self.data['domainAdmin'] = domainAdmin
        self.data['domainAdminPassword'] = domainAdminPassword
        self.data['joinDomain'] = joinDomain
        self.data['joinWorkgroup'] = joinWorkgroup
    
    
    @property
    def domainAdmin(self):
        '''This is the domain user account used for authentication if the virtual machine is
        joining a domain. The user does not need to be a domain administrator, but
        the account must have the privileges required to add computers to the
        domain.
        '''
        return self.data['domainAdmin']

    @property
    def domainAdminPassword(self):
        '''This is the password for the domain user account used for authentication if the
        virtual machine is joining a domain.
        '''
        return self.data['domainAdminPassword']

    @property
    def joinDomain(self):
        '''The domain that the virtual machine should join. If this value is supplied, then
        domainAdmin and domainAdminPassword must also be supplied, and the
        workgroup name must be empty.
        '''
        return self.data['joinDomain']

    @property
    def joinWorkgroup(self):
        '''The workgroup that the virtual machine should join. If this value is supplied,
        then the domain name and authentication fields must be empty.
        '''
        return self.data['joinWorkgroup']

