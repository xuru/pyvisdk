
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostSecuritySpec(DynamicData):
    '''DataObject used for configuring the Security settings
    '''
    
    def __init__(self, addPermission, adminPassword, removePermission):
        # MUST define these
        super(HostSecuritySpec, self).__init__()
    
        self.data['addPermission'] = addPermission
        self.data['adminPassword'] = adminPassword
        self.data['removePermission'] = removePermission
    
    
    @property
    def addPermission(self):
        '''Permissions to add
        '''
        return self.data['addPermission']

    @property
    def adminPassword(self):
        '''Administrator password to configure
        '''
        return self.data['adminPassword']

    @property
    def removePermission(self):
        '''Permissions to remove
        '''
        return self.data['removePermission']

