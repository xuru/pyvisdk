
from pyvisdk.do.dynamic_data import DynamicData
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class DiagnosticManagerBundleInfo(DynamicData):
    '''Describes a location of a diagnostic bundle and the server to which it belongs.
        This is a return type for the generateLogBundles operation.
    '''
    
    def __init__(self, system, url):
        # MUST define these
        super(DiagnosticManagerBundleInfo, self).__init__()
    
        self.data['system'] = system
        self.data['url'] = url
    
    
    @property
    def system(self):
        '''The host to which this diagnostic bundle belongs. If this is for the default
        server, then it is not set.
        '''
        return self.data['system']

    @property
    def url(self):
        '''The location from which the diagnostic bundle can be downloaded. The host part of
        the URL is returned as '*' if the hostname to be used is the name of the
        server to which the call was made. For example, if the call is made to
        vcsrv1.domain1.com, and the bundle is available for download from
        http://vcsrv1.domain1.com/diagnostics/bundle.zip, the URL returned may be
        http:// * /diagnostics/bundle.zip. The client replaces the asterisk with
        the server name on which it invoked the call.
        '''
        return self.data['url']

