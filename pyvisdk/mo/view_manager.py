
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.base_entity import BaseEntity
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
    
    
    
    def CreateContainerView(self):
        '''Create a ContainerView managed object for this session. The method returns a
        reference to a ContainerView object that has a list of managed object
        references. The list references objects in the container and may include
        references to objects from additional containers. You can configure the
        resulting list of objects by specifying a type list and recursion. Once you
        have created the view, the object list always represents the current
        configuration of the virtual environment and reflects any subsequent changes
        that occur.
        :rtype: ManagedObjectReference to a ContainerView
        :returns: 
        '''
        return self.delegate("CreateContainerView")()
    
    def CreateInventoryView(self):
        '''Create a new InventoryView managed object for this session.
        :rtype: ManagedObjectReference to a InventoryView
        :returns: 
        '''
        return self.delegate("CreateInventoryView")()
    
    def CreateListView(self):
        '''Create a ListView object for this session. The method returns a session object
        that has a list of managed object references. The list of references
        corresponds to the input object list. You can modify the resulting list after
        you have created the object.
        :rtype: ManagedObjectReference to a ListView
        :returns: 
        '''
        return self.delegate("CreateListView")()
    
    def CreateListViewFromView(self):
        '''Create a ListView object for this session. This method uses an existing view to
        construct the object list for the new view.
        :rtype: ManagedObjectReference to a ListView
        :returns: 
        '''
        return self.delegate("CreateListViewFromView")()