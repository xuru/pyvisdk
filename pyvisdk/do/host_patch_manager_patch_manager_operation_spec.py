
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class HostPatchManagerPatchManagerOperationSpec(DynamicData):
    '''Optional parameters for hostd to pass to exupdate.
    '''
    
    def __init__(self, cmdOption, password, port, proxy, userName):
        # MUST define these
        super(HostPatchManagerPatchManagerOperationSpec, self).__init__()
    
        self.data['cmdOption'] = cmdOption
        self.data['password'] = password
        self.data['port'] = port
        self.data['proxy'] = proxy
        self.data['userName'] = userName
    
    
    @property
    def cmdOption(self):
        '''Possible command line options when calling esxupdate.
        '''
        return self.data['cmdOption']

    @property
    def password(self):
        '''The password used for the proxy server. This is passed with ssl through a trusted
        channel.
        '''
        return self.data['password']

    @property
    def port(self):
        '''The port of the possible proxy for esxupdate to use to connect to a server. The
        patch and metadata may be cached within the proxy server.
        '''
        return self.data['port']

    @property
    def proxy(self):
        '''The name of the possible proxy for esxupdate to use to connect to a server. The
        patch and metadata may be cached within the proxy server.
        '''
        return self.data['proxy']

    @property
    def userName(self):
        '''The user name used for the proxy server.
        '''
        return self.data['userName']

