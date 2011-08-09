
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualDeviceConfigSpec(DynamicData):
    '''The VirtualDeviceSpec data object type encapsulates change specifications for an
        individual virtual device. The virtual device being added or modified must
        be fully specified.
    '''
    
    def __init__(self, device, fileOperation, operation):
        # MUST define these
        super(VirtualDeviceConfigSpec, self).__init__()
    
        self.data['device'] = device
        self.data['fileOperation'] = fileOperation
        self.data['operation'] = operation
    
    
    @property
    def device(self):
        '''Device specification, with all necessary properties set.
        '''
        return self.data['device']

    @property
    def fileOperation(self):
        '''Type of operation being performed on the backing of the specified virtual device.
        If no file operation is specified in the VirtualDeviceSpec, then any
        backing filenames in the VirtualDevice must refer to files that already
        exist. The "replace" and "delete" values for this property are only
        applicable to virtual disk backing files.
        '''
        return self.data['fileOperation']

    @property
    def operation(self):
        '''Type of operation being performed on the specified virtual device. If no operation
        is specified, the spec. is ignored.
        '''
        return self.data['operation']

