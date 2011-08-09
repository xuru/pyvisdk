
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualMachineTicket(DynamicData):
    '''This data object contains the information needed to establish a connection to a
        running virtual machine.
    '''
    
    def __init__(self, cfgFile, host, port, sslThumbprint, ticket):
        # MUST define these
        super(VirtualMachineTicket, self).__init__()
    
        self.data['cfgFile'] = cfgFile
        self.data['host'] = host
        self.data['port'] = port
        self.data['sslThumbprint'] = sslThumbprint
        self.data['ticket'] = ticket
    
    
    @property
    def cfgFile(self):
        '''The name of the configuration file for the virtual machine.
        '''
        return self.data['cfgFile']

    @property
    def host(self):
        '''The host with which to establish a connection. If the host is not specified, it is
        assumed that the requesting entity knows the appropriate host with which
        to connect.
        '''
        return self.data['host']

    @property
    def port(self):
        '''The port number to use. If the port is not specified, it is assumed that the
        requesting entity knows the appropriate port to use when making a new
        connection.
        '''
        return self.data['port']

    @property
    def sslThumbprint(self):
        '''The expected thumbprint of the SSL cert of the host to which we are connecting.
        '''
        return self.data['sslThumbprint']

    @property
    def ticket(self):
        '''The ticket name. This is used as the username and password for the MKS connection.
        '''
        return self.data['ticket']

