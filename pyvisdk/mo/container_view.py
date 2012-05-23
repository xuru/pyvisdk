
from pyvisdk.base.managed_object_types import ManagedObjectTypes

from pyvisdk.mo.managed_object_view import ManagedObjectView

import logging

########################################
# Automatically generated, do not edit.
########################################

log = logging.getLogger(__name__)

class ContainerView(ManagedObjectView):
    '''The ContainerView managed object provides a means of monitoring the contents of
    a single container and, optionally, other containers. You can use a
    ContainerView with a PropertyCollector method to retrieve data or receive
    notification of changes. For information about using views with the
    PropertyCollector, see the description of ViewManager.When you invoke the
    CreateContainerView method, you specify a managed object instance that provides
    the starting point for object selection. You can use the following managed
    objects as the basis of a container view:* Folder * Datacenter *
    ComputeResource * ResourcePool * HostSystemOnce you have created the view, the
    view list always represents the current configuration of the virtual
    environment and reflects any subsequent changes that occur.'''

    def __init__(self, core, name=None, ref=None, type=ManagedObjectTypes.ContainerView):
        super(ContainerView, self).__init__(core, name=name, ref=ref, type=type)

    
    @property
    def container(self):
        '''The Folder, Datacenter, ComputeResource, ResourcePool, or HostSystem instance
        that provides the objects that the view presents.'''
        return self.update('container')
    @property
    def recursive(self):
        '''Whether to include only the immediate children of the container instance, or to
        include additional objects by following the paths beyond the immediate
        children.'''
        return self.update('recursive')
    @property
    def type(self):
        '''An optional list of types to be applied to the set of objects in the view. The
        list of types indicates objects that are included in the view. If empty, all
        types are included.'''
        return self.update('type')

    