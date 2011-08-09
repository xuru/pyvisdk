
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DistributedVirtualSwitchProductSpec(DynamicData):
    '''This data object type is a subset of AboutInfo. An object of this type can be used
        to describe the specification for a proxy switch module of a
        DistributedVirtualSwitch.
    '''
    
    def __init__(self, build, bundleId, bundleUrl, forwardingClass, name, vendor, version):
        # MUST define these
        super(DistributedVirtualSwitchProductSpec, self).__init__()
    
        self.data['build'] = build
        self.data['bundleId'] = bundleId
        self.data['bundleUrl'] = bundleUrl
        self.data['forwardingClass'] = forwardingClass
        self.data['name'] = name
        self.data['vendor'] = vendor
        self.data['version'] = version
    
    
    @property
    def build(self):
        '''Build string for the server on which this call is made. For example, x.y.z-num.
        This string does not apply to the API.
        '''
        return self.data['build']

    @property
    def bundleId(self):
        '''The ID of the bundle if a host component bundle needs to be installed on the host
        members to support the functionality of the switch.
        '''
        return self.data['bundleId']

    @property
    def bundleUrl(self):
        '''The URL of the bundle that VMware Update Manager will use to install the bundle on
        the host members, if bundleId is set.
        '''
        return self.data['bundleUrl']

    @property
    def forwardingClass(self):
        '''Forwarding class of the distributed virtual switch.
        '''
        return self.data['forwardingClass']

    @property
    def name(self):
        '''Short form of the product name.
        '''
        return self.data['name']

    @property
    def vendor(self):
        '''Name of the vendor of this product.
        '''
        return self.data['vendor']

    @property
    def version(self):
        '''Dot-separated version string. For example, "1.2".
        '''
        return self.data['version']

