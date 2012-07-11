
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiAdapterTarget(Base):
    '''
    Operations that can be performed on iSCSI targets
    '''
    moid = 'ha-cli-handler-iscsi-adapter-target'
    def list(self, adapter=None, name=None):
        '''
        List iSCSI targets.
        :param adapter: string, The iSCSI adapter name.
        :param name: string, The iSCSI target name.
        :returns: vim.EsxCLI.iscsi.adapter.target.list.Target[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.adapter.target.List',
                            adapter=adapter,
                            name=name,
                            )   