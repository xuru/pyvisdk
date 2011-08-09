
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LicenseDiagnostics(DynamicData):
    '''This data object type provides summary status and diagnostic information for
        LicenseManager. Counters in this property can be reset to zero. The
        property specified as a discontinuity is used to determine when this last
        occurred.
    '''
    
    def __init__(self, lastStatusUpdate, licenseFeatureUnknowns, licenseRequestFailures, licenseRequests, opFailureMessage, opState, sourceLastChanged, sourceLatency, sourceLost):
        # MUST define these
        super(LicenseDiagnostics, self).__init__()
    
        self.data['lastStatusUpdate'] = lastStatusUpdate
        self.data['licenseFeatureUnknowns'] = licenseFeatureUnknowns
        self.data['licenseRequestFailures'] = licenseRequestFailures
        self.data['licenseRequests'] = licenseRequests
        self.data['opFailureMessage'] = opFailureMessage
        self.data['opState'] = opState
        self.data['sourceLastChanged'] = sourceLastChanged
        self.data['sourceLatency'] = sourceLatency
        self.data['sourceLost'] = sourceLost
    
    
    @property
    def lastStatusUpdate(self):
        '''A timestamp of when opState was last updated.
        '''
        return self.data['lastStatusUpdate']

    @property
    def licenseFeatureUnknowns(self):
        '''Counter to track Total number of license features parsed from License source that
        are not recognized. This value starts at zero and wraps at 2^32-1 to zero.
        Discontinuity: sourceLastChanged.
        '''
        return self.data['licenseFeatureUnknowns']

    @property
    def licenseRequestFailures(self):
        '''Counter to track Total number of licenses requests that were not fulfilled
        (denied, timeout, or other). This value starts at zero and wraps at 2^32-1
        to zero. Discontinuity: sourceLastChanged.
        '''
        return self.data['licenseRequestFailures']

    @property
    def licenseRequests(self):
        '''Counter to track total number of licenses requested. This value starts at zero and
        wraps at 2^32-1 to zero. Discontinuity: sourceLastChanged.
        '''
        return self.data['licenseRequests']

    @property
    def opFailureMessage(self):
        '''A human readable reason when optState reports Fault condition.
        '''
        return self.data['opFailureMessage']

    @property
    def opState(self):
        '''The general state of the license subsystem.
        '''
        return self.data['opState']

    @property
    def sourceLastChanged(self):
        '''A timestamp of when sourceAvailable last changed state, expressed in UTC.
        '''
        return self.data['sourceLastChanged']

    @property
    def sourceLatency(self):
        '''Exponentially decaying average of the transaction time for license acquisition and
        routine communications with LicenseSource. Units: milliseconds.
        '''
        return self.data['sourceLatency']

    @property
    def sourceLost(self):
        '''Counter to track number of times connection to source was lost. This value starts
        at zero and wraps at 2^32-1 to zero. Discontinuity: sourceLastChanged.
        '''
        return self.data['sourceLost']

