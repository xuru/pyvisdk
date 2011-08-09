
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVSContactInfo(DynamicData):
    '''Contact information of a human operator.
    '''
    
    def __init__(self, contact, name):
        # MUST define these
        super(DVSContactInfo, self).__init__()
    
        self.data['contact'] = contact
        self.data['name'] = name
    
    
    @property
    def contact(self):
        '''The contact information for the person.
        '''
        return self.data['contact']

    @property
    def name(self):
        '''The name of the person who is responsible for the switch.
        '''
        return self.data['name']

