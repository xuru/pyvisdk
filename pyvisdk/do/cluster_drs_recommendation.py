
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterDrsRecommendation(DynamicData):
    '''DrsRecommendation describes a recommendation to migrate one or more virtual
        machines.
    '''
    
    def __init__(self, key, migrationList, rating, reason, reasonText):
        # MUST define these
        super(ClusterDrsRecommendation, self).__init__()
    
        self.data['key'] = key
        self.data['migrationList'] = migrationList
        self.data['rating'] = rating
        self.data['reason'] = reason
        self.data['reasonText'] = reasonText
    
    
    @property
    def key(self):
        '''Key to identify the recommendation when calling applyRecommendation.
        '''
        return self.data['key']

    @property
    def migrationList(self):
        '''
        '''
        return self.data['migrationList']

    @property
    def rating(self):
        '''A rating of the recommendation. Valid values range from 1 (lowest confidence) to 5
        (highest confidence).
        '''
        return self.data['rating']

    @property
    def reason(self):
        '''A reason code explaining why this set of migrations is being suggested.
        '''
        return self.data['reason']

    @property
    def reasonText(self):
        '''Text that provides more information about the reason code for the suggested set of
        migrations.
        '''
        return self.data['reasonText']

