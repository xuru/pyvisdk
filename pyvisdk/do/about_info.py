
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class AboutInfo(DynamicData):
    '''This data object type describes system information including the name, type,
        version, and build number.
    '''
    
    def __init__(self, apiType, apiVersion, build, fullName, instanceUuid, licenseProductName, licenseProductVersion, localeBuild, localeVersion, name, osType, productLineId, vendor, version):
        # MUST define these
        super(AboutInfo, self).__init__()
    
        self.data['apiType'] = apiType
        self.data['apiVersion'] = apiVersion
        self.data['build'] = build
        self.data['fullName'] = fullName
        self.data['instanceUuid'] = instanceUuid
        self.data['licenseProductName'] = licenseProductName
        self.data['licenseProductVersion'] = licenseProductVersion
        self.data['localeBuild'] = localeBuild
        self.data['localeVersion'] = localeVersion
        self.data['name'] = name
        self.data['osType'] = osType
        self.data['productLineId'] = productLineId
        self.data['vendor'] = vendor
        self.data['version'] = version
    
    
    @property
    def apiType(self):
        '''Indicates whether or not the service instance represents a standalone host. If the
        service instance represents a standalone host, then the physical inventory
        for that service instance is fixed to that single host. VirtualCenter
        server provides additional features over single hosts. For example,
        VirtualCenter offers multi-host management.
        '''
        return self.data['apiType']

    @property
    def apiVersion(self):
        '''The version of the API as a dot-separated string. For example, "1.0.0".
        '''
        return self.data['apiVersion']

    @property
    def build(self):
        '''Build string for the server on which this call is made. For example, x.y.z-num.
        This string does not apply to the API.
        '''
        return self.data['build']

    @property
    def fullName(self):
        '''The complete product name, including the version information.
        '''
        return self.data['fullName']

    @property
    def instanceUuid(self):
        '''A globally unique identifier associated with this service instance.
        '''
        return self.data['instanceUuid']

    @property
    def licenseProductName(self):
        '''The license product name
        '''
        return self.data['licenseProductName']

    @property
    def licenseProductVersion(self):
        '''The license product version
        '''
        return self.data['licenseProductVersion']

    @property
    def localeBuild(self):
        '''Build number for the current session's locale. Typically, this is a small number
        reflecting a localization change from the normal product build.
        '''
        return self.data['localeBuild']

    @property
    def localeVersion(self):
        '''Version of the message catalog for the current session's locale.
        '''
        return self.data['localeVersion']

    @property
    def name(self):
        '''Short form of the product name.
        '''
        return self.data['name']

    @property
    def osType(self):
        '''Operating system type and architecture.
        '''
        return self.data['osType']

    @property
    def productLineId(self):
        '''The product ID is a unique identifier for a product line.
        '''
        return self.data['productLineId']

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

