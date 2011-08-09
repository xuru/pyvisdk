
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPortGroupConfig(DynamicData):
    '''This describes the port group configuration containing both the configurable
        properties on a port group and the associated virtual switch.
    '''
    
    def __init__(self, changeOperation, spec):
        # MUST define these
        super(HostPortGroupConfig, self).__init__()
    
        self.data['changeOperation'] = changeOperation
        self.data['spec'] = spec
    
    
    @property
    def changeOperation(self):
        '''Indicates the change operation to apply on this configuration specification.
        '''
        return self.data['changeOperation']

    @property
    def spec(self):
        '''The specification of the port group.
        '''
        return self.data['spec']

