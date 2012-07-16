
from pyvisdk.esxcli.executer import execute_soap
from pyvisdk.esxcli.base import Base

class VmProcess(Base):
    '''
    Operations on running virtual machine processes
    '''
    moid = 'ha-cli-handler-vm-process'
    def list(self):
        '''
        List the virtual machines on this system. This command currently will only list running VMs on the system.
        :returns: vim.EsxCLI.vm.process.list.VirtualMachine[]
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.vm.process.List',
                            )
    def kill(self, type, worldid):
        '''
        Used to forcibly kill Virtual Machines that are stuck and not responding to normal stop operations.
        :param type: string, The type of kill operation to attempt. There are three types of VM kills that can be attempted:   [soft, hard, force]. Users should always attempt 'soft' kills first, which will give the VMX process a chance to shutdown cleanly (like kill or kill -SIGTERM). If that does not work move to 'hard' kills which will shutdown the process immediately (like kill -9 or kill -SIGKILL). 'force' should be used as a last resort attempt to kill the VM. If all three fail then a reboot is required.
        :param worldid: long, The World ID of the Virtual Machine to kill. This can be obtained from the 'vm process list' command
        :returns: boolean
        '''
        return execute_soap(self._client, self._host, self.moid, 'vim.EsxCLI.vm.process.Kill',
                            type=type,
                            worldid=worldid,
                            )   