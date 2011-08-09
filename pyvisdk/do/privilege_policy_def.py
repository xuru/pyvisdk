
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PrivilegePolicyDef(DynamicData):
    '''Describes a basic privilege policy.
    '''
    
    def __init__(self, createPrivilege, deletePrivilege, readPrivilege, updatePrivilege):
        # MUST define these
        super(PrivilegePolicyDef, self).__init__()
    
        self.data['createPrivilege'] = createPrivilege
        self.data['deletePrivilege'] = deletePrivilege
        self.data['readPrivilege'] = readPrivilege
        self.data['updatePrivilege'] = updatePrivilege
    
    
    @property
    def createPrivilege(self):
        '''Name of privilege required for creation.
        '''
        return self.data['createPrivilege']

    @property
    def deletePrivilege(self):
        '''Name of privilege required for deleting.
        '''
        return self.data['deletePrivilege']

    @property
    def readPrivilege(self):
        '''Name of privilege required for reading.
        '''
        return self.data['readPrivilege']

    @property
    def updatePrivilege(self):
        '''Name of privilege required for updating.
        '''
        return self.data['updatePrivilege']

