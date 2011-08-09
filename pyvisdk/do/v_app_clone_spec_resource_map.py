
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VAppCloneSpecResourceMap(DynamicData):
    '''Maps source child entities to destination resource pools and resource settings. If
        a mapping is not specified, a child is copied as a direct child of the
        parent.
    '''
    
    def __init__(self, location, parent, resourceSpec, source):
        # MUST define these
        super(VAppCloneSpecResourceMap, self).__init__()
    
        self.data['location'] = location
        self.data['parent'] = parent
        self.data['resourceSpec'] = resourceSpec
        self.data['source'] = source
    
    
    @property
    def location(self):
        '''A client can optionally specify a datastore in the resource map to override the
        default datastore location set in location field. This enables cloning to
        different compute resources that do not have shared datastores.
        '''
        return self.data['location']

    @property
    def parent(self):
        '''Resource pool to use for the cloned entity of source. This must specify a resource
        pool that is not part of the vApp. If this is specified, a linked child
        (as opposed to a direct child) is created for the vApp.
        '''
        return self.data['parent']

    @property
    def resourceSpec(self):
        '''An optional resource configuration for the cloned entity of the source. If not
        specified, the same resource configuration as the source is used.
        '''
        return self.data['resourceSpec']

    @property
    def source(self):
        '''Source entity
        '''
        return self.data['source']

