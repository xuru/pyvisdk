
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ExtensionPrivilegeInfo(DynamicData):
    '''This data object type describes privileges defined by the extension.
    '''
    
    def __init__(self, privGroupName, privID):
        # MUST define these
        super(ExtensionPrivilegeInfo, self).__init__()
    
        self.data['privGroupName'] = privGroupName
        self.data['privID'] = privID
    
    
    @property
    def privGroupName(self):
        '''Hierarchical group name. Each level of the grouping hierarchy is separated by a
        "." so group names may not include a ".". privGroupName.
        '''
        return self.data['privGroupName']

    @property
    def privID(self):
        '''The ID of the privilege. The format should be "<group name>.<privilege name>". The
        group name should be the same as the privGroupName property.
        '''
        return self.data['privID']

