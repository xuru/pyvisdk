
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVMotionCompatibility(DynamicData):
    '''The object type for the array returned by queryVMotionCompatibility; specifies the
        VMotion compatibility types for a host.
    '''
    
    def __init__(self, compatibility, host):
        # MUST define these
        super(HostVMotionCompatibility, self).__init__()
    
        self.data['compatibility'] = compatibility
        self.data['host'] = host
    
    
    @property
    def compatibility(self):
        '''Ways in which the host is compatible with the designated virtual machine that is a
        candidate for VMotion. This array will be a subset of the set of
        VMotionCompatibilityType strings that were input to
        queryVMotionCompatibility.
        '''
        return self.data['compatibility']

    @property
    def host(self):
        '''The prospective host for the virtual machine.
        '''
        return self.data['host']

