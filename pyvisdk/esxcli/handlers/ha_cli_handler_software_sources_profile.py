
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SoftwareSourcesProfile(Base):
    '''
    Query depot contents image profiles
    '''
    moid = 'ha-cli-handler-software-sources-profile'
    def list(self, depot, proxy=None):
        '''
        List all the image profiles in a depot.
        :param depot: string[], Specifies full remote URLs of the depot index.xml or server file path pointing to an offline bundle .zip file.
        :param proxy: string, Specifies a proxy server to use for HTTP, FTP, and HTTPS connections. The format is proxy-url:port.
        :returns: vim.EsxCLI.software.sources.profile.list.ImageProfileSummary[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.software.sources.profile.List',
                            depot=depot,
                            proxy=proxy,
                            )
    def get(self, depot, profile, proxy=None):
        '''
        Display details about an image profile from the depot.
        :param depot: string[], Specifies full remote URLs of the depot index.xml or server file path pointing to an offline bundle .zip file.
        :param profile: string, Specifies the name of the image profile to display.
        :param proxy: string, Specifies a proxy server to use for HTTP, FTP, and HTTPS connections. The format is proxy-url:port.
        :returns: vim.EsxCLI.software.sources.profile.get.ImageProfile
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.software.sources.profile.Get',
                            depot=depot,
                            profile=profile,
                            proxy=proxy,
                            )   