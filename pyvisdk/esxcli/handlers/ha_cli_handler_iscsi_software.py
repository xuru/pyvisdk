
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class IscsiSoftware(Base):
    '''
    Operations that can be performed on software iSCSI
    '''
    moid = 'ha-cli-handler-iscsi-software'
    def set(self, enabled):
        '''
        Enable or disable software iSCSI.
        :param enabled: boolean, Enable or disable the module.
        :returns: string
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.software.Set',
                            enabled=enabled,
                            )
    def get(self):
        '''
        Software iSCSI information.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.iscsi.software.Get',
                            )   