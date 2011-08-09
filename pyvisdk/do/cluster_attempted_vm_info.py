
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterAttemptedVmInfo(DynamicData):
    '''This data class reports virtual machine powerOn information.
    '''
    
    def __init__(self, task, vm):
        # MUST define these
        super(ClusterAttemptedVmInfo, self).__init__()
    
        self.data['task'] = task
        self.data['vm'] = vm
    
    
    @property
    def task(self):
        '''The ID of the task, which monitors powering on.
        '''
        return self.data['task']

    @property
    def vm(self):
        '''The virtual machine being powered on.
        '''
        return self.data['vm']

