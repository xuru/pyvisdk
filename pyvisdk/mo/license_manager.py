
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LicenseManager(BaseEntity):
    '''This managed object type controls entitlements for a given VMware platform.
    VMware platforms include VirtualCenter, ESX Server, VMware Server, Workstation
    and Player. Entitlements define what software capabilities this host may
    use.Entitlements are identified by a short string 'key'. Keys can represent
    either a particular edition (Full, Starter) or a particular feature/function
    (featureKey) (backup, nas). An edition implies zero one or more functions which
    are express, denied or optional. For example a 'Full' edition includes 'iscsi'
    function but a Starter edition might disallow it.Which edition a given VMware
    platform uses can be defined at any time. Generally this is done right after
    first install and boot as installation software may not set it. For editions
    that are similar in nature, any future changes to edition type will only impact
    future requests for functionality. Current functionality is left unaffected.
    The same is true for optional functions enabled/disabled after some period of
    time. For dissimilar editions, such transitions may require entering
    maintenance mode first else an exception of InvalidState will be thrown.To
    specify the edition type and any optional functions, use updateLicense for ESX
    Server and addLicense follow by LicenseAssingmentManager.updateAssignedLicense
    for VirtualCenter.When an edition is specified for a given host, the cost of
    that edition (how many licenses are needed) is determined. The cost is computed
    using the license's CostUnit value multiplied by the number of units activated.
    For example, when a VMware platform is set to an edition which uses a
    'cpuPackage' on a two socket server, two licenses would be needed to
    successfully install that edition.Here is a diagram of the unit costs supported
    by this API and their relationships.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.LicenseManager):
        super(LicenseManager, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def diagnostics(self):
        '''Return current diagnostic information.'''
        return self.update('diagnostics')
    @property
    def evaluation(self):
        '''vSphere API 4.0'''
        return self.update('evaluation')
    @property
    def featureInfo(self):
        '''The list of features that can be licensed.'''
        return self.update('featureInfo')
    @property
    def licenseAssignmentManager(self):
        '''License Assignment Manager'''
        return self.update('licenseAssignmentManager')
    @property
    def licensedEdition(self):
        '''The product's license edition. The edition defines which product license the
        server requires. This, in turn, determines the core set of functionalities
        provided by the product and the additional features that can be licensed. If no
        edition is set the property is set to the empty string (""). To set the edition
        use SetLicenseEdition.'''
        return self.update('licensedEdition')
    @property
    def licenses(self):
        '''Get information about all the licenses avaiable.'''
        return self.update('licenses')
    @property
    def source(self):
        '''Set or return a data object type of LocalLicense or LicenseServer.'''
        return self.update('source')
    @property
    def sourceAvailable(self):
        '''Current state of the license source. License sources that are LocalSource are
        always available.'''
        return self.update('sourceAvailable')

    
    
    def AddLicense(self, licenseKey, labels=None):
        '''Adds a license to the inventory of available licenses.
        
        :param licenseKey: A license. E.g. a serial license.
        
        :param labels: array of key-value labels. Ignored by ESX Server.
        
        '''
        return self.delegate("AddLicense")(licenseKey, labels)
    
    def CheckLicenseFeature(self, featureKey, host=None):
        '''<b>Deprecated.</b> <i>As of vSphere API 4.0, use QueryAssignedLicenses
        instead.</i> Returns whether or not a given feature is enabled.
        
        :param host: Host to act on if LicenseManager is not on a host.
        
        :param featureKey: Name of the feature to enable.
        
        '''
        return self.delegate("CheckLicenseFeature")(host, featureKey)
    
    def ConfigureLicenseSource(self, licenseSource, host=None):
        '''<b>Deprecated.</b> <i>As of vSphere API 4.0, use UpdateLicense instead.</i>
        Allows for reconfiguration of the License Manager license source.
        
        :param host: Host for which the license manager should be reconfigured.
        
        :param licenseSource: ServedSource or LocalSource.
        
        '''
        return self.delegate("ConfigureLicenseSource")(host, licenseSource)
    
    def DecodeLicense(self, licenseKey):
        '''Decodes licensing information on the license specified.
        
        :param licenseKey: A license. E.g. a serial license.
        
        '''
        return self.delegate("DecodeLicense")(licenseKey)
    
    def DisableFeature(self, featureKey, host=None):
        '''<b>Deprecated.</b> <i>As of vSphere API 4.0, use RemoveAssignedLicense
        instead.</i> Release licenses for an optional feature.
        
        :param host: Host to act on if LicenseManager is not on a host.
        
        :param featureKey: key of the feature to disable.
        
        '''
        return self.delegate("DisableFeature")(host, featureKey)
    
    def EnableFeature(self, featureKey, host=None):
        '''<b>Deprecated.</b> <i>As of vSphere API 4.0, use UpdateAssignedLicense
        instead.</i> Enable a feature that has an optional state.
        
        :param host: Host to act on if LicenseManager is not on a host.
        
        :param featureKey: Name of the feature to enable.
        
        '''
        return self.delegate("EnableFeature")(host, featureKey)
    
    def QueryLicenseSourceAvailability(self, host=None):
        '''<b>Deprecated.</b> <i>As of vSphere API 4.0, use QueryAssignedLicenses
        instead.</i> Queries the current license source for total and available
        licenses available for each feature known to this system.
        
        :param host: Use the license source of the specified host.
        
        '''
        return self.delegate("QueryLicenseSourceAvailability")(host)
    
    def QueryLicenseUsage(self, host=None):
        '''<b>Deprecated.</b> <i>As of vSphere API 4.0, use QueryAssignedLicenses
        instead.</i> Returns the license usage. The license usage is a list of
        supported features and the number of licenses that have been reserved.
        
        :param host: Host to query for usage. If missing, query the server the LicenseManager is on.
        
        '''
        return self.delegate("QueryLicenseUsage")(host)
    
    def QuerySupportedFeatures(self, host=None):
        '''<b>Deprecated.</b> <i>As of vSphere API 4.0, use QueryAssignedLicenses
        instead.</i> Queries the current license source for a list of available
        licenses that can be licensed from this system.
        
        :param host: Use the license source of the specified host.
        
        '''
        return self.delegate("QuerySupportedFeatures")(host)
    
    def RemoveLicense(self, licenseKey):
        '''Remove license from the available set.
        
        :param licenseKey: A licenses. E.g. a serial license.
        
        '''
        return self.delegate("RemoveLicense")(licenseKey)
    
    def RemoveLicenseLabel(self, licenseKey, labelKey):
        '''Removed a license's label.
        
        :param licenseKey: A license.
        
        :param labelKey: A label key.
        
        '''
        return self.delegate("RemoveLicenseLabel")(licenseKey, labelKey)
    
    def SetLicenseEdition(self, host=None, featureKey=None):
        '''<b>Deprecated.</b> <i>As of vSphere API 4.0, use QueryAssignedLicenses
        instead.</i> Defines the product's license edition. The edition defines which
        product license the server requires. This, in turn, determines the core set of
        functionality provided by the product and the additional features that can be
        licensed.
        
        :param host: Host to act on if LicenseManager is not on a host.
        
        :param featureKey: Name of edition feature to select. If featureKey is not set or set to empty string, the product becomes unlicensed.
        
        '''
        return self.delegate("SetLicenseEdition")(host, featureKey)
    
    def UpdateLicense(self, licenseKey, labels=None):
        '''Updates the available licenses to the one provided in licenseKey. This is the
        same as removing all the licenses using RemoveLicense and adding licenseKey
        using AddLicense If the optional parameter labels is specify this is the same
        as calling updateLicense without the optioal parameter and calling updateLabel
        for each pair in the labels array.
        
        :param licenseKey: A license. E.g. a serial license.
        
        :param labels: array of key-value labels.
        
        '''
        return self.delegate("UpdateLicense")(licenseKey, labels)
    
    def UpdateLicenseLabel(self, licenseKey, labelKey, labelValue):
        '''Update a license's label. It creates a label entry if the labelKey doesn't
        already exist
        
        :param licenseKey: A license.
        
        :param labelKey: A label key.
        
        :param labelValue: Value for the label.
        
        '''
        return self.delegate("UpdateLicenseLabel")(licenseKey, labelKey, labelValue)