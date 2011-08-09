
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineFileLayoutExFileInfo(DynamicData):
    '''Basic information about a file.
    '''
    
    def __init__(self, key, name, size, type):
        # MUST define these
        super(VirtualMachineFileLayoutExFileInfo, self).__init__()
    
        self.data['key'] = key
        self.data['name'] = name
        self.data['size'] = size
        self.data['type'] = type
    
    
    @property
    def key(self):
        '''Key to reference this file.
        '''
        return self.data['key']

    @property
    def name(self):
        '''Name of the file, including the complete datastore path.
        '''
        return self.data['name']

    @property
    def size(self):
        '''Size of the file in bytes.
        '''
        return self.data['size']

    @property
    def type(self):
        '''Type of the file. VirtualMachineFileLayoutExFileType lists all valid values.
        '''
        return self.data['type']

