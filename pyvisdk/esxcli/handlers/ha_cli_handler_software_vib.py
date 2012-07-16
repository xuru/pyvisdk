
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SoftwareVib(Base):
    '''
    Install, update, remove, or display individual VIB packages
    '''
    moid = 'ha-cli-handler-software-vib'
    def update(self, depot=None, dryrun=None, force=None, maintenancemode=None, noliveinstall=None, nosigcheck=None, proxy=None, vibname=None, viburl=None):
        '''
        Update installed VIBs to newer VIB packages. No new VIBs will be installed, only updates. WARNING: If your installation requires a reboot, you need to disable HA first.
        :param depot: string[], Specifies full remote URLs of the depot index.xml or server file path pointing to an offline bundle .zip file.
        :param dryrun: boolean, Performs a dry-run only. Report the VIB-level operations that would be performed, but do not change anything in the system.
        :param force: boolean, Bypasses checks for package dependencies, conflicts, obsolescence, and acceptance levels. Really not recommended unless you know what you are doing.  Use of this option will result in a warning being displayed in the vSphere Client.
        :param maintenancemode: boolean, Pretends that maintenance mode is in effect. Otherwise, installation will stop for live installs that require maintenance mode. This flag has no effect for reboot required remediations.
        :param noliveinstall: boolean, Forces an install to /altbootbank even if the VIBs are eligible for live installation or removal. Will cause installation to be skipped on PXE-booted hosts.
        :param nosigcheck: boolean, Bypasses acceptance level verification, including signing. Use of this option poses a large security risk and will result in a SECURITY ALERT warning being displayed in the vSphere Client.
        :param proxy: string, Specifies a proxy server to use for HTTP, FTP, and HTTPS connections. The format is proxy-url:port.
        :param vibname: string[], Specifies VIBs from a depot, using one of the following forms: name, name:version, vendor:name, or vendor:name:version. VIB packages which are not updates will be skipped.
        :param viburl: string[], Specifies one or more URLs to VIB packages to update to. http:, https:, ftp:, and file: are all supported. VIB packages which are not updates will be skipped.
        :returns: vim.EsxCLI.software.vib.update.InstallationResult
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.software.vib.Update',
                            depot=depot,
                            dryrun=dryrun,
                            force=force,
                            maintenancemode=maintenancemode,
                            noliveinstall=noliveinstall,
                            nosigcheck=nosigcheck,
                            proxy=proxy,
                            vibname=vibname,
                            viburl=viburl,
                            )
    def list(self, rebootingimage=None):
        '''
        Lists the installed VIB packages
        :param rebootingimage: boolean, Displays information for the ESXi image which becomes active after a reboot, or nothing if the pending-reboot image has not been created yet. If not specified, information from the current ESXi image in memory will be returned.
        :returns: vim.EsxCLI.software.vib.list.VIBSummary[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.software.vib.List',
                            rebootingimage=rebootingimage,
                            )
    def remove(self, vibname, dryrun=None, force=None, maintenancemode=None, noliveinstall=None):
        '''
        Removes VIB packages from the host. WARNING: If your installation requires a reboot, you need to disable HA first.
        :param dryrun: boolean, Performs a dry-run only. Report the VIB-level operations that would be performed, but do not change anything in the system.
        :param force: boolean, Bypasses checks for package dependencies, conflicts, obsolescence, and acceptance levels. Really not recommended unless you know what you are doing. Use of this option will result in a warning being displayed in the vSphere Client.
        :param maintenancemode: boolean, Pretends that maintenance mode is in effect. Otherwise, remove will stop for live removes that require maintenance mode. This flag has no effect for reboot required remediations.
        :param noliveinstall: boolean, Forces an remove to /altbootbank even if the VIBs are eligible for live removal. Will cause installation to be skipped on PXE-booted hosts.
        :param vibname: string[], Specifies one or more VIBs on the host to remove. Must be one of the following forms: name, name:version, vendor:name, vendor:name:version.
        :returns: vim.EsxCLI.software.vib.remove.InstallationResult
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.software.vib.Remove',
                            dryrun=dryrun,
                            force=force,
                            maintenancemode=maintenancemode,
                            noliveinstall=noliveinstall,
                            vibname=vibname,
                            )
    def install(self, depot=None, dryrun=None, force=None, maintenancemode=None, noliveinstall=None, nosigcheck=None, proxy=None, vibname=None, viburl=None):
        '''
        Installs VIB packages from a URL or depot. VIBs may be installed, upgraded, or downgraded. WARNING: If your installation requires a reboot, you need to disable HA first.
        :param depot: string[], Specifies full remote URLs of the depot index.xml or server file path pointing to an offline bundle .zip file.
        :param dryrun: boolean, Performs a dry-run only. Report the VIB-level operations that would be performed, but do not change anything in the system.
        :param force: boolean, Bypasses checks for package dependencies, conflicts, obsolescence, and acceptance levels. Really not recommended unless you know what you are doing. Use of this option will result in a warning being displayed in the vSphere Client.
        :param maintenancemode: boolean, Pretends that maintenance mode is in effect. Otherwise, installation will stop for live installs that require maintenance mode. This flag has no effect for reboot required remediations.
        :param noliveinstall: boolean, Forces an install to /altbootbank even if the VIBs are eligible for live installation or removal. Will cause installation to be skipped on PXE-booted hosts.
        :param nosigcheck: boolean, Bypasses acceptance level verification, including signing. Use of this option poses a large security risk and will result in a SECURITY ALERT warning being displayed in the vSphere Client.
        :param proxy: string, Specifies a proxy server to use for HTTP, FTP, and HTTPS connections. The format is proxy-url:port.
        :param vibname: string[], Specifies VIBs from a depot, using one of the following forms: name, name:version, vendor:name, or vendor:name:version.
        :param viburl: string[], Specifies one or more URLs to VIB packages to install. http:, https:, ftp:, and file: are all supported.
        :returns: vim.EsxCLI.software.vib.install.InstallationResult
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.software.vib.Install',
                            depot=depot,
                            dryrun=dryrun,
                            force=force,
                            maintenancemode=maintenancemode,
                            noliveinstall=noliveinstall,
                            nosigcheck=nosigcheck,
                            proxy=proxy,
                            vibname=vibname,
                            viburl=viburl,
                            )
    def get(self, rebootingimage=None, vibname=None):
        '''
        Displays detailed information about one or more installed VIBs
        :param rebootingimage: boolean, Displays information for the ESXi image which becomes active after a reboot, or nothing if the pending-reboot image has not been created yet. If not specified, information from the current ESXi image in memory will be returned.
        :param vibname: string[], Specifies one or more installed VIBs to display more information about. If this option is not specified, then all of the installed VIBs will be displayed. Must be one of the following forms: name, name:version, vendor:name, or vendor:name:version.
        :returns: vim.EsxCLI.software.vib.get.VIB[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.software.vib.Get',
                            rebootingimage=rebootingimage,
                            vibname=vibname,
                            )   