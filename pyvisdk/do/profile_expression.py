
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ProfileExpression(DynamicData):
    '''
    '''
    
    def __init__(self, displayName, id, negated):
        # MUST define these
        super(ProfileExpression, self).__init__()
    
        self.data['displayName'] = displayName
        self.data['id'] = id
        self.data['negated'] = negated
    
    
    @property
    def displayName(self):
        '''User visible display name
        '''
        return self.data['displayName']

    @property
    def id(self):
        '''Identifier of this expression. The id has to be unique within a Profile. The id
        can be used as a key while building composite expressions.
        '''
        return self.data['id']

    @property
    def negated(self):
        '''Flag indicating if the condition of the expression should be negated. e.g:
        conditions like VSwitch0 has vmnic0 connected to it can be turned into
        VSwitch0 doesn't have vmnic0 connected to it.
        '''
        return self.data['negated']

