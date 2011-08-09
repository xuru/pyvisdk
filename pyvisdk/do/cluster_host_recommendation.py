
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterHostRecommendation(DynamicData):
    '''A DRS recommended host for either powering on, resuming or reverting a virtual
        machine, or migrating a virtual machine from outside the cluster.
    '''
    
    def __init__(self, host, rating):
        # MUST define these
        super(ClusterHostRecommendation, self).__init__()
    
        self.data['host'] = host
        self.data['rating'] = rating
    
    
    @property
    def host(self):
        '''The recommended host.
        '''
        return self.data['host']

    @property
    def rating(self):
        '''Rating for the recommendation. Ratings range from 1 to 5, and the higher the
        rating, the stronger DRS suggests this host is picked for the operation.
        '''
        return self.data['rating']

