
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ClusterRecommendation(DynamicData):
    '''Recommendation is the base class for any packaged group of actions that are
        intended to take the system from one state to another one.
    '''
    
    def __init__(self, action, key, prerequisite, rating, reason, reasonText, target, time, type):
        # MUST define these
        super(ClusterRecommendation, self).__init__()
    
        self.data['action'] = action
        self.data['key'] = key
        self.data['prerequisite'] = prerequisite
        self.data['rating'] = rating
        self.data['reason'] = reason
        self.data['reasonText'] = reasonText
        self.data['target'] = target
        self.data['time'] = time
        self.data['type'] = type
    
    
    @property
    def action(self):
        '''List of actions that are executed as part of this recommendation
        '''
        return self.data['action']

    @property
    def key(self):
        '''Key to identify the recommendation when calling applyRecommendation.
        '''
        return self.data['key']

    @property
    def prerequisite(self):
        '''This recommendation may depend on some other recommendations. The prerequisite
        recommendations are listed by their keys.
        '''
        return self.data['prerequisite']

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

    @property
    def target(self):
        '''The target object of this recommendation.
        '''
        return self.data['target']

    @property
    def time(self):
        '''The time this recommendation was computed.
        '''
        return self.data['time']

    @property
    def type(self):
        '''Type of the recommendation. This differentiates between various of recommendations
        aimed at achieving different goals.
        '''
        return self.data['type']

