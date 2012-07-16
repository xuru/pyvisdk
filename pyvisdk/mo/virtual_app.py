
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.resource_pool import ResourcePool

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class VirtualApp(ResourcePool):
    '''Represents a multi-tiered software solution. A vApp is a collection of virtual
    machines (and potentially other vApp containers) that are operated and
    monitored as a unit. From a manage perspective, a multi-tiered vApp acts a lot
    like a virtual machine object. It has power operations, networks, datastores,
    and its resource usage can be configured.From a technical perspective, a vApp
    container is a specialized resource pool that has been extended with the
    following capabilities:Destroying a vAppWhen a vApp is destroyed, all of its
    virtual machines are destroyed, as well as any child vApps.The VApp.Delete
    privilege must be held on the vApp as well as the parent folder of the vApp.
    Also, the VApp.Delete privilege must be held on any child vApps that would be
    destroyed by the operation.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.VirtualApp):
        super(VirtualApp, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def childLink(self):
        '''List of linked children'''
        return self.update('childLink')
    @property
    def datastore(self):
        '''A collection of references to the subset of datastore objects used by this
        vApp.'''
        return self.update('datastore')
    @property
    def network(self):
        '''A collection of references to the subset of network objects that is used by
        this virtual machine.'''
        return self.update('network')
    @property
    def parentFolder(self):
        '''A reference to the parent folder in the VM and Template folder hierarchy. This
        is only set for a root vApp. A root vApp is a vApp that is not a child of
        another vApp.'''
        return self.update('parentFolder')
    @property
    def parentVApp(self):
        '''Reference to the parent vApp.'''
        return self.update('parentVApp')
    @property
    def vAppConfig(self):
        '''Configuration of this package.'''
        return self.update('vAppConfig')

    
    
    def CloneVApp_Task(self, name, target, spec):
        '''Creates a clone of this vApp.Creates a clone of this vApp.Creates a clone of
        this vApp.Creates a clone of this vApp.Creates a clone of this vApp.
        
        :param name: The name of the new vApp.
        
        :param target: The parent entity of the new vApp. Must be of type ResourcePool or VirtualApp.
        
        :param spec: Specifies how to clone the vApp.
        
        '''
        return self.delegate("CloneVApp_Task")(name, target, spec)
    
    def ExportVApp(self):
        '''Obtains an export lease on this vApp. The export lease contains a list of URLs
        for the disks of the virtual machines in this vApp, as well as a ticket that
        gives access to these URLs.Obtains an export lease on this vApp. The export
        lease contains a list of URLs for the disks of the virtual machines in this
        vApp, as well as a ticket that gives access to these URLs.
        
        '''
        return self.delegate("ExportVApp")()
    
    def PowerOffVApp_Task(self, force):
        '''Stops this vApp.Stops this vApp.Stops this vApp.
        
        :param force: If force is false, the shutdown order in the vApp is executed. If force is true, all virtual machines are powered-off (regardless of shutdown order).
        
        '''
        return self.delegate("PowerOffVApp_Task")(force)
    
    def PowerOnVApp_Task(self):
        '''Starts this vApp.Starts this vApp.Starts this vApp.Starts this vApp.
        
        '''
        return self.delegate("PowerOnVApp_Task")()
    
    def SuspendVApp_Task(self):
        '''Suspends this vApp.Suspends this vApp.Suspends this vApp.
        
        '''
        return self.delegate("SuspendVApp_Task")()
    
    def unregisterVApp_Task(self):
        '''Removes this vApp from the inventory without removing any of the virtual
        machine's files on disk. All high-level information stored with the management
        server (ESX Server or VirtualCenter) is removed, including information such as
        vApp configuration, statistics, permissions, and alarms.
        
        '''
        return self.delegate("unregisterVApp_Task")()
    
    def UpdateLinkedChildren(self, addChangeSet=None, removeSet=None):
        '''Reconfigure the set of linked children.Reconfigure the set of linked
        children.Reconfigure the set of linked children.Reconfigure the set of linked
        children.Reconfigure the set of linked children.Reconfigure the set of linked
        children.Reconfigure the set of linked children.Reconfigure the set of linked
        children.
        
        :param addChangeSet: a set of LinkInfo objects that either add a new link or modify an exisiting link.
        
        :param removeSet: a set of entities that should no longer link to this vApp.
        
        '''
        return self.delegate("UpdateLinkedChildren")(addChangeSet, removeSet)
    
    def UpdateVAppConfig(self, spec):
        '''Updates the vApp configuration.Updates the vApp configuration.
        
        :param spec: contains the updates to the current configuration. Any set element, is changed. All values in the spec that is left unset, will not be modified.
        
        '''
        return self.delegate("UpdateVAppConfig")(spec)