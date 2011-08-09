
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OvfCreateDescriptorResult(DynamicData):
    '''The result of creating the OVF descriptor for the entity.
    '''
    
    def __init__(self, error, includeImageFiles, ovfDescriptor, warning):
        # MUST define these
        super(OvfCreateDescriptorResult, self).__init__()
    
        self.data['error'] = error
        self.data['includeImageFiles'] = includeImageFiles
        self.data['ovfDescriptor'] = ovfDescriptor
        self.data['warning'] = warning
    
    
    @property
    def error(self):
        '''Errors that happened during processing.
        '''
        return self.data['error']

    @property
    def includeImageFiles(self):
        '''Returns true if there are ISO or Floppy images attached to one or more VMs.
        '''
        return self.data['includeImageFiles']

    @property
    def ovfDescriptor(self):
        '''The OVF descriptor for the entity.
        '''
        return self.data['ovfDescriptor']

    @property
    def warning(self):
        '''Non-fatal warnings from the processing.
        '''
        return self.data['warning']

