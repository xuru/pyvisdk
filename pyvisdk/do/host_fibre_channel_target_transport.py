
from pyvisdk.do.host_target_transport import HostTargetTransport
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostFibreChannelTargetTransport(HostTargetTransport):
    '''Fibre Channel transport information about a SCSI target.
    '''
    
    def __init__(self, nodeWorldWideName, portWorldWideName):
        # MUST define these
        super(HostFibreChannelTargetTransport, self).__init__()
    
        self.data['nodeWorldWideName'] = nodeWorldWideName
        self.data['portWorldWideName'] = portWorldWideName
    
    
    @property
    def nodeWorldWideName(self):
        '''The world wide node name of the target.
        '''
        return self.data['nodeWorldWideName']

    @property
    def portWorldWideName(self):
        '''The world wide port name of the target.
        '''
        return self.data['portWorldWideName']

