
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LicenseManager(BaseEntity):
    '''This managed object type controls entitlements for a given VMware platform. VMware
        platforms include VirtualCenter, ESX Server, VMware Server, Workstation
        and Player. Entitlements define what software capabilities this host may
        use.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.LicenseManager):
        # MUST define these
        super(LicenseManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def diagnostics(self):
        '''
        Return current diagnostic information.
        '''
        return self.update('diagnostics')

    @property
    def evaluation(self):
        '''
        vSphere API 4.0
        '''
        return self.update('evaluation')

    @property
    def featureInfo(self):
        '''
        The list of features that can be licensed.
        '''
        return self.update('featureInfo')

    @property
    def licenseAssignmentManager(self):
        '''
        License Assignment Manager
        '''
        return self.update('licenseAssignmentManager')

    @property
    def licensedEdition(self):
        '''
        The product's license edition. The edition defines which product license the
        server requires. This, in turn, determines the core set of functionalities
        provided by the product and the additional features that can be licensed.
        If no edition is set the property is set to the empty string (""). To set
        the edition use SetLicenseEdition.
        '''
        return self.update('licensedEdition')

    @property
    def licenses(self):
        '''
        Get information about all the licenses avaiable.
        '''
        return self.update('licenses')

    @property
    def source(self):
        '''
        Set or return a data object type of LocalLicense or LicenseServer.
        '''
        return self.update('source')

    @property
    def sourceAvailable(self):
        '''
        Current state of the license source. License sources that are LocalSource are
        always available.
        '''
        return self.update('sourceAvailable')


    def QueryLicenseSourceAvailability(self):
        '''Deprecated. As of vSphere API 4.0, use QueryAssignedLicenses instead. Queries the
        current license source for total and available licenses available for each
        feature known to this system.

        :rtype: LicenseAvailabilityInfo[] 

        '''
        
        return self.delegate("QueryLicenseSourceAvailability")()
        

    def DecodeLicense(self, licenseKey):
        '''Decodes licensing information on the license specified.

        :param licenseKey: A license. E.g. a serial license.


        :rtype: LicenseManagerLicenseInfo 

        '''
        
        return self.delegate("DecodeLicense")(licenseKey)
        

    def RemoveLicense(self, licenseKey):
        '''Remove license from the available set.

        :param licenseKey: A licenses. E.g. a serial license.

        '''
        
        return self.delegate("RemoveLicense")(licenseKey)
        

    def UpdateLicense(self, licenseKey):
        '''Updates the available licenses to the one provided in licenseKey. This is the same
        as removing all the licenses using RemoveLicense and adding licenseKey
        using AddLicense If the optional parameter labels is specify this is the
        same as calling updateLicense without the optioal parameter and calling
        updateLabel for each pair in the labels array.

        :param licenseKey: A license. E.g. a serial license.


        :rtype: LicenseManagerLicenseInfo 

        '''
        
        return self.delegate("UpdateLicense")(licenseKey)
        

    def CheckLicenseFeature(self):
        '''Deprecated. As of vSphere API 4.0, use QueryAssignedLicenses instead. Returns
        whether or not a given feature is enabled.

        :rtype: xsd:boolean 

        '''
        
        return self.delegate("CheckLicenseFeature")()
        

    def QuerySupportedFeatures(self):
        '''Deprecated. As of vSphere API 4.0, use QueryAssignedLicenses instead. Queries the
        current license source for a list of available licenses that can be
        licensed from this system.

        :rtype: LicenseFeatureInfo[] 

        '''
        
        return self.delegate("QuerySupportedFeatures")()
        

    def QueryLicenseUsage(self):
        '''Deprecated. As of vSphere API 4.0, use QueryAssignedLicenses instead. Returns the
        license usage. The license usage is a list of supported features and the
        number of licenses that have been reserved.

        :rtype: LicenseUsageInfo 

        '''
        
        return self.delegate("QueryLicenseUsage")()
        

    def AddLicense(self, licenseKey):
        '''Adds a license to the inventory of available licenses.

        :param licenseKey: A license. E.g. a serial license.


        :rtype: LicenseManagerLicenseInfo 

        '''
        
        return self.delegate("AddLicense")(licenseKey)
        

    def DisableFeature(self):
        '''Deprecated. As of vSphere API 4.0, use RemoveAssignedLicense instead. Release
        licenses for an optional feature.

        :rtype: xsd:boolean 

        '''
        
        return self.delegate("DisableFeature")()
        

    def SetLicenseEdition(self):
        '''Deprecated. As of vSphere API 4.0, use QueryAssignedLicenses instead. Defines the
        product's license edition. The edition defines which product license the
        server requires. This, in turn, determines the core set of functionality
        provided by the product and the additional features that can be licensed.
        '''
        
        return self.delegate("SetLicenseEdition")()
        

    def RemoveLicenseLabel(self, licenseKey, labelKey):
        '''Removed a license's label.

        :param licenseKey: A license.

        :param labelKey: A label key.

        '''
        
        return self.delegate("RemoveLicenseLabel")(licenseKey,labelKey)
        

    def ConfigureLicenseSource(self):
        '''Deprecated. As of vSphere API 4.0, use UpdateLicense instead. Allows for
        reconfiguration of the License Manager license source.
        '''
        
        return self.delegate("ConfigureLicenseSource")()
        

    def UpdateLicenseLabel(self, labelValue, licenseKey, labelKey):
        '''Update a license's label. It creates a label entry if the labelKey doesn't already
        exist

        :param labelValue: Value for the label.

        :param licenseKey: A license.

        :param labelKey: A label key.

        '''
        
        return self.delegate("UpdateLicenseLabel")(labelValue,licenseKey,labelKey)
        

    def EnableFeature(self):
        '''Deprecated. As of vSphere API 4.0, use UpdateAssignedLicense instead. Enable a
        feature that has an optional state.

        :rtype: xsd:boolean 

        '''
        
        return self.delegate("EnableFeature")()
        
