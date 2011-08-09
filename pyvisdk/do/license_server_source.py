
from pyvisdk.do.license_source import LicenseSource
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class LicenseServerSource(LicenseSource):
    '''Specify a license server reachable via IPv4 network.
    '''
    
    def __init__(self, licenseServer):
        # MUST define these
        super(LicenseServerSource, self).__init__()
    
        self.data['licenseServer'] = licenseServer
    
    
    @property
    def licenseServer(self):
        '''This property defines the server to establish a TCP session to obtain license
        data. Format of string is host:port Port is optional unsigned 16 bit
        integer license server is listening on. A trailing colon ':' without a
        port number is a valid expression. Host can either be an IPv4 address in
        dotted quad format or a resolvable DNS name <=254 characters. See RFC
        3696.
        '''
        return self.data['licenseServer']

