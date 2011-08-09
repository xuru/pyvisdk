
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OvfResourceMap(DynamicData):
    '''Maps source child entities to destination resource pools and resource settings. If
        a mapping is not specified, a child is copied as a direct child of the
        parent.
    '''
    
    def __init__(self, datastore, parent, resourceSpec, source):
        # MUST define these
        super(OvfResourceMap, self).__init__()
    
        self.data['datastore'] = datastore
        self.data['parent'] = parent
        self.data['resourceSpec'] = resourceSpec
        self.data['source'] = source
    
    
    @property
    def datastore(self):
        '''A client can optionally specify a datastore location in the resource map to
        override the default datastore passed into CreateImportSpec field. This
        enables importing to different compute resources that do not have shared
        datastores.
        '''
        return self.data['datastore']

    @property
    def parent(self):
        '''The parent resource pool to use for the entity. This must specify a resource pool
        that is not part of the vApp. If this is specified, a linked child (as
        opposed to a direct child) is created for the vApp.
        '''
        return self.data['parent']

    @property
    def resourceSpec(self):
        '''An optional resource configuration for the created entity. If not specified, the
        resource configuration given in the OVF descriptor is used.
        '''
        return self.data['resourceSpec']

    @property
    def source(self):
        '''Identifies a source VirtualSystem or VirtualSystemCollection in an OVF descriptor.
        The source cannot be the root VirtualSystem or VirtualSystemCollection of
        the OVF. This is a path created by concatenating the OVF ids for each
        entity, e.g., "vm1", "WebTier/vm2", etc.
        '''
        return self.data['source']

