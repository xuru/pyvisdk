
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.managed_object_view import ManagedObjectView
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class InventoryView(ManagedObjectView):
    '''InventoryView maintains the view list of managed object references to inventory
        objects. When you create an inventory view (CreateInventoryView), the
        server initializes the view's object list with a single folder - the root
        folder.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.InventoryView):
        # MUST define these
        super(InventoryView, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def CloseInventoryViewFolder(self, entity):
        '''Notify the server that folder(s) have been closed, and changes for all its
        contained objects should no longer be sent. The associated child objects
        are removed from the view. The containers themselves will still be
        retained as open objects until their parent is closed.May partially
        succeed if some entities could not be resolved. The operation will still
        succeed for all entities that could be resolved, and the list of those
        that failed is returned as the result.

        :param entity: An array of managed object references. Each array entry is a reference to an
        entity to collapse.


        :rtype: ManagedEntity[] 

        '''
        
        return self.delegate("CloseInventoryViewFolder")(entity)
        

    def OpenInventoryViewFolder(self, entity):
        '''Adds the child objects of a given managed entity to the view.If a Datacenter is
        returned as a child, the implicit virtual machine folder and host folder
        objects are also returned. If a ComputeResource is returned, the implicit
        root ResourcePool and HostSystem objects are also returned.May partially
        succeed if some entities could not be resolved. The operation will still
        succeed for all entities which could be resolved, and the list of those
        which failed is returned as the result.

        :param entity: An array of managed object references. Each array entry is a reference to an
        entity to expand. Expands each entity in the order given. If an entity is
        not in the current view, expands the view as needed.


        :rtype: ManagedEntity[] 

        '''
        
        return self.delegate("OpenInventoryViewFolder")(entity)
        
