
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class NetworkIp(Base):
    '''
    Operations that can be performed on vmknics
    '''
    moid = 'ha-cli-handler-network-ip'
    def set(self, ipv6enabled=None):
        '''
        Update global IP settings
        :param ipv6enabled: boolean, Enable or disable IPv6 (Reboot Required)
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.ip.Set',
                            ipv6enabled=ipv6enabled,
                            )
    def get(self):
        '''
        Get global IP settings
        :returns: vim.EsxCLI.network.ip.get.IPInfo
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.network.ip.Get',
                            )   