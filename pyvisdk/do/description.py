
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class Description(DynamicData):
    '''Static strings used for describing an object or property.
    '''
    
    def __init__(self, label, summary):
        # MUST define these
        super(Description, self).__init__()
    
        self.data['label'] = label
        self.data['summary'] = summary
    
    
    @property
    def label(self):
        '''Display label.
        '''
        return self.data['label']

    @property
    def summary(self):
        '''Summary description.
        '''
        return self.data['summary']

