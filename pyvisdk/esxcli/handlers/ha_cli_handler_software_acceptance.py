
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SoftwareAcceptance(Base):
    '''
    Retrieve and set the host acceptance level setting
    '''
    moid = 'ha-cli-handler-software-acceptance'
    def set(self, level):
        '''
        Sets the host acceptance level. This controls what VIBs will be allowed on a host.
        :param level: string, Specifies the acceptance level to set. Should be one of VMwareCertified / VMwareAccepted / PartnerSupported / CommunitySupported.
        :returns: string
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.software.acceptance.Set',
                            level=level,
                            )
    def get(self):
        '''
        Gets the host acceptance level. This controls what VIBs will be allowed on a host.
        :returns: string
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.software.acceptance.Get',
                            )   