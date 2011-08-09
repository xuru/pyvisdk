
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostConnectSpec(DynamicData):
    '''Specifies the parameters needed to add a single host. This includes a small set of
        optional information about the host configuration. This allows the network
        and datastore configuration of the host to be synchronized with the naming
        conventions of the datacenter, as well as the configuration of a vim
        account (the username/password for the virtual machine files that is
        created on disk).
    '''
    
    def __init__(self, force, hostName, managementIp, password, port, sslThumbprint, userName, vimAccountName, vimAccountPassword, vmFolder):
        # MUST define these
        super(HostConnectSpec, self).__init__()
    
        self.data['force'] = force
        self.data['hostName'] = hostName
        self.data['managementIp'] = managementIp
        self.data['password'] = password
        self.data['port'] = port
        self.data['sslThumbprint'] = sslThumbprint
        self.data['userName'] = userName
        self.data['vimAccountName'] = vimAccountName
        self.data['vimAccountPassword'] = vimAccountPassword
        self.data['vmFolder'] = vmFolder
    
    
    @property
    def force(self):
        '''If this flag is set to "true", then the connection succeeds even if the host is
        already being managed by another VirtualCenter server. The original
        VirtualCenter server loses connection to the host.
        '''
        return self.data['force']

    @property
    def hostName(self):
        '''The DNS name or IP address of the host. (Required for adding a host.)
        '''
        return self.data['hostName']

    @property
    def managementIp(self):
        '''The IP address of the VirtualCenter server that will manage this host. This field
        can be used to control which IP address the VirtualCenter agent will send
        heartbeats to. If it is not set, VirtualCenter will use the local IP
        address used when communicating with the host. Setting this field is
        useful when the VirtualCenter server is behind a NAT in which case the
        external NAT address must be used.
        '''
        return self.data['managementIp']

    @property
    def password(self):
        '''The password for the administration account. (Required for adding a host.)
        '''
        return self.data['password']

    @property
    def port(self):
        '''The port number for the connection. If this is not specified, the default port
        number is used. For ESX 2.x hosts this is the authd port (902 by default).
        For ESX 3.x and above and VMware Server hosts this is the https port (443
        by default). If this is a reconnect, the port number is unchanged.
        '''
        return self.data['port']

    @property
    def sslThumbprint(self):
        '''The thumbprint of the SSL certificate, which the host is expected to have. If this
        value is set and matches the certificate thumbprint presented by the host,
        then the host is authenticated. If this value is not set or does not match
        the certificate thumbprint presented by the host, then the host's
        certificate is verified by checking whether it was signed by a recognized
        CA.
        '''
        return self.data['sslThumbprint']

    @property
    def userName(self):
        '''The administration account on the host. (Required for adding a host.)
        '''
        return self.data['userName']

    @property
    def vimAccountName(self):
        '''The username to be used for accessing the virtual machine files on the disk.
        '''
        return self.data['vimAccountName']

    @property
    def vimAccountPassword(self):
        '''The password to be used with the vimAccountName property for accessing the virtual
        machine files on the disk.
        '''
        return self.data['vimAccountPassword']

    @property
    def vmFolder(self):
        '''The folder in which to store the existing virtual machines on the host. If this
        folder is not specified, a default folder is chosen (and possibly created)
        by the VirtualCenter. This folder exists (or is possibly created) on the
        VirtualCenter server and is called "Discovered VM".
        '''
        return self.data['vmFolder']

