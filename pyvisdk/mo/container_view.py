
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.managed_object_view import ManagedObjectView
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ContainerView(ManagedObjectView):
    '''The ContainerView managed object provides a means of monitoring the contents of a
        single container and, optionally, other containers. You can use a
        ContainerView with a PropertyCollector method to retrieve data or receive
        notification of changes. For information about using views with the
        ViewManager.
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.ContainerView):
        # MUST define these
        super(ContainerView, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def recursive(self):
        '''
        Whether to include only the immediate children of the container instance, or to
        include additional objects by following the paths beyond the immediate
        children.
        '''
        return self.update('recursive')

    @property
    def type(self):
        '''
        An optional list of types to be applied to the set of objects in the view. The
        list of types indicates objects that are included in the view. If empty,
        all types are included.
        '''
        return self.update('type')

