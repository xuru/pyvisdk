
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class PropertySpec(DynamicData):
    '''Within a PropertyFilterSpec, A PropertySpec specifies which properties should be
        reported to the client for objects of the given managed object type that
        are visited and not skipped. One more subtle side effect is that if a
        managed object is visited and not skipped, but there is no PropertySpec
        associated with the managed object's type, the managed object will not be
        reported to the client.Also, the set of properties applicable to a given
        managed object type is the union of the properties implied by the
        PropertySpec objects even, in the case of a RetrieveResult, where there
        may be an applicable PropertySpec in more than one filter.
    '''
    
    def __init__(self, all, pathSet, type):
        # MUST define these
        super(PropertySpec, self).__init__()
    
        self.data['all'] = all
        self.data['pathSet'] = pathSet
        self.data['type'] = type
    
    
    @property
    def all(self):
        '''Specifies whether or not all properties of the object are read. If this property
        is set to true, the pathSet property is ignored.
        '''
        return self.data['all']

    @property
    def pathSet(self):
        '''Specifies which managed object properties are retrieved. If the pathSet is empty,
        then the PropertyCollector retrieves references to the managed objects and
        no managed object properties are collected.
        '''
        return self.data['pathSet']

    @property
    def type(self):
        '''Name of the managed object type being collected.
        '''
        return self.data['type']

