
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.managed_object_view import ManagedObjectView
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class InventoryView(ManagedObjectView):
    '''The InventoryView managed object provides a means of browsing the inventory and
        tracking changes to open folders. This managed object is particularly
        useful for UI clients that display a tree-based navigation panel of the
        inventory.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.InventoryView):
        # MUST define these
        super(InventoryView, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def OpenInventoryViewFolder(self):
        '''Adds the child objects of a given managed entity to the view.If a Datacenter is
        returned as a child, the implicit virtual machine folder and host folder
        objects are also returned. If a ComputeResource is returned, the implicit
        root ResourcePool and HostSystem objects are also returned.May partially
        succeed if some entities could not be resolved. The operation will still
        succeed for all entities which could be resolved, and the list of those
        which failed is returned as the result.

        :rtype: ManagedObjectReference[] to a ManagedEntity[] 

        '''
        
        return self.delegate("OpenInventoryViewFolder")()
        

    def CloseInventoryViewFolder(self):
        '''Notify the server that folder(s) have been closed, and changes for all its
        contained objects should no longer be sent. The associated child objects
        are removed from the view. The containers themselves will still be
        retained as open objects until their parent is closed.May partially
        succeed if some entities could not be resolved. The operation will still
        succeed for all entities that could be resolved, and the list of those
        that failed is returned as the result.

        :rtype: ManagedObjectReference[] to a ManagedEntity[] 

        '''
        
        return self.delegate("CloseInventoryViewFolder")()
        
