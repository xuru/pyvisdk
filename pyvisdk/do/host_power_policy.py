
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPowerPolicy(DynamicData):
    '''Power Management Policy data object. Used to retrieve and specify current host
        power management policy.
    '''
    
    def __init__(self, description, key, name, shortName):
        # MUST define these
        super(HostPowerPolicy, self).__init__()
    
        self.data['description'] = description
        self.data['key'] = key
        self.data['name'] = name
        self.data['shortName'] = shortName
    
    
    @property
    def description(self):
        '''Power Policy Description.
        '''
        return self.data['description']

    @property
    def key(self):
        '''Power Policy Key. Internally generated key which uniquely identifies power
        management policy on a host.
        '''
        return self.data['key']

    @property
    def name(self):
        '''Power Policy Name.
        '''
        return self.data['name']

    @property
    def shortName(self):
        '''Power Policy Short Name. This is not localizable property which can be used to
        identify specific power managing policies like "custom" power policy.
        Custom power policy has short name set to "custom".
        '''
        return self.data['shortName']

