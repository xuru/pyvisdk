
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LicenseManagerLicenseInfo(DynamicData):
    '''Encapsulates information about a license
    '''
    
    def __init__(self, costUnit, editionKey, labels, licenseKey, name, properties, total, used):
        # MUST define these
        super(LicenseManagerLicenseInfo, self).__init__()
    
        self.data['costUnit'] = costUnit
        self.data['editionKey'] = editionKey
        self.data['labels'] = labels
        self.data['licenseKey'] = licenseKey
        self.data['name'] = name
        self.data['properties'] = properties
        self.data['total'] = total
        self.data['used'] = used
    
    
    @property
    def costUnit(self):
        '''The cost unit for this license
        '''
        return self.data['costUnit']

    @property
    def editionKey(self):
        '''Edition key.
        '''
        return self.data['editionKey']

    @property
    def labels(self):
        '''Key-value lables for this license
        '''
        return self.data['labels']

    @property
    def licenseKey(self):
        '''Key for the license. E.g. serial number.
        '''
        return self.data['licenseKey']

    @property
    def name(self):
        '''Display name for the license
        '''
        return self.data['name']

    @property
    def properties(self):
        '''Additional properties associated with this license
        '''
        return self.data['properties']

    @property
    def total(self):
        '''Total number of units contain in the license
        '''
        return self.data['total']

    @property
    def used(self):
        '''Number of units used from this license
        '''
        return self.data['used']

