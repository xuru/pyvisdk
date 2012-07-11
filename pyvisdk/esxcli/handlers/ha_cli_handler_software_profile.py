
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class SoftwareProfile(Base):
    '''
    Display, install, update or validates image profiles
    '''
    moid = 'ha-cli-handler-software-profile'
    def validate(self, depot, profile, proxy=None):
        '''
        Validates the current image profile on the host against an image profile in a depot.
        :param depot: string[], Specifies full remote URLs of the depot index.xml or server file path pointing to an offline bundle .zip file.
        :param profile: string, Specifies the name of the image profile to validate the host with.
        :param proxy: string, Specifies a proxy server to use for HTTP, FTP, and HTTPS connections. The format is proxy-url:port.
        :returns: vim.EsxCLI.software.profile.validate.ProfileValidationResult
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.software.profile.Validate',
                            depot=depot,
                            profile=profile,
                            proxy=proxy,
                            )
    def update(self, depot, profile, allowdowngrades=None, dryrun=None, force=None, maintenancemode=None, noliveinstall=None, nosigcheck=None, proxy=None):
        '''
        Updates the host with VIBs from an image profile in a depot. Installed VIBs may be upgraded (or downgraded if --allow-downgrades is specified), but they will not be removed. Any VIBs in the image profile which are not related to any installed VIBs will be added to the host. WARNING: If your installation requires a reboot, you need to disable HA first.
        :param allowdowngrades: boolean, If this option is specified, then the VIBs from the image profile which update, downgrade, or are new to the host will be installed. If the option is not specified, then the VIBs which update or are new to the host will be installed.
        :param depot: string[], Specifies full remote URLs of the depot index.xml or server file path pointing to an offline bundle .zip file.
        :param dryrun: boolean, Performs a dry-run only. Report the VIB-level operations that would be performed, but do not change anything in the system.
        :param force: boolean, Bypasses checks for package dependencies, conflicts, obsolescence, and acceptance levels. Really not recommended unless you know what you are doing. Use of this option will result in a warning being displayed in the vSphere Client.
        :param maintenancemode: boolean, Pretends that maintenance mode is in effect. Otherwise, installation will stop for live installs that require maintenance mode. This flag has no effect for reboot required remediations.
        :param noliveinstall: boolean, Forces an install to /altbootbank even if the VIBs are eligible for live installation or removal. Will cause installation to be skipped on PXE-booted hosts.
        :param nosigcheck: boolean, Bypasses acceptance level verification, including signing. Use of this option poses a large security risk and will result in a SECURITY ALERT warning being displayed in the vSphere Client.
        :param profile: string, Specifies the name of the image profile to update the host with.
        :param proxy: string, Specifies a proxy server to use for HTTP, FTP, and HTTPS connections. The format is proxy-url:port.
        :returns: vim.EsxCLI.software.profile.update.InstallationResult
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.software.profile.Update',
                            allowdowngrades=allowdowngrades,
                            depot=depot,
                            dryrun=dryrun,
                            force=force,
                            maintenancemode=maintenancemode,
                            noliveinstall=noliveinstall,
                            nosigcheck=nosigcheck,
                            profile=profile,
                            proxy=proxy,
                            )
    def install(self, depot, profile, dryrun=None, force=None, maintenancemode=None, noliveinstall=None, nosigcheck=None, oktoremove=None, proxy=None):
        '''
        Installs or applies an image profile from a depot to this host. This command completely replaces the installed image with the image defined by the new image profile, and may result in the loss of installed VIBs. The common vibs between host and image profile will be skipped. To preserve installed VIBs, use profile update instead. WARNING: If your installation requires a reboot, you need to disable HA first.
        :param depot: string[], Specifies full remote URLs of the depot index.xml or server file path pointing to an offline bundle .zip file.
        :param dryrun: boolean, Performs a dry-run only. Report the VIB-level operations that would be performed, but do not change anything in the system.
        :param force: boolean, Bypasses checks for package dependencies, conflicts, obsolescence, and acceptance levels. Really not recommended unless you know what you are doing. Use of this option will result in a warning being displayed in the vSphere Client.
        :param maintenancemode: boolean, Pretends that maintenance mode is in effect. Otherwise, installation will stop for live installs that require maintenance mode. This flag has no effect for reboot required remediations.
        :param noliveinstall: boolean, Forces an install to /altbootbank even if the VIBs are eligible for live installation or removal. Will cause installation to be skipped on PXE-booted hosts.
        :param nosigcheck: boolean, Bypasses acceptance level verification, including signing. Use of this option poses a large security risk and will result in a SECURITY ALERT warning being displayed in the vSphere Client.
        :param oktoremove: boolean, Allows the removal of installed VIBs as part of applying the image profile. If not specified, esxcli will error out if applying the image profile results in the removal of installed VIBs.
        :param profile: string, Specifies the name of the image profile to install.
        :param proxy: string, Specifies a proxy server to use for HTTP, FTP, and HTTPS connections. The format is proxy-url:port.
        :returns: vim.EsxCLI.software.profile.install.InstallationResult
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.software.profile.Install',
                            depot=depot,
                            dryrun=dryrun,
                            force=force,
                            maintenancemode=maintenancemode,
                            noliveinstall=noliveinstall,
                            nosigcheck=nosigcheck,
                            oktoremove=oktoremove,
                            profile=profile,
                            proxy=proxy,
                            )
    def get(self, rebootingimage=None):
        '''
        Display the installed image profile and host acceptance level.
        :param rebootingimage: boolean, Displays information for the ESXi image which becomes active after a reboot, or nothing if the pending-reboot image has not been created yet.  If not specified, information from the current ESXi image in memory will be returned.
        :returns: vim.EsxCLI.software.profile.get.ImageProfile
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.software.profile.Get',
                            rebootingimage=rebootingimage,
                            )   