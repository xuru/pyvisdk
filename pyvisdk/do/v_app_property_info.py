
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VAppPropertyInfo(DynamicData):
    '''A vApp Property description, including deployment values
    '''
    
    def __init__(self, category, classId, defaultValue, description, id, instanceId, key, label, type, userConfigurable, value):
        # MUST define these
        super(VAppPropertyInfo, self).__init__()
    
        self.data['category'] = category
        self.data['classId'] = classId
        self.data['defaultValue'] = defaultValue
        self.data['description'] = description
        self.data['id'] = id
        self.data['instanceId'] = instanceId
        self.data['key'] = key
        self.data['label'] = label
        self.data['type'] = type
        self.data['userConfigurable'] = userConfigurable
        self.data['value'] = value
    
    
    @property
    def category(self):
        '''A user-visible description the category the property belongs to.
        '''
        return self.data['category']

    @property
    def classId(self):
        '''class name for this property
        '''
        return self.data['classId']

    @property
    def defaultValue(self):
        '''This either contains the default value of a field (used if value is empty string),
        or the expression if the type is "expression". See comment for the
        '''
        return self.data['defaultValue']

    @property
    def description(self):
        '''A description of the field.
        '''
        return self.data['description']

    @property
    def id(self):
        '''Name of property. In the OVF environment, the property is listed as
        [classId.]id[.instanceId]. The [classId.]name[.instanceId] must be unique.
        '''
        return self.data['id']

    @property
    def instanceId(self):
        '''class name for this property
        '''
        return self.data['instanceId']

    @property
    def key(self):
        '''A unique integer key for the property.
        '''
        return self.data['key']

    @property
    def label(self):
        '''The display name for the property.
        '''
        return self.data['label']

    @property
    def type(self):
        '''Describes the valid format of the property.
        '''
        return self.data['type']

    @property
    def userConfigurable(self):
        '''Whether the property is user-configurable or a system property. This is not used
        if the type is expression.
        '''
        return self.data['userConfigurable']

    @property
    def value(self):
        '''The value of the field at deployment time. For expressions, this will contain the
        value that has been computed.
        '''
        return self.data['value']

