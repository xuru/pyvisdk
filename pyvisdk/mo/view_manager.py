
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.base.base_entity import BaseEntity

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ViewManager(BaseEntity):
    '''The ViewManager managed object provides methods to create ContainerView,
    InventoryView, and ListView managed objects. The ViewManager also maintains a
    list of managed object references to the views that you have created. Use the
    viewList property to access the views.A View is a mechanism that supports
    selection of objects on the server and subsequently, access to those objects.
    Views can simplify the task of retrieving data from the server. When you use a
    view, you can use a single invocation of a PropertyCollector method to retrieve
    data or receive notification of changes instead of multiple invocations
    involving multiple filter specifications. A view exists until you destroy it or
    until the end of the session.The ViewManager supports the following views:* A
    ContainerView is based on Folder, Datacenter, ComputeResource, ResourcePool, or
    HostSystem managed objects. Use a container view to monitor the container
    contents and optionally, its descendants. * A ListView managed object is based
    on an arbitrary but specific set of objects. When you create a list view, you
    provide a list of objects to populate the view (CreateListView), or you provide
    an existing view from which the new view is created (CreateListViewFromView). *
    An InventoryView managed object is based on the entire inventory. Use an
    inventory view as a general mechanism to monitor the inventory or portions of
    the inventory.For example, you might use the following sequence of operations
    to get the names of all the virtual machines on a server:'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.ViewManager):
        super(ViewManager, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def viewList(self):
        '''An array of view references. Each array entry is a managed object reference to
        a view created by this ViewManager.'''
        return self.update('viewList')

    
    
    def CreateContainerView(self, container, recursive, type=None):
        '''Create a ContainerView managed object for this session. The method returns a
        reference to a ContainerView object that has a list of managed object
        references. The list references objects in the container and may include
        references to objects from additional containers. You can configure the
        resulting list of objects by specifying a type list and recursion. Once you
        have created the view, the object list always represents the current
        configuration of the virtual environment and reflects any subsequent changes
        that occur.
        
        :param container: A reference to an instance of a Folder, Datacenter, ComputeResource, ResourcePool, or HostSystem object.
        
        :param type: An optional list of managed entity types. The server associates only objects of the specified type(s) with the view. If you specify an empty array, the server uses all types.
        
        :param recursive: Whether to include only the immediate children of the container instance, or to include additional objects by following paths beyond the immediate children.* Folder object - childEntity property. If recursive is false, the container list includes the reference to the child entity in the folder instance. If recursive is true, the server will follow the child folder path(s) to collect additional childEntity references. * ResourcePool object - vm and resourcePool properties. If recursive is false, the object list will contain references to the virtual machines associated with this resource pool, and references to virtual machines associated with the immediate child resource pools. If recursive is true, the server will follow all child resource pool paths extending from the immediate children (and their children, and so on) to collect additional references to virtual machines. * ComputeResource object - host and resourcePool properties. If recursive is false, the object list will contain references to the host systems associated with this compute resource, references to virtual machines associated with the host systems, and references to virtual machines associated with the immediate child resource pools. If recursive is true, the server will follow the child resource pool paths (and their child resource pool paths, and so on) to collect additional references to virtual machines. * Datacenter object - vmFolder, hostFolder, datastoreFolder, and networkFolder properties. If recursive is set to false, the server uses the immediate child folders for the virtual machines, hosts, datastores, and networks associated with this datacenter. If recursive is set to true, the server will follow the folder paths to collect references to additional objects. * HostSystem object - vm property. The view object list contains references to the virtual machines associated with this host system. The value of recursive does not affect this behavior.
        
        '''
        return self.delegate("CreateContainerView")(container, type, recursive)
    
    def CreateInventoryView(self):
        '''Create a new InventoryView managed object for this session.
        
        '''
        return self.delegate("CreateInventoryView")()
    
    def CreateListView(self, obj=None):
        '''Create a ListView object for this session. The method returns a session object
        that has a list of managed object references. The list of references
        corresponds to the input object list. You can modify the resulting list after
        you have created the object.
        
        :param obj: The initial list of objects in the view.
        
        '''
        return self.delegate("CreateListView")(obj)
    
    def CreateListViewFromView(self, view):
        '''Create a ListView object for this session. This method uses an existing view to
        construct the object list for the new view.
        
        :param view: The view that will provide the object list for the new ListView object.
        
        '''
        return self.delegate("CreateListViewFromView")(view)