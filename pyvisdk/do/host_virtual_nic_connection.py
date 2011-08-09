
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostVirtualNicConnection(DynamicData):
    '''DataObject which provides a level of indirection when identifying VirtualNics
        during configuration. This dataObject lets users specify a VirtualNic in
        terms of the portgroup/Dv Port the vnic is connected to. This is useful in
        cases where VirtualNic will be created as part of a configuration
        operation and the created VirtualNic is referred to in some other part of
        configuration. e.g: for configuring VMotion
    '''
    
    def __init__(self, dvPort, portgroup):
        # MUST define these
        super(HostVirtualNicConnection, self).__init__()
    
        self.data['dvPort'] = dvPort
        self.data['portgroup'] = portgroup
    
    
    @property
    def dvPort(self):
        '''Identifier for the DistributedVirtualPort. If the virtual nic is to be connected
        to a DVS, #dvPort will be set instead of #portgroup
        '''
        return self.data['dvPort']

    @property
    def portgroup(self):
        '''Name of the portgroup to which the virtual nic is connected to. If this parameter
        is set, use a virtual nic connected to a legacy portgroup.
        '''
        return self.data['portgroup']

