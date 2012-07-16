
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class StorageCoreClaiming(Base):
    '''
    Operations pertaining to the pluggable storage direct path claiming system. These operations will allow a user to directly control the claiming and unclaiming process. These operations are considered temporary and any claiming operations that need to survive a reboot should use claimrules instead.
    '''
    moid = 'ha-cli-handler-storage-core-claiming'
    def unclaim(self, type, adapter=None, channel=None, claimruleclass=None, device=None, driver=None, lun=None, model=None, path=None, plugin=None, target=None, vendor=None):
        '''
        1) Unclaim a path or set of paths, disassociating them from a PSA plugin. NOTES:  It is normal for path claiming to fail especially when unclaiming by plugin or adapter. Only inactive paths with no I/O  will be able to be unclaimed. Typically the ESXi USB partition and devices with VMFS volumes on them will not be unclaimable. Also NOTE unclaiming will not persist and periodic path claiming will reclaim these paths in the near future unless claim rules are configured to mask the path. 2) Detach a (set of) filter(s) from one or more devices.
        :param adapter: string, If the --type paramter is 'location' this value indicates the name of the host bus adapter for the paths you wish to unclaim. This parameter can be omitted to indicate unclaiming should be run on paths from all adapters.
        :param channel: long, If the --type parameter is 'location' this value indicates the value of the SCSI channel number for the paths you wish to unclaim. This parameter can be omitted to indicate unclaiming should be run on paths with any channel number.
        :param claimruleclass: string, Indicate the claim rule class to use in this operation [MP, Filter].
        :param device: string, If the --type parameter is 'device' attempt to unclaim all paths to a specific device (for multipathing plugins) or unclaim the device itself (for filter plugins). NOTE. For paths, if there are any active I/O operations on this device, at least 1 path will fail to unclaim.
        :param driver: string, If the --type parameter is 'driver' attempt to unclaim all paths provided by a specific HBA driver.
        :param lun: long, If the --type paramter is 'location' this value indicates the value of the SCSI Logical Unit Number (LUN) for the paths you wish to unclaim. This parameter can be omitted to indicate unclaiming should be run on paths with any Logical Unit Number.
        :param model: string, If the --type parameter is 'vendor' attempt to unclaim all paths to devices with specific model info (for multipathing plugins) or unclaim the device itself (for filter plugins). NOTE. For paths, if there are any active I/O operations on this device, at least 1 path will fail to unclaim.
        :param path: string, If the --type parameter is 'path' attempt to unclaim a specific path given its path UID or runtime name.
        :param plugin: string, If the --type parameter is 'plugin' attempt to unclaim all paths on for a given multipath plugin OR all devices attached to a filter plugin.
        :param target: long, If the --type paramter is 'location' this value indicates the value of the SCSI target number for the paths you wish to unclaim. This parameter can be omitted to indicate unclaiming should be run on paths with any target number.
        :param type: string, Indicate the type of unclaim you wish to perform. Valid values for this paramter are  [location, path, driver, device, plugin, vendor]
        :param vendor: string, If the --type parameter is 'vendor' attempt to unclaim all paths to devices with specific vendor info (for multipathing plugins) or unclaim the device itself (for filter plugins). NOTE. For paths, if there are any active I/O operations on this device, at least 1 path will fail to unclaim.
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.claiming.Unclaim',
                            adapter=adapter,
                            channel=channel,
                            claimruleclass=claimruleclass,
                            device=device,
                            driver=driver,
                            lun=lun,
                            model=model,
                            path=path,
                            plugin=plugin,
                            target=target,
                            type=type,
                            vendor=vendor,
                            )
    def autoclaim(self, enabled, claimruleclass=None, wait=None):
        '''
        Control the automatic PSA (path/device) claiming code allowing the disabling of the automatic claiming process or re-enabling of the claiming process if it was previously disabled. By default the automatic PSA claiming process is on and should not be disabled by users unless specifically instructed to do so.
        :param claimruleclass: string, Indicate the claim rule class to use in this operation [MP, Filter, VAAI, all].
        :param enabled: boolean, Set the autoclaiming enabled state for a givenPSA plugin type in the VMkernel. Default is to have this process enabled. This should not be changed by users unless specifically instructed to do so.
        :param wait: boolean, If the --wait flag is provided then the autoclaim enable will wait for paths to 'settle' before running the claim operation.  This means that the system is reasonably sure that all paths on the system have appeared before enabling autoclaim.
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.claiming.Autoclaim',
                            claimruleclass=claimruleclass,
                            enabled=enabled,
                            wait=wait,
                            )
    def reclaim(self, device):
        '''
         Attempt to unclaim all paths to a device and then run the loaded claimrules on each of the paths unclaimed to attempt to reclaim them.
        :param device: string, Reclaim requires the name of a device on which all paths will be unclaimed and then reclaimed.
        :returns: void
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.storage.core.claiming.Reclaim',
                            device=device,
                            )   