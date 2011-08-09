
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostProfileManagerConfigTaskList(DynamicData):
    '''DataObject which represents list of tasks that will be performed on the host
        during application of a HostProfile.
    '''
    
    def __init__(self, configSpec, taskDescription):
        # MUST define these
        super(HostProfileManagerConfigTaskList, self).__init__()
    
        self.data['configSpec'] = configSpec
        self.data['taskDescription'] = taskDescription
    
    
    @property
    def configSpec(self):
        '''ConfigSpec describing a list of tasks that will be performed on the host to carry
        out HostProfile application.
        '''
        return self.data['configSpec']

    @property
    def taskDescription(self):
        '''Description of tasks that will to be performed on the host to carry out
        HostProfile application.
        '''
        return self.data['taskDescription']

