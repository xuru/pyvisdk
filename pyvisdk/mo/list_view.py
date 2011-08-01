
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.managed_object_view import ManagedObjectView
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ListView(ManagedObjectView):
    '''The ListView managed object provides access to updates on a specific set of
        objects. You can use a ListView with a PropertyCollector method to
        retrieve data or receive notification of changes. For information about
        using views with the ViewManager.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.ListView):
        # MUST define these
        super(ListView, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def ResetListViewFromView(self):
        '''Replaces the list with the set of objects in a given view.
        '''
        
        return self.delegate("ResetListViewFromView")()
        

    def ResetListView(self):
        '''Replaces the list with an entirely new set of objects. If the entire set is
        changing, this is less data to send than a delta.May partially succeed if
        some objects could not be resolved. The operation will still succeed for
        all objects which could be resolved, and the list of those which failed is
        as the result.

        :rtype: ManagedObjectReference[] 

        '''
        
        return self.delegate("ResetListView")()
        

    def ModifyListView(self):
        '''Modify the list by giving a delta of entities to add and entities to remove.May
        partially succeed if some objects could not be resolved. The operation
        will still succeed for all objects which could be resolved, and the list
        of those which failed is returned as the result.

        :rtype: ManagedObjectReference[] 

        '''
        
        return self.delegate("ModifyListView")()
        
