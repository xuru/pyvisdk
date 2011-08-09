
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VnicPortArgument(DynamicData):
    '''This argument records a vnic device that connects to a DVPort.
    '''
    
    def __init__(self, port, vnic):
        # MUST define these
        super(VnicPortArgument, self).__init__()
    
        self.data['port'] = port
        self.data['vnic'] = vnic
    
    
    @property
    def port(self):
        '''The DVPorts that were being used.
        '''
        return self.data['port']

    @property
    def vnic(self):
        '''The vnic devices that were using the DVports.
        '''
        return self.data['vnic']

