
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.resource_pool import ResourcePool
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualApp(ResourcePool):
    '''Represents a multi-tiered software solution. A vApp is a collection of virtual
        machines (and potentially other vApp containers) that are operated and
        monitored as a unit. From a manage perspective, a multi-tiered vApp acts a
        lot like a virtual machine object. It has power operations, networks,
        datastores, and its resource usage can be configured.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.VirtualApp):
        # MUST define these
        super(VirtualApp, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def CloneVApp_Task(self, name, spec):
        '''Creates a clone of this vApp.Any % (percent) character used in this name parameter
        must be escaped, unless it is used to start an escape sequence. Clients
        may also escape any other characters in this name parameter.When invoking
        this method, the following privilege checks occur:

        :param name: The name of the new vApp.

        :param spec: Specifies how to clone the vApp.


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("CloneVApp_Task")(name,spec)
        

    def ExportVApp(self):
        '''Obtains an export lease on this vApp. The export lease contains a list of URLs for
        the disks of the virtual machines in this vApp, as well as a ticket that
        gives access to these URLs.See HttpNfcLease for information on how to use
        the lease.

        :rtype: ManagedObjectReference to a HttpNfcLease 

        '''
        
        return self.delegate("ExportVApp")()
        

    def UpdateVAppConfig(self, spec):
        '''Updates the vApp configuration.Updates in different areas require different
        privileges. See VAppConfigSpec for a full description.

        :param spec: contains the updates to the current configuration. Any set element, is changed. All values in the spec that is left unset, will not be modified.

        '''
        
        return self.delegate("UpdateVAppConfig")(spec)
        

    def unregisterVApp_Task(self):
        '''Removes this vApp from the inventory without removing any of the virtual machine's
        files on disk. All high-level information stored with the management
        server (ESX Server or VirtualCenter) is removed, including information
        such as vApp configuration, statistics, permissions, and alarms.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("unregisterVApp_Task")()
        

    def SuspendVApp_Task(self):
        '''Suspends this vApp.Suspends all powered-on virtual machines in a vApp, including
        virtual machines in child vApps. The virtual machines are suspended in the
        same order as used for a power-off operation (reverse power-on
        sequence).While a vApp is being suspended, all power operations performed
        on sub entities are disabled through the VIM API. They will throw
        TaskInProgress.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("SuspendVApp_Task")()
        

    def PowerOnVApp_Task(self):
        '''Starts this vApp.The virtual machines (or sub vApps) will be started in the order
        specified in the vApp configuration. If the vApp is suspended (@see
        vim.VirtualApp.Summary.suspended), all suspended virtual machines will be
        powered-on based on the defined start-up order.While a vApp is starting,
        all power operations performed on sub entities are disabled through the
        VIM API. They will throw TaskInProgress.In case of a failure to power-on a
        virtual machine, the exception from the virtual machine power on is
        returned, and the power-on sequence will be terminated. In case of a
        failure, virtual machines that are already started will remain powered-on.

        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("PowerOnVApp_Task")()
        

    def PowerOffVApp_Task(self, force):
        '''Stops this vApp.The virtual machines (or child vApps) will be stopped in the order
        specified in the vApp configuration, if force is false. If force is set to
        true, all virtual machines are powered-off (in no specific order and
        possibly in parallel) regardless of the vApp auto-start
        configuration.While a vApp is stopping, all power operations performed on
        sub entities are disabled through the VIM API. They will throw
        TaskInProgress.

        :param force: If force is false, the shutdown order in the vApp is executed. If force is true, all virtual machines are powered-off (regardless of shutdown order).


        :rtype: ManagedObjectReference to a Task 

        '''
        
        return self.delegate("PowerOffVApp_Task")(force)
        

    def UpdateLinkedChildren(self):
        '''Reconfigure the set of linked children.A VirtualMachine and vApp can be added as a
        linked child as long as it is not a direct child of another vApp. In case
        it is a linked child, the existing link is removed and replaced with the
        new link specified in this call.An InvalidArgument fault is thrown if a
        link target is a direct child of another vApp, or if the addition of the
        link will result in a vApp with a cycle. For example, a vApp cannot be
        linked to itself.The removeSet must refer to managed entities that are
        currently linked children. Otherwise, an InvalidArgument exception is
        thrown.For each entity being linked, the operation is subject to the
        following privilege checks:
        '''
        
        return self.delegate("UpdateLinkedChildren")()
        
