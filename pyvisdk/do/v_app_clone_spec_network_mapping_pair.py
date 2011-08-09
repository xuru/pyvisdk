
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VAppCloneSpecNetworkMappingPair(DynamicData):
    '''Maps one network to another as part of the clone process.Instances of this class
        are used in the field networkMapping
    '''
    
    def __init__(self, destination, source):
        # MUST define these
        super(VAppCloneSpecNetworkMappingPair, self).__init__()
    
        self.data['destination'] = destination
        self.data['source'] = source
    
    
    @property
    def destination(self):
        '''The destination network
        '''
        return self.data['destination']

    @property
    def source(self):
        '''The source network
        '''
        return self.data['source']

