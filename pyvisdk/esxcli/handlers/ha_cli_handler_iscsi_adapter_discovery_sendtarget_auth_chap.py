
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiAdapterDiscoverySendtargetAuthChap(Base):
    '''
    Operations that can be performed on iSCSI sendtarget's CHAP authentication
    '''
    moid = 'ha-cli-handler-iscsi-adapter-discovery-sendtarget-auth-chap'
    def set(self, adapter, address, authname=None, default=None, direction=None, inherit=None, level=None, secret=None):
        '''
        Set iSCSI CHAP authentication on a sendtarget address
        :param adapter: string, The iSCSI adapter name.
        :param address: string, The iSCSI sendtarget address: <ip/dns[:port]>
        :param authname: string, The iSCSI authentication name
        :param default: boolean, Resetting iSCSI authentication setting to default.
        :param direction: string, The iSCSI authentication direction ( [uni, mutual])
        :param inherit: boolean, Inheriting iSCSI authentication setting from parent.
        :param level: string, The iSCSI authentication level ( [prohibited, discouraged, preferred, required])
        :param secret: string, The iSCSI authentication secret
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.discovery.sendtarget.auth.chap.Set',
                            adapter=adapter,
                            address=address,
                            authname=authname,
                            default=default,
                            direction=direction,
                            inherit=inherit,
                            level=level,
                            secret=secret,
                            )
    def get(self, adapter, address, direction=None):
        '''
        Get iSCSI CHAP authentication on a sendtarget address
        :param adapter: string, The iSCSI adapter name.
        :param address: string, The iSCSI sendtarget address: <ip/dns[:port]>
        :param direction: string, The iSCSI authentication direction ( [uni, mutual])
        :returns: vim.EsxCLI.iscsi.adapter.discovery.sendtarget.auth.chap.get.Sendtarget[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.discovery.sendtarget.auth.chap.Get',
                            adapter=adapter,
                            address=address,
                            direction=direction,
                            )   