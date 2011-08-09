
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterDasHostRecommendation(DynamicData):
    '''A host recommendation for a virtual machine managed by the VMware HA Service.
    '''
    
    def __init__(self, drsRating, host):
        # MUST define these
        super(ClusterDasHostRecommendation, self).__init__()
    
        self.data['drsRating'] = drsRating
        self.data['host'] = host
    
    
    @property
    def drsRating(self):
        '''Rating as computed by DRS for a DRS-enabled cluster. Rating range from 1 to 5, and
        the higher the rating, the stronger DRS suggests this host is picked for
        the operation.
        '''
        return self.data['drsRating']

    @property
    def host(self):
        '''The recommended host.
        '''
        return self.data['host']

