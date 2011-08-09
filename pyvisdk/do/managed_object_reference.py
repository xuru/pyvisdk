
from pyvisdk.base.base_data import BaseData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ManagedObjectReference(BaseData):
    '''This class is used to refer to a server-side Managed Object.
    '''
    
    def __init__(self, type, value):
        # MUST define these
        super(ManagedObjectReference, self).__init__()
    
        self.data['type'] = type
        self.data['value'] = value
    
    
    @property
    def type(self):
        '''The name of the Managed Object type this ManagedObjectReference refers to.
        '''
        return self.data['type']

    @property
    def value(self):
        '''The specific instance of Managed Object this ManagedObjectReference refers to.
        '''
        return self.data['value']

