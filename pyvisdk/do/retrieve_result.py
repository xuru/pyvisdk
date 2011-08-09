
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class RetrieveResult(DynamicData):
    '''Result of RetrievePropertiesEx and ContinueRetrievePropertiesEx
    '''
    
    def __init__(self, objects, token):
        # MUST define these
        super(RetrieveResult, self).__init__()
    
        self.data['objects'] = objects
        self.data['token'] = token
    
    
    @property
    def objects(self):
        '''retrieved objects.
        '''
        return self.data['objects']

    @property
    def token(self):
        '''A token used to retrieve further retrieve results.
        '''
        return self.data['token']

