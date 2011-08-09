
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterPowerOnVmResult(DynamicData):
    '''PowerOnVmResult is the base class of the result returned to the
        PowerOnMultiVM_Task method.
    '''
    
    def __init__(self, attempted, notAttempted, recommendations):
        # MUST define these
        super(ClusterPowerOnVmResult, self).__init__()
    
        self.data['attempted'] = attempted
        self.data['notAttempted'] = notAttempted
        self.data['recommendations'] = recommendations
    
    
    @property
    def attempted(self):
        '''The list of virtual machines the Virtual Center has attempted to power on. For a
        virtual machine not managed by DRS, a task ID is also returned.
        '''
        return self.data['attempted']

    @property
    def notAttempted(self):
        '''The list of virtual machines DRS can not find suitable hosts for powering on.
        There is one fault associated with each virtual machine.
        '''
        return self.data['notAttempted']

    @property
    def recommendations(self):
        '''The list of recommendations that need the client to approve manually.
        '''
        return self.data['recommendations']

