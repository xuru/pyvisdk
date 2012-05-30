
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SystemSecpolicyDomain(Base):
    '''
    Options related to VMkernel access control security domains.
    '''
    moid = 'ha-cli-handler-system-secpolicy-domain'
    def set(self, level, alldomains=None, name=None):
        '''
        Set the enforcement level for a domain in the system. Any option specified here is not persistent and will not survive a reboot of the system.
        :param alldomains: boolean, All domains.
        :param level: string, The enforcement level.
        :param name: string, The domain name.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.secpolicy.domain.Set',
                            alldomains=alldomains,
                            level=level,
                            name=name,
                            )
    def list(self):
        '''
        List the enforcement level for each domain.
        :returns: vim.EsxCLI.system.secpolicy.domain.list.DomainList[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.system.secpolicy.domain.List',
                            )   