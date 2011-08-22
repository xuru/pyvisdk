
from pyvisdk.base.managed_object_types import ManagedObjectTypes
from pyvisdk.mo.managed_object_view import ManagedObjectView
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ListView(ManagedObjectView):
    '''The ListView managed object provides access to updates on a specific set of
    objects. You can use a ListView with a ViewManager.When you invoke the
    CreateListView method, you specify a list of objects. The view list always
    represents the current configuration of the virtual environment and reflects
    any subsequent changes that occur.'''
    
    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.ListView):
        super(ListView, self).__init__(core, name=name, ref=ref, type=type)
    
    
    
    
    
    def ModifyListView(self):
        '''Modify the list by giving a delta of entities to add and entities to remove.May
        partially succeed if some objects could not be resolved. The operation will
        still succeed for all objects which could be resolved, and the list of those
        which failed is returned as the result.
        :rtype: 
        :returns: 
        '''
        return self.delegate("ModifyListView")()
    
    def ResetListView(self):
        '''Replaces the list with an entirely new set of objects. If the entire set is
        changing, this is less data to send than a delta.May partially succeed if some
        objects could not be resolved. The operation will still succeed for all objects
        which could be resolved, and the list of those which failed is as the result.
        :rtype: 
        :returns: 
        '''
        return self.delegate("ResetListView")()
    
    def ResetListViewFromView(self):
        '''Replaces the list with the set of objects in a given view.
        :rtype: None
        :returns: 
        '''
        return self.delegate("ResetListViewFromView")()