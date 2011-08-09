
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterAction(DynamicData):
    '''Base class for all action recommendations in VirtualCenter.
    '''
    
    def __init__(self, target, type):
        # MUST define these
        super(ClusterAction, self).__init__()
    
        self.data['target'] = target
        self.data['type'] = type
    
    
    @property
    def target(self):
        '''The target object on which this action will be applied. For instance, a migration
        action will have a virtual machine as its target object, while a host
        power action will have a host as its target action.
        '''
        return self.data['target']

    @property
    def type(self):
        '''Type of the action. This is encoded to differentiate between different types of
        actions aimed at achieving different goals.
        '''
        return self.data['type']

