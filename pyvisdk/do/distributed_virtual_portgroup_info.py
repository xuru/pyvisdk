
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualPortgroupInfo(DynamicData):
    '''This class describes a DistributedVirtualPortgroup that a device backing can be
        attached to.
    '''
    
    def __init__(self, portgroup, portgroupKey, portgroupName, portgroupType, switchName, switchUuid, uplinkPortgroup):
        # MUST define these
        super(DistributedVirtualPortgroupInfo, self).__init__()
    
        self.data['portgroup'] = portgroup
        self.data['portgroupKey'] = portgroupKey
        self.data['portgroupName'] = portgroupName
        self.data['portgroupType'] = portgroupType
        self.data['switchName'] = switchName
        self.data['switchUuid'] = switchUuid
        self.data['uplinkPortgroup'] = uplinkPortgroup
    
    
    @property
    def portgroup(self):
        '''The portgroup.
        '''
        return self.data['portgroup']

    @property
    def portgroupKey(self):
        '''The key of the portgroup.
        '''
        return self.data['portgroupKey']

    @property
    def portgroupName(self):
        '''The name of the portgroup.
        '''
        return self.data['portgroupName']

    @property
    def portgroupType(self):
        '''The type of portgroup. See DistributedVirtualPortgroupPortgroupType
        '''
        return self.data['portgroupType']

    @property
    def switchName(self):
        '''The name of the switch.
        '''
        return self.data['switchName']

    @property
    def switchUuid(self):
        '''The UUID of the switch.
        '''
        return self.data['switchUuid']

    @property
    def uplinkPortgroup(self):
        '''Whether this portgroup is an uplink portgroup.
        '''
        return self.data['uplinkPortgroup']

