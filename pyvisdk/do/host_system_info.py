
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostSystemInfo(DynamicData):
    '''Information about the system as a whole.
    '''
    
    def __init__(self, model, otherIdentifyingInfo, uuid, vendor):
        # MUST define these
        super(HostSystemInfo, self).__init__()
    
        self.data['model'] = model
        self.data['otherIdentifyingInfo'] = otherIdentifyingInfo
        self.data['uuid'] = uuid
        self.data['vendor'] = vendor
    
    
    @property
    def model(self):
        '''System model identification.
        '''
        return self.data['model']

    @property
    def otherIdentifyingInfo(self):
        '''Other System identification information. This information may be vendor specific
        '''
        return self.data['otherIdentifyingInfo']

    @property
    def uuid(self):
        '''Hardware BIOS identification.
        '''
        return self.data['uuid']

    @property
    def vendor(self):
        '''Hardware vendor identification.
        '''
        return self.data['vendor']

