
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LicenseFeatureInfo(DynamicData):
    '''A single feature that can be licensed. This information is immutable.
    '''
    
    def __init__(self, costUnit, dependentKey, edition, expiresOn, featureDescription, featureName, key, sourceRestriction, state):
        # MUST define these
        super(LicenseFeatureInfo, self).__init__()
    
        self.data['costUnit'] = costUnit
        self.data['dependentKey'] = dependentKey
        self.data['edition'] = edition
        self.data['expiresOn'] = expiresOn
        self.data['featureDescription'] = featureDescription
        self.data['featureName'] = featureName
        self.data['key'] = key
        self.data['sourceRestriction'] = sourceRestriction
        self.data['state'] = state
    
    
    @property
    def costUnit(self):
        '''Each license has a cost associated with it and the value of costUnit specifies the
        applicable unit.
        '''
        return self.data['costUnit']

    @property
    def dependentKey(self):
        '''Report List of feature keys used by this edition.
        '''
        return self.data['dependentKey']

    @property
    def edition(self):
        '''Flag to indicate whether the feature is an edition.
        '''
        return self.data['edition']

    @property
    def expiresOn(self):
        '''Date representing the expiration date
        '''
        return self.data['expiresOn']

    @property
    def featureDescription(self):
        '''A human readable description of what function this feature enables.
        '''
        return self.data['featureDescription']

    @property
    def featureName(self):
        '''The display string for the feature name.
        '''
        return self.data['featureName']

    @property
    def key(self):
        '''Unique identifier for license as defined in License source data. Max length of
        this string is 64 characters of ASCII/ISO Latin-1 character set.
        '''
        return self.data['key']

    @property
    def sourceRestriction(self):
        '''Describe any restriction on the source of a license for this feature.
        '''
        return self.data['sourceRestriction']

    @property
    def state(self):
        '''Describes the state of the feature based on the current edition license. This
        property is unset for an edition license.
        '''
        return self.data['state']

