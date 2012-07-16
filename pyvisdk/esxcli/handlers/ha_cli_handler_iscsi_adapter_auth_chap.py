
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiAdapterAuthChap(Base):
    '''
    Operations that can be performed on iSCSI adapter CHAP authentication
    '''
    moid = 'ha-cli-handler-iscsi-adapter-auth-chap'
    def set(self, adapter, authname=None, default=None, direction=None, level=None, secret=None):
        '''
        Set the iSCSI CHAP authentication for the iSCSI Host Bus Adapter.
        :param adapter: string, The iSCSI adapter name.
        :param authname: string, The iSCSI CHAP authentication name
        :param default: boolean, Resetting iSCSI CHAP authenthication setting to default.
        :param direction: string, The iSCSI CHAP authentication direction ( [uni, mutual])
        :param level: string, The iSCSI CHAP authentication level ( [prohibited, discouraged, preferred, required])
        :param secret: string, The iSCSI CHAP authentication secret
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.auth.chap.Set',
                            adapter=adapter,
                            authname=authname,
                            default=default,
                            direction=direction,
                            level=level,
                            secret=secret,
                            )
    def get(self, adapter, direction=None):
        '''
        Get the iSCSI CHAP authentication for the iSCSI Host Bus Adapter.
        :param adapter: string, The iSCSI adapter name.
        :param direction: string, The iSCSI CHAP authentication direction ( [uni, mutual])
        :returns: vim.EsxCLI.iscsi.adapter.auth.chap.get.AdapterChapAuth[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.auth.chap.Get',
                            adapter=adapter,
                            direction=direction,
                            )   