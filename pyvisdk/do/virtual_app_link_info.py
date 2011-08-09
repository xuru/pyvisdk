
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualAppLinkInfo(DynamicData):
    '''
    '''
    
    def __init__(self, destroyWithParent, key):
        # MUST define these
        super(VirtualAppLinkInfo, self).__init__()
    
        self.data['destroyWithParent'] = destroyWithParent
        self.data['key'] = key
    
    
    @property
    def destroyWithParent(self):
        '''Whether the entity should be removed, when this vApp is removed
        '''
        return self.data['destroyWithParent']

    @property
    def key(self):
        '''The key contains a reference to the entity that is linked to this vApp
        '''
        return self.data['key']

