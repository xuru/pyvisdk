
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class InheritablePolicy(DynamicData):
    '''The base class for any type of setting or configuration that may get a inherited
        value.When used in a reconfgure operation specification, if inherited is
        true, it specifies the intention to change the values of subclass's
        properties to the inhertied values from the level above. In this case,
        users don't need to specify the values and any set property in the
        subclass will be ignored. if inherited is false, it specifies the
        intension to explicitly set subclass's properties to user specified
        values. Users should set the properties in the subclass with the desired
        values.When used in a configuration information object, The values of the
        properties in the subclass are the effective values. if inherited is true,
        the object is getting the effective values from upper level. If false, the
        values are explicitly set by a user.
    '''
    
    def __init__(self, inherited):
        # MUST define these
        super(InheritablePolicy, self).__init__()
    
        self.data['inherited'] = inherited
    
    
    @property
    def inherited(self):
        '''Whether the configuration is set to inherited value.
        '''
        return self.data['inherited']

