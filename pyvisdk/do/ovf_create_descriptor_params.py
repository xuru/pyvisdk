
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OvfCreateDescriptorParams(DynamicData):
    '''Collection of parameters for createDescriptor
    '''
    
    def __init__(self, description, includeImageFiles, name, ovfFiles):
        # MUST define these
        super(OvfCreateDescriptorParams, self).__init__()
    
        self.data['description'] = description
        self.data['includeImageFiles'] = includeImageFiles
        self.data['name'] = name
        self.data['ovfFiles'] = ovfFiles
    
    
    @property
    def description(self):
        '''The contents of the Annontation section of the top-level OVF Entity. If unset, any
        existing annotation on the entity is left unchanged.
        '''
        return self.data['description']

    @property
    def includeImageFiles(self):
        '''Controls whether attached image files should be included in the descriptor. This
        applies to image files attached to VirtualCdrom and VirtualFloppy.
        '''
        return self.data['includeImageFiles']

    @property
    def name(self):
        '''The ovf:id to use for the top-level OVF Entity. If unset, the entity's product
        name is used if available. Otherwise, the VI entity name is used.
        '''
        return self.data['name']

    @property
    def ovfFiles(self):
        '''Contains information about the files of the entity, if they have already been
        downloaded. Needed to construct the References section of the descriptor.
        '''
        return self.data['ovfFiles']

