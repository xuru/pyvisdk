
from pyvisdk.base.base_data import BaseData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DynamicData(BaseData):
    '''DynamicData is a builtin object model data object type for manipulating data
        properties dynamically. The primary usage is as a base class for types
        that may be extended with subtypes in the future, where new properties
        should be sent to old clients as a set of dynamic properties.
    '''
    
    def __init__(self, dynamicProperty, dynamicType):
        # MUST define these
        super(DynamicData, self).__init__()
    
        self.data['dynamicProperty'] = dynamicProperty
        self.data['dynamicType'] = dynamicType
    
    
    @property
    def dynamicProperty(self):
        '''Set of dynamic properties. This property is optional because only the properties
        of an object that are unknown to a client will be part of this set. This
        property is not readonly just in case we want to send such properties from
        a client in the future.
        '''
        return self.data['dynamicProperty']

    @property
    def dynamicType(self):
        '''Reserved.
        '''
        return self.data['dynamicType']

