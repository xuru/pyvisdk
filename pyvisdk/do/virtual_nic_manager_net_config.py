
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualNicManagerNetConfig(DynamicData):
    '''The NetConfig data object type contains the networking configuration.
    '''
    
    def __init__(self, candidateVnic, multiSelectAllowed, nicType, selectedVnic):
        # MUST define these
        super(VirtualNicManagerNetConfig, self).__init__()
    
        self.data['candidateVnic'] = candidateVnic
        self.data['multiSelectAllowed'] = multiSelectAllowed
        self.data['nicType'] = nicType
        self.data['selectedVnic'] = selectedVnic
    
    
    @property
    def candidateVnic(self):
        '''List of VirtualNic objects that may be used. This will be a subset of the list of
        VirtualNics in vnic.
        '''
        return self.data['candidateVnic']

    @property
    def multiSelectAllowed(self):
        '''Whether multiple nics can be selected for this nicType.
        '''
        return self.data['multiSelectAllowed']

    @property
    def nicType(self):
        '''The NicType of this NetConfig.
        '''
        return self.data['nicType']

    @property
    def selectedVnic(self):
        '''List of VirtualNic objects that are selected for use.
        '''
        return self.data['selectedVnic']

