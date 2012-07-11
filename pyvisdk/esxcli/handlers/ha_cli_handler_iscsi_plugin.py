
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiPlugin(Base):
    '''
    Operations that can be performed on iSCSI management plugins
    '''
    moid = 'ha-cli-handler-iscsi-plugin'
    def list(self, adapter=None, plugin=None):
        '''
        List IMA plugins.
        :param adapter: string, The iSCSI adapter name.
        :param plugin: string, The IMA plugin file name.
        :returns: vim.EsxCLI.iscsi.plugin.list.iScsiPlugin[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.plugin.List',
                            adapter=adapter,
                            plugin=plugin,
                            )   