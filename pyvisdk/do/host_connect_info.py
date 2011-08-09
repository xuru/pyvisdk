
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostConnectInfo(DynamicData):
    '''This data object type contains information about a single host that can be used by
        the connection wizard. This can be returned without adding the host to
        VirtualCenter.
    '''
    
    def __init__(self, clusterSupported, datastore, host, license, network, serverIp, vimAccountNameRequired, vm):
        # MUST define these
        super(HostConnectInfo, self).__init__()
    
        self.data['clusterSupported'] = clusterSupported
        self.data['datastore'] = datastore
        self.data['host'] = host
        self.data['license'] = license
        self.data['network'] = network
        self.data['serverIp'] = serverIp
        self.data['vimAccountNameRequired'] = vimAccountNameRequired
        self.data['vm'] = vm
    
    
    @property
    def clusterSupported(self):
        '''Whether or not the host supports clustering capabilities such as HA or DRS and
        therefore can be added to a cluster. If false, the host must be added as a
        standalone host.
        '''
        return self.data['clusterSupported']

    @property
    def datastore(self):
        '''The list of datastores on the host.
        '''
        return self.data['datastore']

    @property
    def host(self):
        '''Summary information about the host. The status fields and managed object reference
        is not set when an object of this type is created. These fields and
        references are typically set later when these objects are associated with
        a host.
        '''
        return self.data['host']

    @property
    def license(self):
        '''License manager information on the host
        '''
        return self.data['license']

    @property
    def network(self):
        '''The list of network information for networks configured on this host.
        '''
        return self.data['network']

    @property
    def serverIp(self):
        '''The IP address of the VirtualCenter already managing this host, if any.
        '''
        return self.data['serverIp']

    @property
    def vimAccountNameRequired(self):
        '''Whether or not the host requires a vimAccountName and password to be set in the
        ConnectSpec. This is normally only required for VMware Server hosts.
        '''
        return self.data['vimAccountNameRequired']

    @property
    def vm(self):
        '''The list of virtual machines on the host.
        '''
        return self.data['vm']

