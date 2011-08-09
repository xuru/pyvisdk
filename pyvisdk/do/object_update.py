
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ObjectUpdate(DynamicData):
    '''The ObjectUpdate data object type contains information about changes to a
        particular managed object. We distinguish updates when an object is
        created, destroyed, or modified, as well as when the object enters or
        leaves the set of objects dynamically associated with a filter.
    '''
    
    def __init__(self, changeSet, kind, missingSet, obj):
        # MUST define these
        super(ObjectUpdate, self).__init__()
    
        self.data['changeSet'] = changeSet
        self.data['kind'] = kind
        self.data['missingSet'] = missingSet
        self.data['obj'] = obj
    
    
    @property
    def changeSet(self):
        '''Optional set of changes to the object. Present only if the "kind" is either
        "modify" or "enter".
        '''
        return self.data['changeSet']

    @property
    def kind(self):
        '''Kind of update that caused the filter to report a change.
        '''
        return self.data['kind']

    @property
    def missingSet(self):
        '''Properties whose value could not be retrieved and their associated faults. Present
        only if the "kind" is either "modify" or "enter".
        '''
        return self.data['missingSet']

    @property
    def obj(self):
        '''Reference to the managed object to which this update applies.
        '''
        return self.data['obj']

