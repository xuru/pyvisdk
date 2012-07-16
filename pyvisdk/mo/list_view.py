
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.managed_object_view import ManagedObjectView

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ListView(ManagedObjectView):
    '''The ListView managed object provides access to updates on a specific set of
    objects. You can use a ListView with a PropertyCollector method to retrieve
    data or receive notification of changes. For information about using views with
    the PropertyCollector, see the description of ViewManager.When you invoke the
    CreateListView method, you specify a list of objects. The view list always
    represents the current configuration of the virtual environment and reflects
    any subsequent changes that occur.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.ListView):
        super(ListView, self).__init__(core, name=name, ref=ref, type=type)

    

    
    
    def ModifyListView(self, add=None, remove=None):
        '''Modify the list by giving a delta of entities to add and entities to
        remove.Modify the list by giving a delta of entities to add and entities to
        remove.
        
        :param add: Optional list of objects to add to the view.
        
        :param remove: Optional list of objects to remove from the view.
        
        '''
        return self.delegate("ModifyListView")(add, remove)
    
    def ResetListView(self, obj=None):
        '''Replaces the list with an entirely new set of objects. If the entire set is
        changing, this is less data to send than a delta.Replaces the list with an
        entirely new set of objects. If the entire set is changing, this is less data
        to send than a delta.
        
        :param obj: The new list of objects.
        
        '''
        return self.delegate("ResetListView")(obj)
    
    def ResetListViewFromView(self, view):
        '''Replaces the list with the set of objects in a given view.
        
        :param view: The view to copy objects from.
        
        '''
        return self.delegate("ResetListViewFromView")(view)