
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitchInfo(DynamicData):
    '''This class describes a DistributedVirtualSwitch that a device backing can attached
        to its ports.
    '''
    
    def __init__(self, distributedVirtualSwitch, switchName, switchUuid):
        # MUST define these
        super(DistributedVirtualSwitchInfo, self).__init__()
    
        self.data['distributedVirtualSwitch'] = distributedVirtualSwitch
        self.data['switchName'] = switchName
        self.data['switchUuid'] = switchUuid
    
    
    @property
    def distributedVirtualSwitch(self):
        '''The switch.
        '''
        return self.data['distributedVirtualSwitch']

    @property
    def switchName(self):
        '''The name of the switch.
        '''
        return self.data['switchName']

    @property
    def switchUuid(self):
        '''The UUID of the switch.
        '''
        return self.data['switchUuid']

