
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class OvfCreateImportSpecResult(DynamicData):
    '''The CreateImportSpecResult contains all information regarding the import that can
        be extracted from the OVF descriptor.For example, this includes the list
        of items that the caller must upload in order to complete the import, but
        not the list of URLs to which the files must be uploaded. These paths are
        not known until the VMs have been created, ie. until
        ResourcePool.importVApp has been called.
    '''
    
    def __init__(self, error, fileItem, importSpec, warning):
        # MUST define these
        super(OvfCreateImportSpecResult, self).__init__()
    
        self.data['error'] = error
        self.data['fileItem'] = fileItem
        self.data['importSpec'] = importSpec
        self.data['warning'] = warning
    
    
    @property
    def error(self):
        '''Errors that happened during processing. Something will be wrong with the
        ImportSpec, or it is not present.
        '''
        return self.data['error']

    @property
    def fileItem(self):
        '''The files that must be uploaded by the caller as part of importing the entity.
        '''
        return self.data['fileItem']

    @property
    def importSpec(self):
        '''The ImportSpec contains information about which VirtualMachines and VirtualApps
        are present in the entity and how they relate to each other.
        '''
        return self.data['importSpec']

    @property
    def warning(self):
        '''Non-fatal warnings from the processing. The ImportSpec will be valid, but the user
        may choose to reject it based on these warnings.
        '''
        return self.data['warning']

