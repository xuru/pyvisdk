
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageCoreClaimrule(Base):
    '''
    Operations pertaining to the pluggable storage architecture claiming rule system. These operations operate on the rules used to determine the PSA plugin used to claim storage paths.
    '''
    moid = 'ha-cli-handler-storage-core-claimrule'
    def load(self, claimruleclass=None):
        '''
        Load path claiming rules from config file into the VMkernel.
        :param claimruleclass: string, Indicate the claim rule class to use in this operation [MP, Filter, VAAI, all].
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.claimrule.Load',
                            claimruleclass=claimruleclass,
                            )
    def convert(self, commit=None):
        '''
        Convert ESX 3.x style /adv/Disk/MaskLUNs LUN masks to Claim Rule format.
WARNING: This conversion will not work for all input MaskLUNs variations! Please inspect the list of generated claim rules carefuly, then if the suggested LUN mask claim rules are correct use the --commit parameter to write the list to the config file.
        :param commit: boolean, Force LUN mask config changes to be saved. If this parameter is omitted, config file changes will not be saved.
        :returns: vim.EsxCLI.storage.core.claimrule.convert.ConvertedClaimRule[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.claimrule.Convert',
                            commit=commit,
                            )
    def run(self, adapter=None, channel=None, claimruleclass=None, device=None, lun=None, path=None, target=None, type=None, wait=None):
        '''
        Execute path claiming rules.
        :param adapter: string, If the --type parameter is 'location' this value indicates the name of the host bus adapter for the paths you wish to run claim rules on. This parameter can be omitted to indicate claim rules should be run on paths from all adapters.
        :param channel: long, If the --type parameter is 'location' this value indicates the value of the SCSI channel number for the paths you wish to run claim rules on. This parameter can be omitted to indicate claim rules should be run on paths with any channel number.
        :param claimruleclass: string, Indicate the claim rule class to use in this operation [MP, Filter].
        :param device: string, Indicate the Device Uid to use for this operation.
        :param lun: long, If the --type paramter is 'location' this value indicates the value of the SCSI Logical Unit Number (LUN) for the paths you wish to run claim rules on. This parameter can be omitted to indicate claim rules should be run on paths with any Logical Unit Number.
        :param path: string, If the --type paramter is 'path' this value indicates the unique path identifier (UID) or the runtime name of a path which you wish to run claim rules on.
        :param target: long, If the --type parameter is 'location' this value indicates the value of the SCSI target number for the paths you wish to run claim rules on. This parameter can be omitted to indicate claim rules should be run on paths with any target number.
        :param type: string, Indicate the type of claim run you wish to perform. By default the value of 'all' will be used indicating you wish to run claim rules without restricting the run to specific paths or SCSI addresses. Valid values for this parameter are  [location, path, device, all]
        :param wait: boolean, If the --wait flag is provided then the claim command will wait until device registration has completed to return. This option is only valid when used with the --all option.
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.claimrule.Run',
                            adapter=adapter,
                            channel=channel,
                            claimruleclass=claimruleclass,
                            device=device,
                            lun=lun,
                            path=path,
                            target=target,
                            type=type,
                            wait=wait,
                            )
    def move(self, newrule, rule, claimruleclass=None):
        '''
        Move a claimrule from one rule id to another
        :param claimruleclass: string, Indicate the claim rule class to use in this operation [MP, Filter, VAAI].
        :param newrule: long, Indicate the new rule id you wish to apply to the rule given by the --rule parameter.
        :param rule: long, Indicate the rule ID to use for this operation.
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.claimrule.Move',
                            claimruleclass=claimruleclass,
                            newrule=newrule,
                            rule=rule,
                            )
    def list(self, claimruleclass=None):
        '''
        List all the claimrules on the system.
        :param claimruleclass: string, Indicate the claim rule class to use in this operation [MP, Filter, VAAI, all].
        :returns: vim.EsxCLI.storage.core.claimrule.list.PSAClaimRule[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.claimrule.List',
                            claimruleclass=claimruleclass,
                            )
    def remove(self, claimruleclass=None, plugin=None, rule=None):
        '''
        Delete a claimrule to the set of claimrules on the system.
        :param claimruleclass: string, Indicate the claim rule class to use in this operation [MP, Filter, VAAI].
        :param plugin: string, Indicate the plugin to use for this operation.
        :param rule: long, Indicate the rule ID to use for this operation.
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.claimrule.Remove',
                            claimruleclass=claimruleclass,
                            plugin=plugin,
                            rule=rule,
                            )
    def add(self, plugin, type, adapter=None, autoassign=None, channel=None, claimruleclass=None, device=None, driver=None, force=None, ifunset=None, iqn=None, lun=None, model=None, rule=None, target=None, transport=None, vendor=None, wwnn=None, wwpn=None):
        '''
        Add a claimrule to the set of claimrules on the system.
        :param adapter: string, Indicate the adapter of the paths to use in this operation.
        :param autoassign: boolean, The system will auto assign a rule id.
        :param channel: long, Indicate the channel of the paths to use in this operation.
        :param claimruleclass: string, Indicate the claim rule class to use in this operation [MP, Filter, VAAI].
        :param device: string, Indicate the Device Uid to use for this operation.
        :param driver: string, Indicate the driver of the paths to use in this operation.
        :param force: boolean, Force claim rules to ignore validity checks and install the rule anyway.
        :param ifunset: string, Execute this command if this advanced user variable is not set to 1
        :param iqn: string, Indicate the iSCSI Qualified Name for the target to use in this operation.
        :param lun: long, Indicate the LUN of the paths to use in this operation.
        :param model: string, Indicate the model of the paths to use in this operation.
        :param plugin: string, Indicate which PSA plugin to use for this operation.
        :param rule: long, Indicate the rule ID to use for this operation.
        :param target: long, Indicate the target of the paths to use in this operation.
        :param transport: string, Indicate the transport of the paths to use in this operation.  Valid Values are:  [block, fc, iscsi, iscsivendor, ide, sas, sata, usb, parallel, unknown]
        :param type: string, Indicate which type of matching used for claim/unclaim or claimrule. Valid values are:  [vendor, location, driver, transport, device, target]
        :param vendor: string, Indicate the vendor of the paths to user in this operation.
        :param wwnn: string, Indicate the World-Wide Node Number for the target to use in this operation.
        :param wwpn: string, Indicate the World-Wide Port Number for the target to use in this operation.
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.claimrule.Add',
                            adapter=adapter,
                            autoassign=autoassign,
                            channel=channel,
                            claimruleclass=claimruleclass,
                            device=device,
                            driver=driver,
                            force=force,
                            ifunset=ifunset,
                            iqn=iqn,
                            lun=lun,
                            model=model,
                            plugin=plugin,
                            rule=rule,
                            target=target,
                            transport=transport,
                            type=type,
                            vendor=vendor,
                            wwnn=wwnn,
                            wwpn=wwpn,
                            )   