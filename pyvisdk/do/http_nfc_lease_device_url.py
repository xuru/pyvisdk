
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HttpNfcLeaseDeviceUrl(DynamicData):
    '''Provides a mapping from logical device IDs to upload/download URLs.For export, a
        single device id is returned based on the object identifiers for the
        objects.For import, two device ids are returned. One based on the object
        names used in the ImportSpec, and one based on the object identifiers for
        the created objects. This is immutable and would match the id if an
        ExportLease is latter created.
    '''
    
    def __init__(self, datastoreKey, disk, fileSize, importKey, key, sslThumbprint, targetId, url):
        # MUST define these
        super(HttpNfcLeaseDeviceUrl, self).__init__()
    
        self.data['datastoreKey'] = datastoreKey
        self.data['disk'] = disk
        self.data['fileSize'] = fileSize
        self.data['importKey'] = importKey
        self.data['key'] = key
        self.data['sslThumbprint'] = sslThumbprint
        self.data['targetId'] = targetId
        self.data['url'] = url
    
    
    @property
    def datastoreKey(self):
        '''Key for the datastore this disk is on. This is used to look up hosts which can be
        used to multi-POST disk contents, in the host map of the lease.
        '''
        return self.data['datastoreKey']

    @property
    def disk(self):
        '''Optional value to specify if the attached file is a disk in vmdk format.
        '''
        return self.data['disk']

    @property
    def fileSize(self):
        '''Specifies the size of the file backing for this device. This property is only set
        for non-disk file backings.
        '''
        return self.data['fileSize']

    @property
    def importKey(self):
        '''Identifies the device based on the names in an ImportSpec. This is only set for
        import leases.
        '''
        return self.data['importKey']

    @property
    def key(self):
        '''The immutable identifier for the device. This is set for both import/export
        leases.
        '''
        return self.data['key']

    @property
    def sslThumbprint(self):
        '''SSL thumbprint for the host the URL refers to. Empty if no SSL thumbprint is
        available or needed.
        '''
        return self.data['sslThumbprint']

    @property
    def targetId(self):
        '''Id for this target. This only used for multi-POSTing, where a single HTTP POST is
        applied to multiple targets.
        '''
        return self.data['targetId']

    @property
    def url(self):
        '''
        '''
        return self.data['url']

