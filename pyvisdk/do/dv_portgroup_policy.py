
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DVPortgroupPolicy(DynamicData):
    '''The DistributedVirtualPortgroup policies. This field is not applicable when
        queried directly against an ESX host.
    '''
    
    def __init__(self, blockOverrideAllowed, livePortMovingAllowed, portConfigResetAtDisconnect, shapingOverrideAllowed, vendorConfigOverrideAllowed):
        # MUST define these
        super(DVPortgroupPolicy, self).__init__()
    
        self.data['blockOverrideAllowed'] = blockOverrideAllowed
        self.data['livePortMovingAllowed'] = livePortMovingAllowed
        self.data['portConfigResetAtDisconnect'] = portConfigResetAtDisconnect
        self.data['shapingOverrideAllowed'] = shapingOverrideAllowed
        self.data['vendorConfigOverrideAllowed'] = vendorConfigOverrideAllowed
    
    
    @property
    def blockOverrideAllowed(self):
        '''Allow the blocked setting of an individual port to override the setting in
        defaultPortConfig of a portgroup.
        '''
        return self.data['blockOverrideAllowed']

    @property
    def livePortMovingAllowed(self):
        '''Allow a live port to be moved in and out of the portgroup.
        '''
        return self.data['livePortMovingAllowed']

    @property
    def portConfigResetAtDisconnect(self):
        '''If true, reset the port network setting back to the portgroup setting (thus
        removing the per-port setting) when the port is disconnected from the
        connectee.
        '''
        return self.data['portConfigResetAtDisconnect']

    @property
    def shapingOverrideAllowed(self):
        '''Allow the inShapingPolicy or outShapingPolicy settings of an individual port to
        override the setting in defaultPortConfig of a portgroup.
        '''
        return self.data['shapingOverrideAllowed']

    @property
    def vendorConfigOverrideAllowed(self):
        '''Allow the vendorSpecificConfig setting of an individual port to override the
        setting in defaultPortConfig of a portgroup.
        '''
        return self.data['vendorConfigOverrideAllowed']

