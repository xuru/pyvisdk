
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVirtualNicManagerNicTypeSelection(DynamicData):
    '''DataObject which lets a VirtualNic be marked for use as a
        HostVirtualNicManagerNicType.
    '''
    
    def __init__(self, nicType, vnic):
        # MUST define these
        super(HostVirtualNicManagerNicTypeSelection, self).__init__()
    
        self.data['nicType'] = nicType
        self.data['vnic'] = vnic
    
    
    @property
    def nicType(self):
        '''
        '''
        return self.data['nicType']

    @property
    def vnic(self):
        '''VirtualNic for the selection is being made
        '''
        return self.data['vnic']

