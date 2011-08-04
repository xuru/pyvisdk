
from pyvisdk.mo.consts import ManagedEntityTypes
from pyvisdk.mo.managed_object_view import ManagedObjectView
import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ContainerView(ManagedObjectView):
    '''* Folder * Datacenter * ComputeResource * ResourcePool * HostSystem
    '''
    def __init__(self, core, name=None, ref=None, type=ManagedEntityTypes.ContainerView):
        # MUST define these
        super(ContainerView, self).__init__(core, name=name, ref=ref, type=type)
    
    
    @property
    def container(self):
        '''The Folder, Datacenter, ComputeResource, ResourcePool, or HostSystem instance that
        provides the objects that the view presents.
        '''
        return self.update('container')

    @property
    def recursive(self):
        '''Whether to include only the immediate children of the container instance, or to
        include additional objects by following the paths beyond the immediate
        children.
        '''
        return self.update('recursive')

    @property
    def type(self):
        '''An optional list of types to be applied to the set of objects in the view. The
        list of types indicates objects that are included in the view. If empty,
        all types are included.
        '''
        return self.update('type')

