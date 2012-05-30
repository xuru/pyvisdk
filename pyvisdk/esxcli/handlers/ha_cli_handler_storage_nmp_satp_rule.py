
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageNmpSatpRule(Base):
    '''
    Operations pertaining to claimrules for Storage Array Type Plug-ins.
    '''
    moid = 'ha-cli-handler-storage-nmp-satp-rule'
    def add(self, satp, boot=None, claimoption=None, description=None, device=None, driver=None, force=None, model=None, option=None, psp=None, pspoption=None, transport=None, type=None, vendor=None):
        '''
        Add a rule to the list of claim rules for the given SATP.
        :param boot: boolean, This is a system default rule added at boot time. Do not modify esx.conf or add to host profile.
        :param claimoption: string, Set the claim option string when adding a SATP claim rule.
        :param description: string, Set the claim rule description when adding a SATP claim rule.
        :param device: string, Set the device when adding SATP claim rules. Device rules are mutually exclusive with vendor/model and driver rules.
        :param driver: string, Set the driver string when adding a SATP claim rule. Driver rules are mutually exclusive with vendor/model rules.
        :param force: boolean, Force claim rules to ignore validity checks and install the rule anyway.
        :param model: string, Set the model string when adding SATP a claim rule. Vendor/Model rules are mutually exclusive with driver rules.
        :param option: string, Set the option string when adding a SATP claim rule.
        :param psp: string, Set the default PSP for the SATP claim rule.
        :param pspoption: string, Set the PSP options for the SATP claim rule.
        :param satp: string, The SATP for which a new rule will be added.
        :param transport: string, Set the claim transport type string when adding a SATP claim rule.
        :param type: string, Set the claim type when adding a SATP claim rule.
        :param vendor: string, Set the vendor string when adding SATP claim rules. Vendor/Model rules are mutually exclusive with driver rules.
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nmp.satp.rule.Add',
                            boot=boot,
                            claimoption=claimoption,
                            description=description,
                            device=device,
                            driver=driver,
                            force=force,
                            model=model,
                            option=option,
                            psp=psp,
                            pspoption=pspoption,
                            satp=satp,
                            transport=transport,
                            type=type,
                            vendor=vendor,
                            )
    def list(self, satp=None):
        '''
        List the claiming rules for Storage Array Type Plugins (SATP)
        :param satp: string, Filter the SATP rules to a specific SATP
        :returns: vim.EsxCLI.storage.nmp.satp.rule.list.StorageArrayTypePluginRule[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nmp.satp.rule.List',
                            satp=satp,
                            )
    def remove(self, satp, boot=None, claimoption=None, description=None, device=None, driver=None, model=None, option=None, psp=None, pspoption=None, transport=None, type=None, vendor=None):
        '''
        Delete a rule from the list of claim rules for the given SATP.
        :param boot: boolean, This is a system default rule added at boot time. Do not modify esx.conf or add to host profile.
        :param claimoption: string, The claim option string for the SATP claim rule to delete.
        :param description: string, The desription string for the SATP claim rule to delete.
        :param device: string, The device for the SATP claim rule to delete
        :param driver: string, The driver string for the SATP claim rule to delete.
        :param model: string, The model string for the SATP claim rule to delete.
        :param option: string, The option string for the SATP claim rule to delete.
        :param psp: string, The default PSP for the SATP claim rule to delete.
        :param pspoption: string, The PSP options for the SATP claim rule to delete.
        :param satp: string, The SATP for which a rule will be deleted.
        :param transport: string, The transport type for the SATP claim rule to delete.
        :param type: string, Set the claim type when adding a SATP claim rule.
        :param vendor: string, The vendor string for the SATP claim rule to delete
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.nmp.satp.rule.Remove',
                            boot=boot,
                            claimoption=claimoption,
                            description=description,
                            device=device,
                            driver=driver,
                            model=model,
                            option=option,
                            psp=psp,
                            pspoption=pspoption,
                            satp=satp,
                            transport=transport,
                            type=type,
                            vendor=vendor,
                            )   