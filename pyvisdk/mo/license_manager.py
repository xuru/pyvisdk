
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
        use.Entitlements are identified by a short string 'key'. Keys can
        represent either a particular edition (Full, Starter) or a particular
        feature/function (featureKey) (backup, nas). An edition implies zero one
        or more functions which are express, denied or optional. For example a
        'Full' edition includes 'iscsi' function but a Starter edition might
        disallow it.Which edition a given VMware platform uses can be defined at
        any time. Generally this is done right after first install and boot as
        installation software may not set it. For editions that are similar in
        nature, any future changes to edition type will only impact future
        requests for functionality. Current functionality is left unaffected. The
        same is true for optional functions enabled/disabled after some period of
        time. For dissimilar editions, such transitions may require entering
        maintenance mode first else an exception of InvalidState will be thrown.To
        specify the edition type and any optional functions, use updateLicense for
        ESX Server and addLicense follow by
        LicenseAssingmentManager.updateAssignedLicense for VirtualCenter.When an
        edition is specified for a given host, the cost of that edition (how many
        licenses are needed) is determined. The cost is computed using the
        license's CostUnit value multiplied by the number of units activated. For
        example, when a VMware platform is set to an edition which uses a
        'cpuPackage' on a two socket server, two licenses would be needed to
        successfully install that edition.Here is a diagram of the unit costs
        supported by this API and their relationships.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.LicenseManager):
        # MUST define these
        super(LicenseManager, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def diagnostics(self):
        '''Return current diagnostic information.
        '''
        return self.update('diagnostics')

    @property
    def evaluation(self):
        '''vSphere API 4.0
        '''
        return self.update('evaluation')

    @property
    def featureInfo(self):
        '''The list of features that can be licensed.
        '''
        return self.update('featureInfo')

    @property
    def licenseAssignmentManager(self):
        '''License Assignment Manager
        '''
        return self.update('licenseAssignmentManager')

    @property
    def licensedEdition(self):
        '''The product's license edition. The edition defines which product license the
        server requires. This, in turn, determines the core set of functionalities
        provided by the product and the additional features that can be licensed.
        If no edition is set the property is set to the empty string (""). To set
        the edition use SetLicenseEdition.
        '''
        return self.update('licensedEdition')

    @property
    def licenses(self):
        '''Get information about all the licenses avaiable.
        '''
        return self.update('licenses')

    @property
    def source(self):
        '''Set or return a data object type of LocalLicense or LicenseServer.
        '''
        return self.update('source')

    @property
    def sourceAvailable(self):
        '''Current state of the license source. License sources that are LocalSource are
        always available.
        '''
        return self.update('sourceAvailable')


    def AddLicense(self, licenseKey, labelKey, labelValue):
        '''Adds a license to the inventory of available licenses.

        :param licenseKey: A license.

        :param labelKey: A label key.

        :param labelValue: Value for the label.

        '''
        
        return self.delegate("AddLicense")(licenseKey,labelKey,labelValue)
        

    def CheckLicenseFeature(self, licenseKey, labelKey, labelValue):
        '''Deprecated. As of vSphere API 4.0, use QueryAssignedLicenses instead. Returns
        whether or not a given feature is enabled.

        :param licenseKey: A license.

        :param labelKey: A label key.

        :param labelValue: Value for the label.

        '''
        
        return self.delegate("CheckLicenseFeature")(licenseKey,labelKey,labelValue)
        

    def ConfigureLicenseSource(self, licenseKey, labelKey, labelValue):
        '''Deprecated. As of vSphere API 4.0, use UpdateLicense instead. Allows for
        reconfiguration of the License Manager license source.

        :param licenseKey: A license.

        :param labelKey: A label key.

        :param labelValue: Value for the label.

        '''
        
        return self.delegate("ConfigureLicenseSource")(licenseKey,labelKey,labelValue)
        

    def DecodeLicense(self, licenseKey, labelKey, labelValue):
        '''Decodes licensing information on the license specified.

        :param licenseKey: A license.

        :param labelKey: A label key.

        :param labelValue: Value for the label.

        '''
        
        return self.delegate("DecodeLicense")(licenseKey,labelKey,labelValue)
        

    def DisableFeature(self, licenseKey, labelKey, labelValue):
        '''Deprecated. As of vSphere API 4.0, use RemoveAssignedLicense instead. Release
        licenses for an optional feature.

        :param licenseKey: A license.

        :param labelKey: A label key.

        :param labelValue: Value for the label.

        '''
        
        return self.delegate("DisableFeature")(licenseKey,labelKey,labelValue)
        

    def EnableFeature(self, licenseKey, labelKey, labelValue):
        '''Deprecated. As of vSphere API 4.0, use UpdateAssignedLicense instead. Enable a
        feature that has an optional state.

        :param licenseKey: A license.

        :param labelKey: A label key.

        :param labelValue: Value for the label.

        '''
        
        return self.delegate("EnableFeature")(licenseKey,labelKey,labelValue)
        

    def QueryLicenseSourceAvailability(self, licenseKey, labelKey, labelValue):
        '''Deprecated. As of vSphere API 4.0, use QueryAssignedLicenses instead. Queries the
        current license source for total and available licenses available for each
        feature known to this system.

        :param licenseKey: A license.

        :param labelKey: A label key.

        :param labelValue: Value for the label.

        '''
        
        return self.delegate("QueryLicenseSourceAvailability")(licenseKey,labelKey,labelValue)
        

    def QueryLicenseUsage(self, licenseKey, labelKey, labelValue):
        '''Deprecated. As of vSphere API 4.0, use QueryAssignedLicenses instead. Returns the
        license usage. The license usage is a list of supported features and the
        number of licenses that have been reserved.

        :param licenseKey: A license.

        :param labelKey: A label key.

        :param labelValue: Value for the label.

        '''
        
        return self.delegate("QueryLicenseUsage")(licenseKey,labelKey,labelValue)
        

    def QuerySupportedFeatures(self, licenseKey, labelKey, labelValue):
        '''Deprecated. As of vSphere API 4.0, use QueryAssignedLicenses instead. Queries the
        current license source for a list of available licenses that can be
        licensed from this system.

        :param licenseKey: A license.

        :param labelKey: A label key.

        :param labelValue: Value for the label.

        '''
        
        return self.delegate("QuerySupportedFeatures")(licenseKey,labelKey,labelValue)
        

    def RemoveLicense(self, licenseKey, labelKey, labelValue):
        '''Remove license from the available set.

        :param licenseKey: A license.

        :param labelKey: A label key.

        :param labelValue: Value for the label.

        '''
        
        return self.delegate("RemoveLicense")(licenseKey,labelKey,labelValue)
        

    def RemoveLicenseLabel(self, licenseKey, labelKey, labelValue):
        '''Removed a license's label.

        :param licenseKey: A license.

        :param labelKey: A label key.

        :param labelValue: Value for the label.

        '''
        
        return self.delegate("RemoveLicenseLabel")(licenseKey,labelKey,labelValue)
        

    def SetLicenseEdition(self, licenseKey, labelKey, labelValue):
        '''Deprecated. As of vSphere API 4.0, use QueryAssignedLicenses instead. Defines the
        product's license edition. The edition defines which product license the
        server requires. This, in turn, determines the core set of functionality
        provided by the product and the additional features that can be licensed.

        :param licenseKey: A license.

        :param labelKey: A label key.

        :param labelValue: Value for the label.

        '''
        
        return self.delegate("SetLicenseEdition")(licenseKey,labelKey,labelValue)
        

    def UpdateLicense(self, licenseKey, labelKey, labelValue):
        '''Updates the available licenses to the one provided in licenseKey. This is the same
        as removing all the licenses using RemoveLicense and adding licenseKey
        using AddLicense If the optional parameter labels is specify this is the
        same as calling updateLicense without the optioal parameter and calling
        updateLabel for each pair in the labels array.

        :param licenseKey: A license.

        :param labelKey: A label key.

        :param labelValue: Value for the label.

        '''
        
        return self.delegate("UpdateLicense")(licenseKey,labelKey,labelValue)
        

    def UpdateLicenseLabel(self, licenseKey, labelKey, labelValue):
        '''Update a license's label. It creates a label entry if the labelKey doesn't already
        exist

        :param licenseKey: A license.

        :param labelKey: A label key.

        :param labelValue: Value for the label.

        '''
        
        return self.delegate("UpdateLicenseLabel")(licenseKey,labelKey,labelValue)
        
