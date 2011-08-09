
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DatastoreSummary(DynamicData):
    '''Summary information about the datastore. The status fields and managed object
        reference is not set when an object of this type is created. These fields
        and references are typically set later when these objects are associated
        with a host.
    '''
    
    def __init__(self, accessible, capacity, datastore, freeSpace, multipleHostAccess, name, type, uncommitted, url):
        # MUST define these
        super(DatastoreSummary, self).__init__()
    
        self.data['accessible'] = accessible
        self.data['capacity'] = capacity
        self.data['datastore'] = datastore
        self.data['freeSpace'] = freeSpace
        self.data['multipleHostAccess'] = multipleHostAccess
        self.data['name'] = name
        self.data['type'] = type
        self.data['uncommitted'] = uncommitted
        self.data['url'] = url
    
    
    @property
    def accessible(self):
        '''The connectivity status of this datastore. If this is set to false, meaning the
        datastore is not accessible, this datastore's capacity and freespace
        properties cannot be validated. Furthermore, if this property is set to
        false, some of the properties in this summary and in DatastoreInfo should
        not be used. Refer to the documentation for the property of your interest.
        '''
        return self.data['accessible']

    @property
    def capacity(self):
        '''Maximum capacity of this datastore, in bytes. This value is updated periodically
        by the server. It can be explicitly refreshed with the Refresh operation.
        This property is guaranteed to be valid only if accessible is true.
        '''
        return self.data['capacity']

    @property
    def datastore(self):
        '''The reference to the managed object.
        '''
        return self.data['datastore']

    @property
    def freeSpace(self):
        '''Available space of this datastore, in bytes. The server periodically updates this
        value. It can be explicitly refreshed with the Refresh operation. This
        property is guaranteed to be valid only if accessible is true.
        '''
        return self.data['freeSpace']

    @property
    def multipleHostAccess(self):
        '''More than one host in the datacenter has been configured with access to the
        datastore. This is only provided by VirtualCenter.
        '''
        return self.data['multipleHostAccess']

    @property
    def name(self):
        '''The name of the datastore.
        '''
        return self.data['name']

    @property
    def type(self):
        '''Type of file system volume, such as VMFS or NFS.
        '''
        return self.data['type']

    @property
    def uncommitted(self):
        '''Total additional storage space, in bytes, potentially used by all virtual machines
        on this datastore. The server periodically updates this value. It can be
        explicitly refreshed with the RefreshDatastoreStorageInfo operation. This
        property is valid only if accessible is true.
        '''
        return self.data['uncommitted']

    @property
    def url(self):
        '''The unique locator for the datastore. This property is guaranteed to be valid only
        if accessible is true.
        '''
        return self.data['url']

