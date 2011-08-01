
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.base_entity import BaseEntity
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ViewManager(BaseEntity):
    '''The ViewManager managed object provides methods to create ContainerView,
        InventoryView, and ListView managed objects. The ViewManager also
        maintains a list of managed object references to the views that you have
        created. Use the viewList property to access the views.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.ViewManager):
        # MUST define these
        super(ViewManager, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def CreateInventoryView(self):
        '''Create a new InventoryView managed object for this session.

        :rtype: ManagedObjectReference to a InventoryView 

        '''
        
        return self.delegate("CreateInventoryView")()
        

    def CreateContainerView(self):
        '''Create a ContainerView managed object for this session. The method returns a
        reference to a ContainerView object that has a list of managed object
        references. The list references objects in the container and may include
        references to objects from additional containers. You can configure the
        resulting list of objects by specifying a type list and recursion. Once
        you have created the view, the object list always represents the current
        configuration of the virtual environment and reflects any subsequent
        changes that occur.

        :rtype: ManagedObjectReference to a ContainerView 

        '''
        
        return self.delegate("CreateContainerView")()
        

    def CreateListViewFromView(self):
        '''Create a ListView object for this session. This method uses an existing view to
        construct the object list for the new view.

        :rtype: ManagedObjectReference to a ListView 

        '''
        
        return self.delegate("CreateListViewFromView")()
        

    def CreateListView(self):
        '''Create a ListView object for this session. The method returns a session object
        that has a list of managed object references. The list of references
        corresponds to the input object list. You can modify the resulting list
        after you have created the object.

        :rtype: ManagedObjectReference to a ListView 

        '''
        
        return self.delegate("CreateListView")()
        
