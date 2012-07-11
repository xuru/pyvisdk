
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiAdapterTargetPortalAuthChap(Base):
    '''
    Operations that can be performed on iSCSI target portal CHAP authentications
    '''
    moid = 'ha-cli-handler-iscsi-adapter-target-portal-auth-chap'
    def set(self, adapter, address, name, authname=None, default=None, direction=None, inherit=None, level=None, secret=None):
        '''
        Set the iSCSI CHAP authentication for the iSCSI Target.
        :param adapter: string, The iSCSI adapter name.
        :param address: string, The iSCSI target address: <ip/dns[:port]>
        :param authname: string, The iSCSI authentication name
        :param default: boolean, Resetting iSCSI authentication setting to default.
        :param direction: string, The iSCSI authentication direction ( [uni, mutual])
        :param inherit: boolean, Inheriting iSCSI authentication setting from parent.
        :param level: string, The iSCSI authentication level ( [prohibited, discouraged, preferred, required])
        :param name: string, The iSCSI target name: <iqn/eui>
        :param secret: string, The iSCSI authentication password
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.target.portal.auth.chap.Set',
                            adapter=adapter,
                            address=address,
                            authname=authname,
                            default=default,
                            direction=direction,
                            inherit=inherit,
                            level=level,
                            name=name,
                            secret=secret,
                            )
    def get(self, adapter, address, name, direction=None, method=None):
        '''
        Get iSCSI CHAP authentication on a target
        :param adapter: string, The iSCSI adapter name.
        :param address: string, The iSCSI target address: <ip/dns[:port]>
        :param direction: string, The iSCSI authentication direction ( [uni, mutual])
        :param method: string, The iSCSI authentication method ( [chap])
        :param name: string, The iSCSI target name: <iqn/eui>
        :returns: vim.EsxCLI.iscsi.adapter.target.portal.auth.chap.get.TargetAuth[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.target.portal.auth.chap.Get',
                            adapter=adapter,
                            address=address,
                            direction=direction,
                            method=method,
                            name=name,
                            )   