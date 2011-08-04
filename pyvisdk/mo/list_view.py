
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.managed_object_view import ManagedObjectView
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ListView(ManagedObjectView):
    '''Properties
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.ListView):
        # MUST define these
        super(ListView, self).__init__(core, name=name, ref=ref, type=type)
    
    

    def ModifyListView(self, add, remove):
        '''Modify the list by giving a delta of entities to add and entities to remove.May
        partially succeed if some objects could not be resolved. The operation
        will still succeed for all objects which could be resolved, and the list
        of those which failed is returned as the result.

        :param add: Optional list of objects to add to the view.

        :param remove: Optional list of objects to remove from the view.


        :rtype: ManagedObjectReference[] 

        '''
        
        return self.delegate("ModifyListView")(add,remove)
        

    def ResetListView(self, obj):
        '''Replaces the list with an entirely new set of objects. If the entire set is
        changing, this is less data to send than a delta.May partially succeed if
        some objects could not be resolved. The operation will still succeed for
        all objects which could be resolved, and the list of those which failed is
        as the result.

        :param obj: The new list of objects.


        :rtype: ManagedObjectReference[] 

        '''
        
        return self.delegate("ResetListView")(obj)
        

    def ResetListViewFromView(self, view):
        '''Replaces the list with the set of objects in a given view.

        :param view: The view to copy objects from.

        '''
        
        return self.delegate("ResetListViewFromView")(view)
        
