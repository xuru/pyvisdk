
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SoftwareSourcesVib(Base):
    '''
    Query depot contents for VIBs; display information about VIB URLs and files
    '''
    moid = 'ha-cli-handler-software-sources-vib'
    def list(self, depot, proxy=None):
        '''
        List all the VIBs from depots.
        :param depot: string[], Specifies full remote URLs of the depot index.xml or server file path pointing to an offline bundle .zip file.
        :param proxy: string, Specifies a proxy server to use for HTTP, FTP, and HTTPS connections. The format is proxy-url:port.
        :returns: vim.EsxCLI.software.sources.vib.list.VIBSummary[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.software.sources.vib.List',
                            depot=depot,
                            proxy=proxy,
                            )
    def get(self, depot=None, proxy=None, vibname=None, viburl=None):
        '''
        Displays detailed information about one or more VIB packages in the depot
        :param depot: string[], Specifies full remote URLs of the depot index.xml or server file path pointing to an offline bundle .zip file.
        :param proxy: string, Specifies a proxy server to use for HTTP, FTP, and HTTPS connections. The format is proxy-url:port.
        :param vibname: string[], Specifies one or more VIBs in the depot to display more information about. If this option is not specified, then all of the VIB packages from the depot will be displayed. Must be one of the following forms: name, name:version, vendor:name, or vendor:name:version.
        :param viburl: string[], Specifies one or more URLs to VIB packages to display information about. http:, https:, ftp:, and file: are all supported.
        :returns: vim.EsxCLI.software.sources.vib.get.VIB[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.software.sources.vib.Get',
                            depot=depot,
                            proxy=proxy,
                            vibname=vibname,
                            viburl=viburl,
                            )   