
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VAppProductInfo(DynamicData):
    '''Information that describes what product a vApp contains, e.g., what software that
        is installed in the contained virtual machines.
    '''
    
    def __init__(self, appUrl, classId, fullVersion, instanceId, key, name, productUrl, vendor, vendorUrl, version):
        # MUST define these
        super(VAppProductInfo, self).__init__()
    
        self.data['appUrl'] = appUrl
        self.data['classId'] = classId
        self.data['fullVersion'] = fullVersion
        self.data['instanceId'] = instanceId
        self.data['key'] = key
        self.data['name'] = name
        self.data['productUrl'] = productUrl
        self.data['vendor'] = vendor
        self.data['vendorUrl'] = vendorUrl
        self.data['version'] = version
    
    
    @property
    def appUrl(self):
        '''URL to entry-point for application. This is often specified using a macro, e.g.,
        http://${app.ip}/, where app.ip is a defined property on the virtual
        machine or vApp container.
        '''
        return self.data['appUrl']

    @property
    def classId(self):
        '''class name for this attribute
        '''
        return self.data['classId']

    @property
    def fullVersion(self):
        '''Full-version of the product, e.g., 1.0-build 12323.
        '''
        return self.data['fullVersion']

    @property
    def instanceId(self):
        '''class name for this attribute
        '''
        return self.data['instanceId']

    @property
    def key(self):
        '''A unqique key for the product section
        '''
        return self.data['key']

    @property
    def name(self):
        '''Name of the product.
        '''
        return self.data['name']

    @property
    def productUrl(self):
        '''URL to product homepage.
        '''
        return self.data['productUrl']

    @property
    def vendor(self):
        '''Vendor of the product.
        '''
        return self.data['vendor']

    @property
    def vendorUrl(self):
        '''URL to vendor homepage.
        '''
        return self.data['vendorUrl']

    @property
    def version(self):
        '''Short version of the product , e.g., 1.0.
        '''
        return self.data['version']

