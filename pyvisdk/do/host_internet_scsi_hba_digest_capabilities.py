
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostInternetScsiHbaDigestCapabilities(DynamicData):
    '''The digest capabilities for this host bus adapter.
    '''
    
    def __init__(self, dataDigestSettable, headerDigestSettable, targetDataDigestSettable, targetHeaderDigestSettable):
        # MUST define these
        super(HostInternetScsiHbaDigestCapabilities, self).__init__()
    
        self.data['dataDigestSettable'] = dataDigestSettable
        self.data['headerDigestSettable'] = headerDigestSettable
        self.data['targetDataDigestSettable'] = targetDataDigestSettable
        self.data['targetHeaderDigestSettable'] = targetHeaderDigestSettable
    
    
    @property
    def dataDigestSettable(self):
        '''True if this host bus adapter supports the configuration of the use of data
        digest. Defaults to false, in which case no data digests will be used.
        '''
        return self.data['dataDigestSettable']

    @property
    def headerDigestSettable(self):
        '''True if this host bus adapter supports the configuration of the use of header
        digest. Defaults to false, in which case no header digests will be used.
        '''
        return self.data['headerDigestSettable']

    @property
    def targetDataDigestSettable(self):
        '''True if configuration of the use of data digest is supported on the targets
        associated with the host bus adapter. Defaults to false, in which case no
        data digests will be used.
        '''
        return self.data['targetDataDigestSettable']

    @property
    def targetHeaderDigestSettable(self):
        '''True if configuration of the use of header digest is supported on the targets
        associated with the host bus adapter. Defaults to false, in which case no
        header digests will be used.
        '''
        return self.data['targetHeaderDigestSettable']

